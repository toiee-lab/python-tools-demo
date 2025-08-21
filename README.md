# 🐍 Python Tools Demo Collection

美しく実用的なPythonツール集へようこそ！このコレクションは、日常的に使える便利なPythonスクリプトを集めたデモプロジェクトです。

## ✨ 特徴

- 🎨 **Rich**ライブラリによる美しい出力
- 🌐 **クロスプラットフォーム**対応（Windows/macOS/Linux）
- 📱 **実用的**で楽しいツール
- 🔧 **簡単**なセットアップと実行
- 🎯 **初学者**にも優しい設計

## 🛠️ セットアップ

### 1. リポジトリをクローン

```bash
git clone <repository-url>
cd python-tools-demo
```

### 2. 仮想環境の作成と有効化

```bash
# 仮想環境作成
python -m venv venv

# 有効化（macOS/Linux）
source venv/bin/activate

# 有効化（Windows）
venv\\Scripts\\activate
```

### 3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

## 🎪 利用可能なツール

### 📰 [news.py] - RSSニュースアグリゲーター

3つの主要ニュースソースから最新情報を美しく表示します。

**実行方法：**
```bash
python news.py
```

**特徴：**
- Yahoo!ニュース、ITメディア、Yahoo!経済から取得
- 記事の公開時刻付き表示
- カラフルで見やすいテーブル形式
- 取得結果のサマリー表示

---

### 🌈 [progress.py] - 美しいプログレスバーデモ

Richライブラリの力を体感できる視覚的に美しいデモです。

**実行方法：**
```bash
python progress.py
```

**含まれるデモ：**
1. **クラシック・プログレスバー** - シンプルで美しい基本形
2. **複数プログレスバー** - 並行処理の可視化
3. **超豪華プログレスバー** - レインボーカラーで魔法のような演出

---

### 🌤️ [weather.py] - 天気情報表示ツール

OpenWeatherMap APIを使用して都市の天気を美しく表示します。

