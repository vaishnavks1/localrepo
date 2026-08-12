# Bolt's Journal - Critical Learnings Only

## 2025-08-12 - Standard HTML Pre-optimizations for Bare Projects
**Learning:** For bare-bones static HTML repositories without active build pipelines, immediate high-impact optimizations include switching the document compatibility mode to standard HTML5 mode (`<!DOCTYPE html>`), setting the charset configuration early to bypass browser heuristic scanning overhead, and preventing wasteful automatic 404 network requests for favicon.ico via a light inline data-URI favicon block.
**Action:** Always add standard doctype definitions, UTF-8 charsets, and data-URI favicon links as a low-overhead, high-efficiency performance baseline, taking care to preserve any existing text content outside standard body tags exactly to avoid regressions.
