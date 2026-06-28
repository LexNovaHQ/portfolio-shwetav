const API_PREFIX = "/api/interface-diligence";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === `${API_PREFIX}/health`) {
      return proxyToBackend(request, env, "/health");
    }

    if (url.pathname.startsWith(`${API_PREFIX}/`)) {
      const backendPath = url.pathname.slice(API_PREFIX.length) || "/";
      return proxyToBackend(request, env, `${backendPath}${url.search}`);
    }

    return env.ASSETS.fetch(request);
  }
};

async function proxyToBackend(request, env, pathAndSearch) {
  if (request.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: securityHeaders() });
  }

  const backendBase = String(env.DILIGENCE_BACKEND_URL || "").trim().replace(/\/$/, "");
  if (!backendBase) {
    return json({
      ok: false,
      error: "MISSING_DILIGENCE_BACKEND_URL",
      message: "DILIGENCE_BACKEND_URL is not configured on the Cloudflare Worker."
    }, 500);
  }

  const target = new URL(pathAndSearch, backendBase);
  const headers = new Headers(request.headers);
  headers.delete("host");
  headers.delete("content-length");
  headers.set("x-interface-proxy", "cloudflare-worker");

  const init = {
    method: request.method,
    headers,
    redirect: "manual"
  };

  if (!['GET', 'HEAD'].includes(request.method.toUpperCase())) {
    init.body = request.body;
  }

  const upstream = await fetch(target.toString(), init);
  const responseHeaders = new Headers(upstream.headers);
  for (const [key, value] of securityHeaders()) responseHeaders.set(key, value);

  return new Response(upstream.body, {
    status: upstream.status,
    statusText: upstream.statusText,
    headers: responseHeaders
  });
}

function json(payload, status = 200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      ...Object.fromEntries(securityHeaders())
    }
  });
}

function securityHeaders() {
  return new Map([
    ["cache-control", "no-store"],
    ["referrer-policy", "no-referrer"],
    ["x-content-type-options", "nosniff"]
  ]);
}
