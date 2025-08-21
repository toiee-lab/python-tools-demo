#!/usr/bin/env python3
"""
📰 RSSニュース取得・表示スクリプト
Yahoo!ニュース、ITメディア、Yahoo!経済のRSSフィードから最新ニュースを美しく表示
"""

import feedparser
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import track
from rich import box
from dataclasses import dataclass
from typing import List, Optional

console = Console()

@dataclass
class NewsItem:
    title: str
    url: str
    source: str
    published: Optional[str] = None
    summary: Optional[str] = None

class NewsAggregator:
    def __init__(self):
        self.rss_feeds = {
            'Yahoo!ニュース': 'https://news.yahoo.co.jp/rss/topics/top-picks.xml',
            'ITメディア': 'https://rss.itmedia.co.jp/rss/2.0/topstory.xml',
            'Yahoo!経済': 'https://news.yahoo.co.jp/rss/topics/business.xml'
        }

    def get_rss_feed(self, source_name: str, rss_url: str) -> List[NewsItem]:
        """RSSフィードから記事を取得"""
        news_items = []
        try:
            feed = feedparser.parse(rss_url)
            
            if feed.bozo:
                console.print(f"[yellow]警告: {source_name}のRSSフィードに問題があります[/yellow]")
            
            for entry in feed.entries[:15]:  # 最大15件
                # タイトルを取得
                title = entry.get('title', '').strip()
                if not title:
                    continue
                
                # URLを取得
                url = entry.get('link', '')
                
                # 公開日を取得
                published = ''
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    try:
                        pub_time = datetime(*entry.published_parsed[:6])
                        published = pub_time.strftime('%m/%d %H:%M')
                    except:
                        pass
                
                # サマリーを取得
                summary = entry.get('summary', '')
                if summary:
                    # HTMLタグを除去
                    import re
                    summary = re.sub(r'<[^>]+>', '', summary)
                    summary = summary.strip()[:100] + '...' if len(summary) > 100 else summary
                
                news_items.append(NewsItem(
                    title=title,
                    url=url,
                    source=source_name,
                    published=published,
                    summary=summary
                ))
            
        except Exception as e:
            console.print(f"[red]{source_name}のRSSフィード取得に失敗: {e}[/red]")
        
        return news_items



    def get_all_news(self) -> List[NewsItem]:
        """すべてのRSSフィードから記事を取得"""
        all_news = []
        
        # プログレスバー付きで各RSSフィードから取得
        feeds = list(self.rss_feeds.items())
        
        for source_name, rss_url in track(feeds, description="RSSフィードを取得中..."):
            news = self.get_rss_feed(source_name, rss_url)
            all_news.extend(news)
            time.sleep(0.5)  # 各フィードへのアクセス間隔を空ける
        
        return all_news

def display_welcome():
    """ウェルカムメッセージを表示"""
    welcome_text = Text()
    welcome_text.append("📰 ", style="bold blue")
    welcome_text.append("ニュース", style="bold cyan")
    welcome_text.append("アグリゲーター", style="bold blue")
    welcome_text.append(" 📰", style="bold blue")
    welcome_text.append("\n\n")
    welcome_text.append("最新のニュースを複数のソースから取得しています", style="white")
    
    panel = Panel(
        welcome_text,
        title="🌟 ニュースダッシュボード 🌟",
        border_style="bright_blue",
        padding=(1, 2)
    )
    
    console.print()
    console.print(panel)
    console.print()

def display_news_by_source(news_items: List[NewsItem]):
    """ソース別にニュースを美しく表示"""
    
    # ソース別にグループ化
    sources = {}
    for item in news_items:
        if item.source not in sources:
            sources[item.source] = []
        sources[item.source].append(item)
    
    # 各ソースのニュースを表示
    for source_name, items in sources.items():
        if not items:
            continue
            
        # ソース名に応じて色とアイコンを設定
        if "Yahoo!" in source_name:
            if "経済" in source_name:
                color = "yellow"
                icon = "💼"
            else:
                color = "red"
                icon = "📰"
        elif "ITMedia" in source_name:
            color = "green"
            icon = "💻"
        else:
            color = "blue"
            icon = "📄"
        
        # テーブル作成
        table = Table(
            title=f"{icon} {source_name} ({len(items)}件)",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold white",
            title_style=f"bold {color}"
        )
        
        table.add_column("時刻", style="dim cyan", width=10, no_wrap=True)
        table.add_column("記事タイトル", style="white", no_wrap=False)
        
        # 記事を追加
        for i, item in enumerate(items, 1):
            # タイトルを適度な長さに制限
            title = item.title
            if len(title) > 70:
                title = title[:67] + "..."
            
            # 公開時刻
            time_str = item.published if item.published else ""
            
            table.add_row(time_str, f"{i:2d}. {title}")
        
        console.print()
        console.print(table)

def display_summary(news_items: List[NewsItem]):
    """取得結果のサマリーを表示"""
    
    # ソース別の件数をカウント
    source_counts = {}
    for item in news_items:
        source_counts[item.source] = source_counts.get(item.source, 0) + 1
    
    # サマリーテーブル
    summary_table = Table(
        title="📊 取得結果サマリー",
        box=box.DOUBLE_EDGE,
        show_header=True,
        header_style="bold cyan"
    )
    
    summary_table.add_column("ニュースソース", style="bold yellow", width=20)
    summary_table.add_column("記事数", style="bold green", justify="center", width=10)
    
    total = 0
    for source, count in source_counts.items():
        summary_table.add_row(source, str(count))
        total += count
    
    summary_table.add_row("", "")  # 区切り行
    summary_table.add_row("合計", str(total), style="bold white")
    
    console.print()
    console.print(summary_table)

def display_footer():
    """フッターメッセージを表示"""
    current_time = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    
    footer_text = Text()
    footer_text.append("🕐 最終更新: ", style="dim")
    footer_text.append(current_time, style="bold white")
    footer_text.append("\n")
    footer_text.append("💡 ニュースは各サイトから自動取得されています", style="dim")
    footer_text.append("\n")
    footer_text.append("🔗 詳細は各記事のリンクをご確認ください", style="dim")
    
    panel = Panel(
        footer_text,
        title="ℹ️ 情報",
        border_style="dim",
        padding=(1, 2)
    )
    
    console.print()
    console.print(panel)
    console.print()

def main():
    """メイン処理"""
    try:
        # 画面クリア
        console.clear()
        
        # ウェルカムメッセージ
        display_welcome()
        
        # ニュース取得
        aggregator = NewsAggregator()
        news_items = aggregator.get_all_news()
        
        if not news_items:
            console.print("[bold red]❌ ニュースを取得できませんでした。[/bold red]")
            console.print("[yellow]💡 インターネット接続を確認してください。[/yellow]")
            return
        
        # ニュース表示
        display_news_by_source(news_items)
        
        # サマリー表示
        display_summary(news_items)
        
        # フッター表示
        display_footer()
        
        # 完了メッセージ
        console.print("[bold green]✨ ニュースの取得と表示が完了しました！[/bold green]")
        
    except KeyboardInterrupt:
        console.print("\n[bold yellow]⚠️ 処理が中断されました。[/bold yellow]")
    except Exception as e:
        console.print(f"\n[bold red]❌ エラーが発生しました: {e}[/bold red]")
        console.print("[yellow]💡 しばらく時間を置いてから再試行してください。[/yellow]")

if __name__ == "__main__":
    main()