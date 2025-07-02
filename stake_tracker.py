from playwright.sync_api import sync_playwright

def get_stake_game_data(stake_cookie):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Load cookie
        context.add_cookies([{
            "name": "cookie_name",
            "value": stake_cookie,
            "domain": ".stake.com",
            "path": "/",
            "httpOnly": True,
            "secure": True
        }])

        page = context.new_page()
        page.goto("https://stake.com/casino/games/mines")

        page.wait_for_timeout(5000)

        # Extract game state (JS from console)
        data = page.evaluate("""
            () => {
                const mines = window?.store?.state?.mines;
                if (!mines) return null;
                return {
                    clientSeed: mines.clientSeed,
                    mineCount: mines.minesCount,
                    nonce: mines.nonce,
                };
            }
        """)

        browser.close()
        return data
