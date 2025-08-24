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
git clone https://github.com/toiee-lab/python-tools-demo.git
cd python-tools-demo
```

### 2. uv のインストール

macOSの場合は、ターミナルで以下を実行。

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

あるいは、

```
wget -qO- https://astral.sh/uv/install.sh | sh
```

Windowsの場合は、管理者権限で、PowerShellを起動し、以下を実行。

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


## 🎪 デモの試し方

### 📰 [news.py] - RSSニュースアグリゲーター

3つの主要ニュースソースから最新情報を美しく表示します。

**実行方法：**
```bash
uv run news.py
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
uv run progress.py
```

**含まれるデモ：**
1. **クラシック・プログレスバー** - シンプルで美しい基本形
2. **複数プログレスバー** - 並行処理の可視化
3. **超豪華プログレスバー** - レインボーカラーで魔法のような演出

---

### 🌤️ [weather.py] - 天気情報表示ツール

OpenWeatherMap APIを使用して都市の天気を美しく表示します。

**セットアップ：**
1. [OpenWeatherMap](https://openweathermap.org/api)で無料のAPIキーを取得（無料登録して、取得する。1時間ほど待つ必要あり）
2. 環境変数を設定：
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

**実行方法：**
```bash
# 環境変数を使用
uv run weather.py Tokyo

# 直接APIキーを指定
uv run weather.py Paris --api-key your_api_key_here

# カスタマイズオプション
uv run weather.py "New York" --help
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
uv run qr.py "Hello World" output.png

# URL用QRコード
uv run qr.py "https://github.com" github.png

# 日本語テキスト
uv run qr.py "こんにちは世界！" hello.png

# カスタマイズオプション
uv run qr.py "重要な情報" custom.png --size 15 --error-level H
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

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 🙏 謝辞

- [Rich](https://github.com/Textualize/rich) - 美しいターミナル出力を提供
- [OpenWeatherMap](https://openweathermap.org/) - 天気データAPI
- [QRCode](https://github.com/lincolnloop/python-qrcode) - QRコード生成
- [FeedParser](https://feedparser.readthedocs.io/) - RSSフィード解析
