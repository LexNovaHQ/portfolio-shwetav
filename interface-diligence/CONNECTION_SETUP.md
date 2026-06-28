# Interface Diligence Connection Setup

This is the main-domain connection layer for Interface Diligence.

## Architecture

```text
Browser on main domain
→ /api/interface-diligence/*
→ Cloudflare Worker
→ Google Cloud Run diligence backend
```

The browser must not call the Cloud Run URL directly.

## Required Cloudflare environment variable

Set this in the Cloudflare Worker environment:

```text
DILIGENCE_BACKEND_URL=<cloud-run-service-url>
```

Use the full HTTPS Cloud Run service URL. Do not include a trailing slash.

## Public routes proxied

```text
GET  /api/interface-diligence/health
POST /api/interface-diligence/public/reviewer/jobs
GET  /api/interface-diligence/public/reviewer/jobs/:run_id
POST /api/interface-diligence/public/reviewer/jobs/:run_id/advance
GET  /api/interface-diligence/public/reviewer/report/:run_id
```

The Worker strips `/api/interface-diligence` and forwards the remaining path to the backend.

## Build boundary

This patch is connection-only. It intentionally does not implement the final premium report UI.

Confirm connection first, then build UI around `renderer_payload.section_list`.
