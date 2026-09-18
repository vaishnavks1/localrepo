## 2026-09-18 - HTML Standards Mode and Early Resource Hints
**Learning:** Omission of `<!DOCTYPE html>` puts browsers in Quirks Mode, triggering slower rendering pathways and legacy layout algorithms. Specifying `<meta charset="UTF-8">` early prevents encoding sniffing pauses, and an empty data URI favicon prevents wasteful 404 network roundtrips.
**Action:** Always include standards doctype, explicit charset meta tag, and data URI favicon for minimal static HTML pages.
