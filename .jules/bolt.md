## 2026-08-25 - HTML Document Structure & Standards Mode Optimization

**Learning:** Static HTML pages without `<!DOCTYPE html>` trigger Quirks Mode in browsers, leading to inefficient rendering engine paths. Early `<meta charset="UTF-8">` declaration prevents character encoding sniffing delays during HTML parsing, and data-URI favicons avoid unnecessary 404 network requests.

**Action:** Always include `<!DOCTYPE html>`, early charset declaration, and data-URI favicon in static HTML templates to ensure peak initial render performance and eliminate wasteful HTTP round-trips.
