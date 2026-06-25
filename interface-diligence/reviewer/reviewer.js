const els = {
  backendUrl: document.getElementById("backendUrl"),
  apiKey: document.getElementById("apiKey"),
  targetUrl: document.getElementById("targetUrl"),
  runButton: document.getElementById("runButton"),
  statusBox: document.getElementById("statusBox"),
  reportLink: document.getElementById("reportLink")
};

els.backendUrl.value = sessionStorage.getItem("ln_reviewer_backend_url") || "";
els.apiKey.value = sessionStorage.getItem("ln_reviewer_api_key") || "";

els.runButton.addEventListener("click", runDiligence);

async function runDiligence() {
  const backendUrl = cleanBaseUrl(els.backendUrl.value);
  const apiKey = els.apiKey.value.trim();
  const targetUrl = els.targetUrl.value.trim();

  if (!backendUrl || !apiKey || !targetUrl) {
    setStatus({ ok: false, error: "MISSING_INPUT", message: "Backend URL, operator API key, and target URL are required." });
    return;
  }

  sessionStorage.setItem("ln_reviewer_backend_url", backendUrl);
  sessionStorage.setItem("ln_reviewer_api_key", apiKey);
  els.runButton.disabled = true;
  els.reportLink.textContent = "";

  try {
    const created = await request(backendUrl, apiKey, "/v1/reviewer/jobs", {
      method: "POST",
      body: JSON.stringify({ target_url: targetUrl, created_by: "portfolio-reviewer" })
    });

    setStatus(created);

    let latest = created;
    for (let i = 0; i < 20; i += 1) {
      latest = await request(backendUrl, apiKey, `/v1/reviewer/jobs/${created.run_id}/advance`, {
        method: "POST",
        body: JSON.stringify({ max_steps: 1 })
      });
      setStatus(latest);
      if (latest.current_phase === "COMPLETE" || latest.status === "COMPLETE") break;
    }

    if (latest.current_phase === "COMPLETE" || latest.status === "COMPLETE") {
      const href = `report.html?run_id=${encodeURIComponent(created.run_id)}`;
      els.reportLink.innerHTML = `<a href="${href}" target="_blank" rel="noopener">Open report</a>`;
    }
  } catch (error) {
    setStatus({ ok: false, error: "REVIEWER_RUN_FAILED", message: error.message });
  } finally {
    els.runButton.disabled = false;
  }
}

async function request(baseUrl, apiKey, path, init) {
  const response = await fetch(`${baseUrl}${path}`, {
    ...init,
    headers: {
      "content-type": "application/json",
      "x-ln-api-key": apiKey,
      ...(init.headers || {})
    }
  });

  const json = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(`${response.status}: ${JSON.stringify(json)}`);
  }
  return json;
}

function cleanBaseUrl(value) {
  return String(value || "").trim().replace(/\/$/, "");
}

function setStatus(value) {
  els.statusBox.textContent = JSON.stringify(value, null, 2);
}
