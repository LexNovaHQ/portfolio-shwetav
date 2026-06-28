# Reviewer Route

Connection-test pages:

- `index.html` creates and polls diligence runs through `/api/interface-diligence`.
- `report.html` fetches renderer payloads through `/api/interface-diligence`.
- `connection-check.html` verifies Cloudflare-to-GCloud health.

Final premium UI is intentionally not implemented in this patch.
