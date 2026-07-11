import asyncio
import os
from playwright.async_api import async_playwright

async def verify_performance():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Track failed requests (specifically looking for favicon.ico)
        failed_requests = []
        page.on("requestfailed", lambda request: failed_requests.append(request.url))

        # Also track 404 responses
        page.on("response", lambda response: failed_requests.append(response.url) if response.status == 404 else None)

        # Get the absolute path to index.html
        file_path = f"file://{os.path.join(os.getcwd(), 'index.html')}"
        print(f"Navigating to: {file_path}")

        await page.goto(file_path)

        # 1. Check document.compatMode
        compat_mode = await page.evaluate("document.compatMode")
        print(f"Document compatMode: {compat_mode}")

        # 2. Check for favicon.ico requests that failed/404'd
        favicon_failed = any("favicon.ico" in url for url in failed_requests)
        print(f"Favicon 404 detected: {favicon_failed}")

        await browser.close()

        return {
            "compatMode": compat_mode,
            "favicon_failed": favicon_failed
        }

if __name__ == "__main__":
    results = asyncio.run(verify_performance())
    print("\n--- Summary ---")
    print(f"Standards Mode: {'YES' if results['compatMode'] == 'CSS1Compat' else 'NO (Quirks Mode)'}")
    print(f"Favicon 404 Avoided: {'YES' if not results['favicon_failed'] else 'NO'}")
