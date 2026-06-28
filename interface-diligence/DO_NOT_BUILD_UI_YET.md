# UI Build Gate

Do not start the premium report UI until the online connection passes.

Required checks first:

1. Cloudflare Pages deploy succeeds.
2. `DILIGENCE_BACKEND_URL` is configured.
3. `/interface-diligence/reviewer/connection-check.html` returns backend health.
4. `/interface-diligence/reviewer/` can create a run.
5. The run can queue and poll through the same-origin API.
6. `/interface-diligence/reviewer/report.html?run_id=<run_id>` can fetch the backend renderer payload.

After these pass, build the premium report UI around `renderer_payload.section_list`, not raw legacy JSON.
