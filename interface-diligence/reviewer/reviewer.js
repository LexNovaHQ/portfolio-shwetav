const API_BASE = "/api/interface-diligence";
const POLL_INTERVAL_MS = 4000;
const MAX_POLLS = 240;

const els = {
  targetUrl: document.getElementById("targetUrl"),
  runButton: document.getElementById("runButton"),
  statusBox: document.getElementById("statusBox"),
  reportLink: document.getElementById("reportLink")
};

els.runButton.addEventListener("click", runDiligence);

async function runDiligence() {
  const targetUrl = els.targetUrl.value.trim();

  if (!targetUrl) {
    setStatus({ ok: false, error: "MISSING_INPUT", message: "Target URL is required." });
    return;
  }

  els.runButton.disabled = true;
  els.reportLink.textContent = "";

  try {
    const created = await request("/public/reviewer/jobs", {
      method: "POST",
      body: JSON.stringify({ target_url: targetUrl })
    });

    const runId = created.run_id;
    sessionStorage.setItem("ln_reviewer_last_run_id", runId);
    setStatus({ step: "created", ...created });

    const queued = await request(`/public/reviewer/jobs/${encodeURIComponent(runId)}/advance`, {
      method: "POST",
      body: JSON.stringify({ auto_continue: true, max_steps: 1 })
    });
    setStatus({ step: "queued", ...queued });

    const latest = await pollUntilComplete(runId);
    if (isComplete(latest.run || latest)) {
      const href = `report.html?run_id=${encodeURIComponent(runId)}`;
      els.reportLink.innerHTML = `<a href="${href}" target="_blank" rel="noopener">Open report</a>`;
    }
  } catch (error) {
    setStatus({ ok: false, error: "REVIEWER_RUN_FAILED", message: error.message });
  } finally {
    els.runButton.disabled = false;
  }
}

async function pollUntilComplete(runId) {
  let latest = null;
  for (let i = 0; i < MAX_POLLS; i += 1) {
    await delay(POLL_INTERVAL_MS);
    latest = await request(`/public/reviewer/jobs/${encodeURIComponent(runId)}`, { method: "GET" });
    setStatus({ step: "poll", poll_count: i + 1, ...latest });
    if (isComplete(latest.run || latest)) return latest;
    if (isTerminalFailure(latest.run || latest)) throw new Error(`Run stopped before completion: ${JSON.stringify(latest)}`);
  }
  throw new Error(`Timed out waiting for run ${runId} to complete.`);
}

async function request(path, init = {}) {
  const headers = new Headers(init.headers || {});
  if (init.body && !headers.has("content-type")) headers.set("content-type", "application/json");

  const response = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers
  });

  const json = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(`${response.status}: ${JSON.stringify(json)}`);
  return json;
}

function isComplete(run) {
  return run?.current_phase === "COMPLETE" || run?.status === "COMPLETE";
}

function isTerminalFailure(run) {
  const status = String(run?.status || "").toUpperCase();
  const phase = String(run?.current_phase || "").toUpperCase();
  return status.includes("FAIL") || status.includes("CONTROLLED_FAILURE") || phase.includes("CONTROLLED_FAILURE");
}

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function setStatus(value) {
  els.statusBox.textContent = JSON.stringify(value, null, 2);
}
