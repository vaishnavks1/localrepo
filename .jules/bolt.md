# Bolt's Journal

## 2025-02-12 - Initial static HTML performance optimization
**Learning:** For extremely minimal, static HTML web projects with no build step, standard optimizations like triggering CSS1Compat Standards Mode via `<!DOCTYPE html>`, setting the `<meta charset="UTF-8">` early, and preventing 404 favicon requests with a data URI `<link rel="icon" href="data:,">` provide the largest relative performance improvements by avoiding standard parser quirks, rendering delays, and unnecessary network round-trips.
**Action:** When handling minimal static HTML pages, always apply these three core speed optimizations while meticulously preserving all existing text nodes (even those previously outside tag structures) to maintain backward compatibility and avoid breaking functionality.
