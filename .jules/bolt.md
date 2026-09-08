## 2026-03-31 - Standards Mode & Document Header Optimization
**Learning:** Static HTML pages without `<!DOCTYPE html>` force browsers into Quirks Mode (`BackCompat`), incurring layout rendering overhead. Missing `<meta charset="UTF-8">` causes browsers to scan the initial chunks of HTML for character encoding, causing latency, while missing favicon definitions cause redundant 404 network requests.
**Action:** Always include `<!DOCTYPE html>`, early `<meta charset="UTF-8">`, and a data URI favicon (`<link rel="icon" href="data:,">`) in static HTML entries.
