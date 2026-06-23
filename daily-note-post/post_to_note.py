#!/usr/bin/env python3
"""
post_to_note.py - note.com 自動投稿スクリプト

使い方:
  1. post_config.json を作成してから実行（日本語引数の文字化け回避のためJSON経由）
  2. python post_to_note.py

post_config.json の形式:
{
  "article_path": "C:\\...\\article39_xxx_for_posting.txt",
  "title": "記事タイトル",
  "price": 600,
  "tags": ["タグ1", "タグ2", "タグ3"]
}

出力:
  SUCCESS: <投稿URL>   → 成功
  AUTH_ERROR: ...      → ログイン切れ（save_note_auth.py を実行）
  FAILED: ...          → その他エラー
"""

import sys, json, os, time, traceback, datetime
from pathlib import Path

SCRIPT_DIR  = Path(__file__).parent
OPENCLAW    = Path(r'C:\Users\sawas\.openclaw')
AUTH_FILE   = OPENCLAW / 'auth_state.json'
CONFIG_FILE = SCRIPT_DIR / 'post_config.json'
QUEUE_FILE  = SCRIPT_DIR / 'post_queue.json'
LOG_FILE    = SCRIPT_DIR / 'post_log.txt'


def load_queue() -> dict | None:
    """post_queue.jsonを読み込む。存在しなければNone。"""
    if not QUEUE_FILE.exists():
        return None
    with open(QUEUE_FILE, encoding='utf-8') as f:
        return json.load(f)


def advance_queue(queue_data: dict) -> None:
    """キューの先頭を削除してpost_queue.jsonを更新し、post_config.jsonも次の記事に更新する。"""
    q = queue_data.get('queue', [])
    if q:
        q.pop(0)
    with open(QUEUE_FILE, 'w', encoding='utf-8') as f:
        json.dump(queue_data, f, ensure_ascii=False, indent=2)
    # 次の記事があればpost_config.jsonも更新
    if q:
        article_dir = queue_data.get('article_dir', '')
        next_file = q[0]
        next_path = str(Path(article_dir) / next_file)
        cfg = {
            'article_path': next_path,
            'title': '',
            'price': queue_data.get('default_price', 600),
            'tags': queue_data.get('tags', ['恋活', 'チャット', '50代'])
        }
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
        log(f"  キュー更新: 次の記事 → {next_file}")

def log(msg):
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(line + '\n')
    except Exception:
        pass

