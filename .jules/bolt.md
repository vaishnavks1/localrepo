## 2025-05-15 - [Favicon 404 in minimal HTML]
**Learning:** Even in a barebones HTML file with no assets, browsers will automatically attempt to fetch `/favicon.ico`, resulting in a wasteful 404 network request.
**Action:** Always include `<link rel="icon" href="data:,">` in the `<head>` of minimal HTML projects to silence this request and save a network round-trip.
