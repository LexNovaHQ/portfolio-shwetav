const PROXY_PREFIX = "/api/interface-diligence";

export async function onRequest(context) {
  const { request, env } = context;

  if (request.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: securityHeaders() });
  }

  const backendUrl = String(env.DILIGENCE_BACKEND_URL || "").trim().replace(/\/$/, "");
  if (!backendUrl) {
    return json({ ok: false, error: "MISSING_DILIGENCE_BACKEND_URL", message: "Cloudflare env var DILIGENCE_BACKEND_URL is not configured." }, 500);
  }

  const incoming = new URL(request.url);
  const backendPath = incoming.pathname.startsWith(PROXY_PREFIX)
    ? incoming.pathname.slice(PROXY_PREFIX.length) || "/"
    : incoming.pathname;
  const target = new URL(`${backendPath}${incoming.search}`, backendUrl);

  const headers = new Headers(request.headers);
  headers.delete("host");
  headers.delete("content-length");
  headers.set("x-interface-proxy", "cloudflare-pages");

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
    ["x-content-type-options", "nosniff"],
    ["referrer-policy", "no-referrer"],
    ["cache-control", "no-store"]
  ]);
}
