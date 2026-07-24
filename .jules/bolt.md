# Bolt's Journal

## 2025-07-24 - Document Standard Structure and Data-URI Favicon
**Learning:** For extremely minimal, static HTML web projects, missing doc structure defaults the browser to Quirks Mode, slowing down rendering. Additionally, browsers automatically request `/favicon.ico`, resulting in wasteful 404 network requests and server/connection overhead.
**Action:** Always include `<!DOCTYPE html>`, `<meta charset="UTF-8">`, and a data-URI favicon `<link rel="icon" href="data:,">` to ensure Standards Mode rendering and avoid wasteful favicon 404 requests.
