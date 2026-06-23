#!/usr/bin/env python3
"""
save_note_auth.py - note.com 認証情報保存スクリプト（初回1回・セッション切れ時に実行）

1. ブラウザが開きます
2. note.com にログインしてください
3. ログイン完了後 Enter キーを押してください
4. auth_state.json に保存されます
"""

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

OPENCLAW   = Path(r'C:\Users\sawas\.openclaw')
AUTH_FILE  = OPENCLAW / 'auth_state.json'

def main():
    print("=" * 50)
    print(" note.com 認証情報保存ツール")
    print("=" * 50)
    print()

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=False,
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"],
        )
        ctx = browser.new_context(
            viewport={'width': 1280, 'height': 900},
            locale='ja-JP',
        )
        page = ctx.new_page()
        page.goto('https://note.com/login')

        print("ブラウザが開きました。")
        print("note.com にログインしてください。")
        print()
        print("ログイン完了後、このターミナルで Enter キーを押してください...")
        input()

        # ログイン確認（Google OAuth SSO リダイレクトが発生する場合があるため try/except で対処）
        try:
            page.goto('https://note.com', wait_until='domcontentloaded', timeout=20000)
        except Exception:
            pass
        page.wait_for_load_state('networkidle', timeout=30000)

        if 'login' in page.url or 'signin' in page.url:
            print("エラー: ログインが完了していないようです。再度試してください。")
            ctx.close()
            browser.close()
            sys.exit(1)

        # 認証情報保存
        ctx.storage_state(path=str(AUTH_FILE))
        print(f"\n✅ 認証情報を保存しました: {AUTH_FILE}")
        print("   次回からスケジュールタスクが自動投稿できます。")

        ctx.close()
        browser.close()

if __name__ == '__main__':
    main()