def set_clipboard_windows(text):
    """Windowsシステムクリップボードに直接書き込む（確実な方法）"""
    import subprocess
    # PowerShell経由でクリップボードに設定
    proc = subprocess.Popen(
        ['powershell.exe', '-NoProfile', '-Command',
         '[Console]::InputEncoding = [System.Text.Encoding]::UTF8; '
         '$input | Set-Clipboard'],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    proc.communicate(input=text.encode('utf-8'))
    return proc.returncode == 0

def main():
    sys.stdout.reconfigure(encoding='utf-8')

    # ── キュー or config 読み込み ──
    queue_data = load_queue()
    if queue_data and queue_data.get('queue'):
        # キューが存在し、かつ残りがある場合はキューから読む
        article_dir = queue_data.get('article_dir', '')
        next_file   = queue_data['queue'][0]
        article_path = Path(article_dir) / next_file
        price = int(queue_data.get('default_price', 600))
        tags  = queue_data.get('tags', ['恋活', 'チャット', '50代'])
        title = ''
        cover_image = Path(r'C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\cover_image.jpg')
        log(f"キューモード: {next_file} ({len(queue_data['queue'])}本残り)")
    else:
        # キューが空またはない場合はpost_config.jsonにフォールバック
        if not CONFIG_FILE.exists():
            log(f"FAILED: {CONFIG_FILE} が見つかりません。先に作成してください。")
            sys.exit(1)
        with open(CONFIG_FILE, encoding='utf-8') as f:
            cfg = json.load(f)
        article_path = Path(cfg['article_path'])
        title  = cfg.get('title', '')
        price  = int(cfg.get('price', 100))
        tags   = cfg.get('tags', ['恋活', 'チャット', '50代'])
        cover_image = Path(cfg.get(
            'cover_image',
            r'C:\Users\sawas\.openclaw\workspace\恋活マネタイズプロジェクト\cover_image.jpg'
        ))

    if not article_path.exists():
        log(f"FAILED: 記事ファイルが見つかりません: {article_path}")
        sys.exit(1)

    if not AUTH_FILE.exists():
        log("AUTH_ERROR: auth_state.json がありません。save_note_auth.py を実行してください。")
        sys.exit(2)

    # ── 記事本文読み込み ──
    content = article_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    if not title:
        for i, line in enumerate(lines):
            if line.startswith('#'):
                title = line.lstrip('#').strip()
                lines = lines[i+1:]
                break
        if not title:
            title = article_path.stem

    body = '\n'.join(lines).strip()

    log(f"投稿開始: {title}")
    log(f"  ファイル : {article_path.name}")
    log(f"  価格     : {price}円")
    log(f"  タグ     : {tags}")

    # ── Playwright 起動 ──
    from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=True,
            args=[
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--disable-blink-features=AutomationControlled',
                '--window-size=1280,900',
            ]
        )
        ctx = browser.new_context(
            storage_state=str(AUTH_FILE),
            permissions=['clipboard-read', 'clipboard-write'],
            user_agent=(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/130.0.0.0 Safari/537.36'
            ),
            viewport={'width': 1280, 'height': 900},
            locale='ja-JP',
            timezone_id='Asia/Tokyo',
        )
        page = ctx.new_page()
        page.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        try:
            # ── Step 1: 新規作成ページへ ──
            log("  note.com/notes/new へ移動...")
            page.goto('https://note.com/notes/new', timeout=40000)
            page.wait_for_load_state('domcontentloaded', timeout=30000)
            time.sleep(3)

            cur = page.url
            log(f"  現在URL: {cur}")
            if 'login' in cur or 'signin' in cur or 'sign_in' in cur:
                log("AUTH_ERROR: ログインセッション切れ。save_note_auth.py で再ログインしてください。")
                print("AUTH_ERROR: ログインセッション切れ")
                sys.exit(2)

            # ── Step 2: タイトル入力 ──
            log("  タイトル入力...")
            title_sels = [
                'textarea[placeholder="タイトル"]',
                'textarea[placeholder*="タイトル"]',
                'input[placeholder*="タイトル"]',
                '[data-placeholder*="タイトル"]',
                '.o-noteEditTitle textarea',
                '.p-titleInput',
                'div[contenteditable][data-placeholder*="タイトル"]',
            ]
            title_el = None
            for sel in title_sels:
                try:
                    el = page.locator(sel).first
                    if el.is_visible(timeout=3000):
                        title_el = el
                        log(f"  タイトルセレクタ: {sel}")
                        break
                except Exception:
                    continue

            if title_el is None:
                raise Exception("タイトル入力欄が見つかりません")

            title_el.click()
            # contenteditable か input/textarea かで処理を分ける
            tag = page.evaluate(
                "(el) => el.tagName.toLowerCase()",
                title_el.element_handle()
            )
            if tag in ('input', 'textarea'):
                title_el.fill(title)
            else:
                title_el.type(title)
            time.sleep(0.5)

            # ── Step 2.5: カバー画像アップロード ──
            log(f"  カバー画像アップロード: {cover_image.name}...")
            if cover_image.exists():
                uploaded_cover = False
                # ページ最上部にスクロールしてアイコンを表示
                page.evaluate("window.scrollTo(0, 0)")
                time.sleep(0.8)

                # Step A: ヘッダー画像アイコンをクリック
                header_icon_sels = [
                    '[aria-label*="ヘッダー画像"]',
                    '[aria-label*="カバー画像"]',
                    '[aria-label*="画像を追加"]',
                    '[aria-label*="ヘッダー"]',
                    '[title*="ヘッダー"]',
                    '[title*="カバー"]',
                ]
                icon_clicked = False
                for sel in header_icon_sels:
                    try:
                        el = page.locator(sel).first
                        if el.count() > 0:
                            el.click()
                            time.sleep(1)
                            log(f"  ヘッダー画像アイコンクリック: {sel}")
                            icon_clicked = True
                            break
                    except Exception:
                        continue

                # アイコンが見つからない場合: JS経由でタイトル上部の画像ボタンを探す
                if not icon_clicked:
                    icon_info = page.evaluate("""
                        () => {
                            const candidates = document.querySelectorAll('button, [role="button"]');
                            for (const el of candidates) {
                                const aria = el.getAttribute('aria-label') || '';
                                const title = el.getAttribute('title') || '';
                                const r = el.getBoundingClientRect();
                                if (r.y < 300 && r.y > 30 && r.width > 20 && r.height > 20) {
                                    if (aria.includes('画像') || aria.includes('ヘッダー') || aria.includes('カバー') ||
                                        title.includes('画像') || title.includes('ヘッダー')) {
                                        return {x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2), aria};
                                    }
                                }
                            }
                            return null;
                        }
                    """)
                    if icon_info:
                        page.mouse.click(icon_info['x'], icon_info['y'])
                        time.sleep(1)
                        log(f"  ヘッダー画像アイコン（JS）: {icon_info}")
                        icon_clicked = True

                if icon_clicked:
                    # Step B: ドロップダウンから「画像をアップロード」をクリック → ファイル選択
                    upload_menu_sels = [
                        'button:has-text("画像をアップロード")',
                        'li:has-text("画像をアップロード")',
                        '[role="menuitem"]:has-text("画像をアップロード")',
                    ]
                    for up_sel in upload_menu_sels:
                        try:
                            if page.locator(up_sel).count() > 0:
                                with page.expect_file_chooser(timeout=8000) as fc_info:
                                    page.locator(up_sel).first.click()
                                fc_info.value.set_files(str(cover_image))
                                time.sleep(4)
                                log(f"  カバー画像ファイルセット完了: {cover_image.name}")

                                # クロップ/確認ダイアログを閉じる
                                # ※ ReactEasyCropのCropArea divがポインターイベントを横取りするため
                                #   force=True でインターセプトをバイパスする
                                crop_closed = False
                                time.sleep(2)  # モーダルのレンダリング待ち

                                if page.locator('.reactEasyCrop_CropArea').count() > 0:
                                    log("  クロップモーダル検出（reactEasyCrop_CropArea）")

                                    # モーダル内ボタン一覧をログ
                                    modal_btns = page.evaluate("""
                                        () => Array.from(
                                            document.querySelectorAll('.ReactModalPortal button')
                                        ).map(b => b.innerText.trim())
                                    """)
                                    log(f"  モーダル内ボタン: {modal_btns}")

                                    # 方法1: force=True でCropAreaインターセプトをバイパスしてクリック
                                    crop_confirm_texts = [
                                        "設定する", "選択する", "決定", "OK", "完了", "適用", "確認", "保存"
                                    ]
                                    for ct in crop_confirm_texts:
                                        try:
                                            btn = page.locator(f'.ReactModalPortal button:has-text("{ct}")').first
                                            if btn.count() > 0:
                                                log(f"  クロップ確認ボタンクリック (force=True): {ct}")
                                                btn.click(force=True)
                                                time.sleep(3)
                                                if page.locator('.reactEasyCrop_CropArea').count() == 0:
                                                    log("  クロップモーダル閉じた（force click）")
                                                    crop_closed = True
                                                    break
                                                else:
                                                    log(f"  クリック後もモーダル残存、次を試みる")
                                        except Exception as e:
                                            log(f"  ボタンクリック失敗 ({ct}): {e}")
                                            continue

                                    # 方法2: JS で最後のボタンをクリック
                                    if not crop_closed:
                                        log("  方法2: JS経由でモーダル最終ボタンをクリック...")
                                        try:
                                            page.evaluate("""
                                                () => {
                                                    const btns = Array.from(
                                                        document.querySelectorAll('.ReactModalPortal button')
                                                    );
                                                    if (btns.length > 0) btns[btns.length - 1].click();
                                                }
                                            """)
                                            time.sleep(3)
                                            if page.locator('.reactEasyCrop_CropArea').count() == 0:
                                                log("  クロップモーダル閉じた（JS click）")
                                                crop_closed = True
                                        except Exception as e:
                                            log(f"  JS クリック失敗: {e}")

                                    # 方法3: Escape で強制クローズ
                                    if not crop_closed:
                                        log("  方法3: Escapeでクロップモーダルを強制クローズ")
                                        page.keyboard.press('Escape')
                                        time.sleep(2)
                                        if page.locator('.reactEasyCrop_CropArea').count() == 0:
                                            log("  クロップモーダル閉じた（Escape）")
                                            crop_closed = True
                                        else:
                                            log("  警告: クロップモーダルが閉じられませんでした")
                                else:
                                    log("  クロップモーダルなし（スキップ）")
                                    crop_closed = True

                                uploaded_cover = True
                                log(f"  カバー画像アップロード成功: {cover_image.name}")
                                break
                        except Exception as e:
                            log(f"  アップロードメニュー失敗 ({up_sel}): {e}")
                            try:
                                page.keyboard.press('Escape')
                                time.sleep(0.5)
                            except Exception:
                                pass

                if not uploaded_cover:
                    log("  カバー画像: アップロードスキップ（セレクタ未対応）")
            else:
                log(f"  カバー画像ファイルなし: {cover_image}（スキップ）")
            time.sleep(0.5)

            # ── Step 3: 本文ペースト ──
            log("  本文をクリップボードに設定...")
            pasted = False

            # 本文エディタ候補（AIアシスタントパネルを除く。メインのProseMirrorを優先）
            body_sels = [
                '.o-noteEditBody .ProseMirror',
                '.o-noteEditArea__content .ProseMirror',
                '.ProseMirror[contenteditable="true"]',
                'div[contenteditable="true"]:not([data-placeholder*="タイトル"])',
                '.o-noteEditArea__content',
            ]

            def find_body_el():
                for sel in body_sels:
                    try:
                        el = page.locator(sel).first
                        if el.is_visible(timeout=3000):
                            return el, sel
                    except Exception:
                        continue
                return None, None

            def content_length(el):
                """ペースト後の文字数を確認（0なら失敗）"""
                try:
                    txt = el.inner_text(timeout=2000)
                    return len(txt.strip())
                except Exception:
                    return 0

            # 方法A: ブラウザ内 clipboard API → Ctrl+V
            # ※ headlessモードではWindowsクリップボードは使えないためブラウザAPIを使う
            log("  方法A: ブラウザclipboard API → Ctrl+V...")
            try:
                body_el, body_sel = find_body_el()
                if body_el is not None:
                    page.evaluate(
                        "async (t) => { await navigator.clipboard.writeText(t); }",
                        body
                    )
                    body_el.click()
                    time.sleep(0.5)
                    page.keyboard.press('Control+a')
                    time.sleep(0.2)
                    page.keyboard.press('Control+v')
                    time.sleep(2)
                    if content_length(body_el) > 10:
                        log(f"  方法A成功: {body_sel}")
                        pasted = True
                    else:
                        log(f"  方法A: ペースト後も0文字 → 次の方法へ")
            except Exception as e:
                log(f"  方法A失敗: {e}")

            # 方法B: Windows クリップボード + Ctrl+V（非headless環境向けフォールバック）
            if not pasted:
                log("  方法B: Windowsクリップボード → Ctrl+V...")
                if set_clipboard_windows(body):
                    body_el, body_sel = find_body_el()
                    if body_el is not None:
                        try:
                            body_el.click()
                            time.sleep(0.5)
                            page.keyboard.press('Control+a')
                            time.sleep(0.2)
                            page.keyboard.press('Control+v')
                            time.sleep(2)
                            if content_length(body_el) > 10:
                                log(f"  方法B成功: {body_sel}")
                                pasted = True
                            else:
                                log("  方法B: ペースト後も0文字 → 次の方法へ")
                        except Exception as e:
                            log(f"  方法B失敗: {e}")

            # 方法C: keyboard.insert_text（確実だが遅い）
            if not pasted:
                log("  方法C: keyboard.insert_text フォールバック...")
                body_el, body_sel = find_body_el()
                if body_el is not None:
                    try:
                        body_el.click()
                        time.sleep(0.3)
                        page.keyboard.press('Control+a')
                        page.keyboard.insert_text(body)
                        time.sleep(3)
                        if content_length(body_el) > 10:
                            log(f"  方法C成功: {body_sel}")
                            pasted = True
                        else:
                            log("  方法C: ペースト後も0文字")
                    except Exception as e:
                        log(f"  方法C失敗: {e}")

            if not pasted:
                raise Exception("本文の入力に失敗しました（全方法試行済み）")

            # ── Step 4: 「公開する」ボタン ──
            log("  「公開する」ボタンをクリック...")
            pub_btn_sels = [
                'button:has-text("公開する")',
                'button:has-text("公開")',
            ]
            pub_btn = None
            for sel in pub_btn_sels:
                try:
                    el = page.locator(sel).first
                    if el.is_visible(timeout=5000):
                        pub_btn = el
                        break
                except Exception:
                    continue
            if pub_btn is None:
                raise Exception("「公開する」ボタンが見つかりません")
            pub_btn.click()
            time.sleep(2)

            # ── Step 5: 有料設定 ──
            if price > 0:
                log(f"  価格設定: {price}円...")
                paid_sels = [
                    'label:has-text("有料")',
                    'input[value="paid"]',
                    '[data-value="paid"]',
                    'button:has-text("有料")',
                ]
                for sel in paid_sels:
                    try:
                        el = page.locator(sel).first
                        if el.is_visible(timeout=3000):
                            el.click()
                            time.sleep(0.5)
                            log(f"  有料選択: {sel}")
                            break
                    except Exception:
                        continue

                price_sels = [
                    'input[type="number"]',
                    'input[placeholder*="販売価格"]',
                    'input[placeholder*="価格"]',
                    'input[name*="price"]',
                ]
                for sel in price_sels:
                    try:
                        el = page.locator(sel).first
                        if el.is_visible(timeout=3000):
                            el.triple_click()
                            el.fill(str(price))
                            time.sleep(0.3)
                            log(f"  価格入力: {sel}")
                            break
                    except Exception:
                        continue

            # ── Step 6: タグ設定 ──
            log(f"  タグ設定: {tags}...")
            tag_sels = [
                'input[placeholder*="タグ"]',
                'input[name*="tag"]',
                '.p-tagInput input',
                'input[placeholder*="ハッシュタグ"]',
            ]
            for tag in tags[:5]:
                added = False
                for sel in tag_sels:
                    try:
                        el = page.locator(sel).first
                        if el.is_visible(timeout=2000):
                            el.fill(tag)
                            time.sleep(0.3)
                            page.keyboard.press('Enter')
                            time.sleep(0.5)
                            added = True
                            log(f"  タグ追加: {tag}")
                            break
                    except Exception:
                        continue
                if not added:
                    log(f"  (タグ '{tag}' 追加失敗 - スキップ)")
                    break

            # ── Step 7: 最終「投稿する」 ──
            log("  最終投稿ボタンをクリック...")

            final_btn = None

            # 有料記事の場合: 「有料エリア設定」をクリック → 「投稿する」が現れる（新UI対応）
            if price > 0:
                try:
                    yuryou_btn = page.locator('button:has-text("有料エリア設定")').first
                    if yuryou_btn.is_visible(timeout=3000):
                        log("  「有料エリア設定」をクリック（有料記事の新UIフロー）...")
                        yuryou_btn.click()
                        time.sleep(3)
                        log("  有料エリア設定後のボタンを検索...")
                except Exception as e:
                    log(f"  有料エリア設定ボタンなし: {e}")

            # 通常の「投稿する」ボタンを検索
            final_sels = [
                'button:has-text("投稿する")',
                'button:has-text("公開する")',
                'button:has-text("投稿")',
            ]
            for sel in final_sels:
                try:
                    els = page.locator(sel).all()
                    for el in reversed(els):
                        try:
                            if el.is_visible(timeout=2000):
                                final_btn = el
                                log(f"  最終ボタン発見: {sel}")
                                break
                        except Exception:
                            continue
                    if final_btn:
                        break
                except Exception:
                    continue

            # さらにボタンが見つからない場合: 全クリッカブル要素をスキャン
            if final_btn is None:
                log("  全ボタンをスキャン...")
                try:
                    btn_texts = page.evaluate(
                        "() => Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim())"
                    )
                    log(f"  ページ上のボタン: {btn_texts}")
                    for text in ['投稿する', '公開する', '投稿', '公開', 'Publish']:
                        if text in btn_texts:
                            el = page.locator(f'button:has-text("{text}")').last
                            if el.is_visible(timeout=2000):
                                final_btn = el
                                log(f"  最終ボタン(スキャン): {text}")
                                break
                except Exception as e:
                    log(f"  ボタンスキャン失敗: {e}")

            # button以外の要素（a, div[role=button]等）も検索
            if final_btn is None:
                log("  全クリッカブル要素をスキャン...")
                try:
                    clickables = page.evaluate("""
                        () => Array.from(document.querySelectorAll(
                            'button, a, [role="button"], input[type="submit"], [class*="publish"], [class*="submit"]'
                        )).filter(el => el.innerText && (
                            el.innerText.includes('投稿') || el.innerText.includes('公開')
                        )).map(el => ({
                            tag: el.tagName,
                            cls: el.className.substring(0, 60),
                            txt: el.innerText.trim().substring(0, 30)
                        }))
                    """)
                    log(f"  クリッカブル要素: {clickables}")
                    for item in clickables:
                        txt = item.get('txt', '')
                        tag = item.get('tag', '').lower()
                        cls = item.get('cls', '')
                        for sel_try in [
                            f'{tag}:has-text("{txt}")',
                            f'[class*="{cls[:20]}"]:has-text("{txt}")',
                            f':has-text("{txt}")',
                        ]:
                            try:
                                el = page.locator(sel_try).last
                                if el.is_visible(timeout=1000):
                                    final_btn = el
                                    log(f"  最終ボタン(拡張スキャン): {sel_try}")
                                    break
                            except Exception:
                                continue
                        if final_btn:
                            break
                except Exception as e:
                    log(f"  拡張スキャン失敗: {e}")

            # 最終手段A: 非表示含む全要素をDOMサーチ
            if final_btn is None:
                log("  DOM全要素サーチ（非表示含む）...")
                try:
                    hidden_els = page.evaluate("""
                        () => Array.from(document.querySelectorAll('*'))
                            .filter(el => el.innerText && (
                                el.innerText.includes('投稿') || el.innerText.includes('公開')
                            ) && el.tagName !== 'BODY' && el.tagName !== 'HTML')
                            .map(el => ({
                                tag: el.tagName,
                                id: el.id,
                                cls: el.className.toString().substring(0, 50),
                                txt: el.innerText.trim().substring(0, 20),
                                visible: el.offsetWidth > 0 && el.offsetHeight > 0
                            })).slice(0, 30)
                    """)
                    log(f"  投稿/公開テキスト要素: {hidden_els}")
                except Exception as e:
                    log(f"  DOMサーチ失敗: {e}")

            # 最終手段B: 「有料エリア設定」をクリックして最終公開フローを試みる
            if final_btn is None:
                log("  「有料エリア設定」経由で公開を試みる...")
                try:
                    yuryou_btn = page.locator('button:has-text("有料エリア設定")').first
                    if yuryou_btn.is_visible(timeout=3000):
                        yuryou_btn.click()
                        time.sleep(3)
                        page.screenshot(path=str(SCRIPT_DIR / 'debug_yuryou.png'))
                        # 有料エリア設定後のボタンを探す
                        for sel in [
                            'button:has-text("投稿する")',
                            'button:has-text("公開する")',
                            'button:has-text("設定して投稿")',
                            'button:has-text("確認して投稿")',
                            'button:has-text("投稿")',
                        ]:
                            try:
                                el = page.locator(sel).last
                                if el.is_visible(timeout=2000):
                                    final_btn = el
                                    log(f"  有料エリア設定後のボタン: {sel}")
                                    break
                            except Exception:
                                continue
                        if final_btn is None:
                            new_btns = page.evaluate(
                                "() => Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim())"
                            )
                            log(f"  有料エリア設定後のボタン一覧: {new_btns}")
                except Exception as e:
                    log(f"  有料エリア設定試行失敗: {e}")

            if final_btn is None:
                cur_url = page.url
                log(f"  現在URL: {cur_url}")
                page.screenshot(path=str(SCRIPT_DIR / 'debug_final_step.png'))
                raise Exception("最終投稿ボタンが見つかりません")

            final_btn.click()
            page.wait_for_load_state('networkidle', timeout=40000)
            time.sleep(3)

            final_url = page.url
            log(f"SUCCESS: {final_url}")
            print(f"SUCCESS: {final_url}")

            # auth state 保存（セッション更新）
            ctx.storage_state(path=str(AUTH_FILE))
            log("  auth_state.json 更新完了")

            # キューを進める（キューモード時のみ）
            if queue_data and queue_data.get('queue'):
                advance_queue(queue_data)
                remaining = len(queue_data.get('queue', [])) - 1
                if remaining > 0:
                    log(f"  残りキュー: {remaining}本")
                else:
                    log("  キュー完了（残り0本）")

        except Exception as e:
            tb = traceback.format_exc()
            log(f"FAILED: {e}")
            log(tb)
            try:
                ss = SCRIPT_DIR / 'error_screenshot.png'
                page.screenshot(path=str(ss))
                log(f"  スクリーンショット: {ss}")
            except Exception:
                pass
            try:
                ctx.storage_state(path=str(AUTH_FILE))
            except Exception:
                pass
            print(f"FAILED: {e}")
            sys.exit(3)
        finally:
            ctx.close()
            browser.close()

if __name__ == '__main__':
    main()
