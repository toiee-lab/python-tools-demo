#!/usr/bin/env python3
# /// script
# dependencies = [
#   "rich==13.7.1",
# ]
# ///
"""
🚀 Richライブラリを使った美しいプログレスバーのデモ
カラフルで美しいプログレスバーを表示します！
"""

import time
import random
from rich.console import Console
from rich.progress import (
    Progress, 
    SpinnerColumn, 
    TextColumn, 
    BarColumn, 
    TaskProgressColumn, 
    TimeElapsedColumn,
    MofNCompleteColumn
)
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

def show_welcome():
    """美しいウェルカムメッセージを表示"""
    welcome_text = Text()
    welcome_text.append("🎉 プログレスバー ", style="bold magenta")
    welcome_text.append("デモンストレーション", style="bold cyan")
    welcome_text.append(" へようこそ！ 🎉", style="bold magenta")
    
    panel = Panel(
        Align.center(welcome_text),
        border_style="bright_blue",
        padding=(1, 2)
    )
    
    console.print()
    console.print(panel)
    console.print()

def demo_simple_progress():
    """デモ1: シンプルで美しいプログレスバー"""
    console.print("[bold green]🔥 デモ1: クラシック・プログレスバー[/bold green]")
    console.print()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        
        task = progress.add_task("[cyan]素晴らしいデータを読み込み中...", total=100)
        
        for i in range(100):
            time.sleep(0.03)  # 3 seconds total
            progress.update(task, advance=1)
    
    console.print("[bold green]✨ 完了！美しいでしょう？[/bold green]")
    console.print()

def demo_multiple_progress():
    """デモ2: 複数のプログレスバー"""
    console.print("[bold yellow]🌟 デモ2: 複数プログレスバー[/bold yellow]")
    console.print()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TaskProgressColumn(),
        console=console
    ) as progress:
        
        # 異なる速度のタスク
        task1 = progress.add_task("[red]🔥 ファイルをダウンロード中...", total=50)
        task2 = progress.add_task("[green]🌱 データを処理中...", total=30)
        task3 = progress.add_task("[blue]🚀 結果をアップロード中...", total=20)
        
        tasks = [(task1, 50, 0.06), (task2, 30, 0.1), (task3, 20, 0.15)]
        
        while not progress.finished:
            for task_id, total, sleep_time in tasks:
                if not progress.tasks[task_id].finished:
                    progress.update(task_id, advance=1)
                    time.sleep(sleep_time)
    
    console.print("[bold yellow]🎊 すべてのタスクが完了！素晴らしい！[/bold yellow]")
    console.print()

def demo_fancy_progress():
    """デモ3: 超豪華なプログレスバー"""
    console.print("[bold magenta]💫 デモ3: 超豪華プログレスバー！[/bold magenta]")
    console.print()
    
    with Progress(
        SpinnerColumn("dots12"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=50),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        
        descriptions = [
            "[rainbow]🌈 魔法を作成中...",
            "[rainbow]✨ 星の粉を振りかけ中...",
            "[rainbow]🎨 虹を描画中...",
            "[rainbow]🦄 ユニコーンを召喚中...",
            "[rainbow]🎉 もうすぐ完了..."
        ]
        
        task = progress.add_task(descriptions[0], total=100)
        
        for i in range(100):
            # 20%ごとに説明を変更
            if i % 20 == 0 and i > 0:
                description_index = min(i // 20, len(descriptions) - 1)
                progress.update(task, description=descriptions[description_index])
            
            # ランダムな速度で興奮を演出
            time.sleep(random.uniform(0.02, 0.04))
            progress.update(task, advance=1)
    
    console.print("[bold rainbow]🎆 素晴らしい！魔法を目撃しましたね！ 🎆[/bold rainbow]")
    console.print()


def show_finale():
    """グランドフィナーレを表示"""
    finale_text = Text()
    finale_text.append("🎊 ", style="bold magenta")
    finale_text.append("おめでとうございます！", style="bold rainbow")
    finale_text.append(" 🎊", style="bold magenta")
    finale_text.append("\n\n")
    finale_text.append("あなたは以下の力を体験しました：", style="bold white")
    finale_text.append("\n")
    finale_text.append("• 美しいターミナル出力のためのRichライブラリ", style="cyan")
    finale_text.append("\n")
    finale_text.append("• Pythonの素晴らしい機能！", style="yellow")
    finale_text.append("\n\n")
    finale_text.append("コーディングを続けて、素晴らしいものを作り続けてください！ 🚀", style="bold blue")
    
    panel = Panel(
        Align.center(finale_text),
        title="🏆 ミッション完了！ 🏆",
        border_style="gold1",
        padding=(1, 2)
    )
    
    console.print()
    console.print(panel)
    console.print()

def main():
    """メインデモ関数"""
    # 画面クリア効果（ほとんどのターミナルで動作）
    console.clear()
    
    # ウェルカム
    show_welcome()
    time.sleep(1)
    
    # デモ1: シンプルプログレス
    demo_simple_progress()
    time.sleep(0.5)
    
    # デモ2: 複数プログレスバー
    demo_multiple_progress()
    time.sleep(0.5)
    
    # デモ3: 豪華プログレス
    demo_fancy_progress()
    time.sleep(0.5)
    
    # グランドフィナーレ
    show_finale()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]デモが中断されました！ご視聴ありがとうございました！ 👋[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]エラーが発生しました: {e}[/bold red]")
        console.print("[bold yellow]でも、それも学習の一部です！コーディングを続けましょう！ 💪[/bold yellow]")