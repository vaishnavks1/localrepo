# Bolt's Journal

## 2025-08-11 - Static HTML Standards Mode & Favicon Optimizations
**Learning:** For extremely minimal, static HTML web projects with no build steps or bundlers, significant performance and compatibility gains can be achieved with three lightweight changes:
1. Adding `<!DOCTYPE html>` to trigger HTML5 Standards Mode (avoiding the performance-penalizing Quirks Mode).
2. Specifying `<meta charset="UTF-8">` early to prevent character encoding sniffing/re-parsing delays.
3. Specifying a inline, empty data URI favicon (`<link rel="icon" href="data:,">`) to stop browsers from sending an extra HTTP request and waiting on a wasteful 404 response.
**Action:** When working with bare static sites, always apply these low-risk, highly-compatible practices without altering any visible text nodes.
