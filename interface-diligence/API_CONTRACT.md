# Interface Diligence UI API Contract

```text
API base: /api/interface-diligence
Connection mode: same-origin Cloudflare proxy to GCloud backend
```

## Cloudflare environment

```text
DILIGENCE_BACKEND_URL=<Cloud Run service URL>
```

## Routes

```text
GET  /api/interface-diligence/health
POST /api/interface-diligence/public/reviewer/jobs
GET  /api/interface-diligence/public/reviewer/jobs/:run_id
POST /api/interface-diligence/public/reviewer/jobs/:run_id/advance
GET  /api/interface-diligence/public/reviewer/report/:run_id
```

## Frontend rules

```text
manual_backend_url_input_allowed: false
session_storage_backend_url_dependency_allowed: false
cloud_run_url_exposed_to_browser_ui: false
premium_ui_started: false
purpose: connection proof before final UI build
```
