# Bolt Journal - Critical learnings only

## 2024-07-29 - Initializing Bolt Journal
**Learning:** In a bare-bones static HTML repository lacking Node.js or dev tooling, critical baseline optimizations like Standards Mode (via Doctype declaration), specifying charset early, and preventing 404 favicon network requests can drastically reduce document compilation/parsing times and eliminate redundant resource requests.
**Action:** Always verify with Playwright via file:// URL and check for document.compatMode === 'CSS1Compat'.
