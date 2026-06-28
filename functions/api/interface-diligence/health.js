export async function onRequest(context) {
  const backendUrl = String(context.env.DILIGENCE_BACKEND_URL || "").trim().replace(/\/$/, "");
  if (!backendUrl) {
    return new Response(JSON.stringify({ ok: false, error: "MISSING_DILIGENCE_BACKEND_URL" }), {
      status: 500,
      headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" }
    });
  }

  const upstream = await fetch(`${backendUrl}/health`, { headers: { "x-interface-proxy": "cloudflare-pages" } });
  const body = await upstream.text();
  return new Response(body, {
    status: upstream.status,
    statusText: upstream.statusText,
    headers: { "content-type": upstream.headers.get("content-type") || "application/json; charset=utf-8", "cache-control": "no-store" }
  });
}
