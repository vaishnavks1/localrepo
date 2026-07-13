## 2025-05-14 - Programmatic verification of Standards Mode
**Learning:** In minimal static HTML projects lacking build tools, performance can be measurably improved by triggering Standards Mode with `<!DOCTYPE html>`. This can be programmatically verified using `document.compatMode`, where 'CSS1Compat' indicates Standards Mode and 'BackCompat' indicates Quirks Mode.
**Action:** Always include `<!DOCTYPE html>` and verify `document.compatMode` in automated tests to ensure optimal browser rendering performance.

## 2025-05-14 - Eliminating 404s for favicon.ico
**Learning:** Browsers automatically request `/favicon.ico`, which results in a wasteful 404 network request and console error if missing. A data-URI favicon `<link rel="icon" href="data:,">` silences this request without requiring a physical file.
**Action:** Use a data-URI favicon in all web projects to reduce unnecessary network traffic and improve load time.
