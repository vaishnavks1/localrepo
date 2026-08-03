# Bolt's Journal - Critical Learnings Only

## 2025-02-15 - HTML Baseline Optimization
**Learning:** For extremely minimal, static HTML web projects, standard frontend framework optimizations (such as `React.memo` or bundle-splitting) are not applicable. Instead, critical performance wins include enabling Standards Mode via `<!DOCTYPE html>`, setting `<meta charset="UTF-8">` early to avoid character encoding sniffing/re-parsing, and avoiding wasted 404 network requests for favicon.ico via a data-URI favicon.
**Action:** When working on very basic or boilerplate HTML repositories, immediately implement these three basic optimizations first to establish a solid performance foundation.
