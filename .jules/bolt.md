# Bolt's Performance Journal

Critical learnings and performance-related discoveries.

## 2025-02-14 - Optimizing Minimal Static HTML Web Pages
**Learning:** For extremely minimal, static web applications lacking build pipelines, standard performance tools, or backend layers, critical frontend optimizations focus on standards mode compliance, character set declaration to bypass character encoding detection/sniffing, and eliminating 404 network requests from implicit favicon lookups.
**Action:** Always include a `<!DOCTYPE html>`, `<meta charset="UTF-8">`, and a blank/data-URI favicon `<link rel="icon" href="data:,">` to prevent wasteful network requests and render blocking behaviors, while ensuring existing free-text/structural nodes are preserved verbatim.
