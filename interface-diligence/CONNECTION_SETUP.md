# Interface Diligence Connection Setup

This folder is wired for the main-domain Cloudflare deployment.

## Runtime shape

```text
Browser on main domain
→ /api/interface-diligence/*
→ Cloudflare Pages Function
→ Google Cloud Run diligence backend
```

The browser must not call the Cloud Run URL directly.

## Required Cloudflare environment variable

Set this in Cloudflare Pages project settings:

```text
DILIGENCE_BACKEND_URL=https://<cloud-run-service-url>
```

Do not include a trailing slash.

## Public routes proxied

```text
POST /api/interface-diligence/public/reviewer/jobs
GET  /api/interface-diligence/public/reviewer/jobs/:run_id
POST /api/interface-diligence/public/reviewer/jobs/:run_id/advance
GET  /api/interface-diligence/public/reviewer/report/:run_id
```

The proxy strips `/api/interface-diligence` and forwards the remaining path to the backend.

## UI boundary

This patch is connection-only. It intentionally does not implement the final premium report UI.

Current reviewer/report pages prove:

1. the main-domain page can create a run;
2. Cloudflare can reach the GCloud backend;
3. the async run can be queued;
4. the browser can poll status;
5. the report page can fetch `renderer_payload` without `sessionStorage` or a manual backend URL.