**セットアップ：**
1. [OpenWeatherMap](https://openweathermap.org/api)で無料のAPIキーを取得
2. 環境変数を設定：
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

**実行方法：**
```bash
# 環境変数を使用
python weather.py Tokyo

# 直接APIキーを指定
python weather.py Paris --api-key your_api_key_here

# カスタマイズオプション
python weather.py "New York" --help
```

**特徴：**
- 天気アイコン（絵文字）付き表示
- 気温、湿度、風速、気圧などの詳細情報
- 温度に応じた色分け表示
- 包括的なエラーハンドリング

---

### 📱 [qr.py] - QRコード生成ツール

テキストやURLからQRコードを生成し、画像ファイルとして保存します。

**実行方法：**
```bash
# 基本的な使用方法
python qr.py "Hello World" output.png

# URL用QRコード
python qr.py "https://github.com" github.png

# 日本語テキスト
python qr.py "こんにちは世界！" hello.png

# カスタマイズオプション
python qr.py "重要な情報" custom.png --size 15 --error-level H
```

**オプション：**
- `--size` : ボックスサイズ（デフォルト: 10）
- `--border` : ボーダーサイズ（デフォルト: 4）
- `--error-level` : エラー訂正レベル（L/M/Q/H）
- `--style` : スタイル（square）
- `--fill-color` : 前景色
- `--back-color` : 背景色

## 📦 依存関係

プロジェクトで使用している主要なライブラリ：

```
rich==13.7.1          # 美しいターミナル出力
requests==2.31.0      # HTTP通信
qrcode[pil]==7.4.2    # QRコード生成
beautifulsoup4==4.12.3 # HTML解析
feedparser==6.0.11    # RSSフィード解析
```

## 🎯 使用例とスクリーンショット

### ニュースアグリゲーターの出力例

```
╭──────────────────────── 🌟 ニュースダッシュボード 🌟 ────────────────────────╮
│                                                                              │
│  📰 ニュースアグリゲーター 📰                                                │
│                                                                              │
│  最新のニュースを複数のソースから取得しています                              │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

              📰 Yahoo!ニュース (8件)               
╭────────────┬─────────────────────────────────────╮
│ 時刻       │ 記事タイトル                        │
├────────────┼─────────────────────────────────────┤
│ 08/21 06:… │  1. 最新ニュースのタイトル          │
│ 08/21 03:… │  2. 重要なニュース情報              │
```

### プログレスバーの表示例

```
🔥 デモ1: クラシック・プログレスバー

  素晴らしいデータを読み込み中... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:03
✨ 完了！美しいでしょう？
```

### 天気情報の表示例

```
╭─────────────── 🌤️ Weather in Tokyo, JP ───────────────╮
│ 🌡️  Temperature    25.3°C                              │
│ 🌡️  Feels like     27.1°C                              │
│ ☁️  Condition      Clear Sky                            │
│ 💧 Humidity       65%                                  │
│ 💨 Wind           3.2 m/s (SW)                         │
│ 🔽 Pressure       1013 hPa                             │
╰────────────────────────────────────────────────────────╯
```

## 🔧 トラブルシューティング

### よくある問題と解決方法

#### 1. モジュールが見つからないエラー

```bash
ModuleNotFoundError: No module named 'rich'
```

**解決方法：**
```bash
# 仮想環境が有効になっていることを確認
source venv/bin/activate  # macOS/Linux
# または
venv\\Scripts\\activate   # Windows

# 依存関係を再インストール
pip install -r requirements.txt
```

#### 2. 天気APIのエラー

```bash
Error: API request failed: 401 Client Error: Unauthorized
```

**解決方法：**
- APIキーが正しく設定されていることを確認
- 新しいAPIキーの場合、アクティベーションに数時間かかる場合があります
- ブラウザで直接APIをテスト：
```
http://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid=YOUR_API_KEY
```

#### 3. QRコード生成エラー

```bash
PIL/Pillow related errors
```

**解決方法：**
```bash
pip install --upgrade Pillow
```

#### 4. ニュース取得エラー

**症状：** RSSフィードが取得できない

**解決方法：**
- インターネット接続を確認
- ファイアウォールの設定を確認
- 数分後に再試行

## 🎨 カスタマイズ

### テーマの変更

各スクリプトはRichライブラリを使用しているため、色やスタイルを簡単にカスタマイズできます。

### 新しいニュースソースの追加

`news.py`で新しいRSSフィードを追加：

```python
self.rss_feeds = {
    'Yahoo!ニュース': 'https://news.yahoo.co.jp/rss/topics/top-picks.xml',
    'ITメディア': 'https://rss.itmedia.co.jp/rss/2.0/topstory.xml',
    'Yahoo!経済': 'https://news.yahoo.co.jp/rss/topics/business.xml',
    # 新しいソースを追加
    'あなたのソース': 'https://example.com/rss.xml'
}
```

## 🤝 コントリビューション

このプロジェクトへの貢献を歓迎します！

1. このリポジトリをフォーク
2. 新しい機能ブランチを作成（`git checkout -b feature/amazing-feature`）
3. 変更をコミット（`git commit -m 'Add some amazing feature'`）
4. ブランチにプッシュ（`git push origin feature/amazing-feature`）
5. プルリクエストを開く

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 🙏 謝辞

- [Rich](https://github.com/Textualize/rich) - 美しいターミナル出力を提供
- [OpenWeatherMap](https://openweathermap.org/) - 天気データAPI
- [QRCode](https://github.com/lincolnloop/python-qrcode) - QRコード生成
- [FeedParser](https://feedparser.readthedocs.io/) - RSSフィード解析

## 🚀 次のステップ

このプロジェクトを楽しんでいただけましたか？ぜひ以下も試してみてください：

- 新しいツールの追加
- 既存ツールの機能拡張
- 他のAPIとの連携
- GUIアプリケーションへの発展

---

**Happy Coding! 🎉**

何か質問や提案がありましたら、お気軽にIssueを作成してください！