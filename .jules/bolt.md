# Bolt Journal

## 2024-07-18 - HTML Performance Best Practices
**Learning:** Minimal/incomplete HTML without DOCTYPE, charset, and favicon results in Quirks Mode, encoding sniffing delays, and wasteful 404 network requests.
**Action:** Always structure static web pages with `<!DOCTYPE html>`, `<meta charset="UTF-8">`, and a inline data URI favicon `<link rel="icon" href="data:,">` to ensure Standards Mode rendering and zero-waste network request profile.
