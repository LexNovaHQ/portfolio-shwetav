# Online Gate Lock

The connection layer is the only purpose of this branch.

Locked sequence:

```text
1. Merge and deploy Cloudflare connection patch.
2. Configure DILIGENCE_BACKEND_URL.
3. Confirm health proxy.
4. Confirm run create / queue / poll.
5. Confirm report payload fetch.
6. Only then build premium UI.
```
