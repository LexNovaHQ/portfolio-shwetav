# Interface Diligence Online Test Plan

Use this after the branch is merged and Cloudflare deploys.

## 1. Configure Cloudflare env var

Set:

```text
DILIGENCE_BACKEND_URL=https://<cloud-run-service-url>
```

No trailing slash.

## 2. Verify proxy health

Open:

```text
/interface-diligence/reviewer/connection-check.html
```

Expected:

```json
{ "ok": true, "status": 200 }
```

If it fails with `MISSING_DILIGENCE_BACKEND_URL`, Cloudflare env is not configured.

If it fails with a backend error, the Cloud Run service or public backend config is not ready.

## 3. Create a run

Open:

```text
/interface-diligence/reviewer/
```

Submit a public target URL.

Expected:

- run is created;
- async runner is queued;
- status polling starts;
- current phase advances through backend phases;
- `Open report` appears when complete.

## 4. Verify report fetch

Open the report link:

```text
/interface-diligence/reviewer/report.html?run_id=<run_id>
```

Expected:

- page loads without asking for backend URL;
- report shell appears;
- 11 renderer sections appear;
- each section has a technical payload disclosure;
- no `sessionStorage` backend dependency.

## 5. Do not start premium UI until these pass

The next UI phase should start only after connection, run creation, polling, and report fetch all work on the main domain.
