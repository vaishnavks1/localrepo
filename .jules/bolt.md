# Bolt's Journal

## 2025-02-14 - Standard Static HTML Optimizations
**Learning:** For extremely minimal static HTML web pages, initial rendering performance and network overhead are the primary bottlenecks. Without build tools, optimal browser execution is achieved by leveraging basic HTML performance practices. In Standards Mode (via `<!DOCTYPE html>`), layout and rendering calculations are faster compared to Quirks Mode. Specifying the charset `<meta charset="UTF-8">` within the first 1024 bytes avoids expensive character encoding sniffing, and using a data-URI favicon `<link rel="icon" href="data:,">` eliminates the redundant favicon.ico 404 network request which causes a blocking latency penalty.
**Action:** Always include a doctype, explicit charset definition, and a data-URI favicon in static html files to reduce loading times and eliminate wasteful network lookups.
