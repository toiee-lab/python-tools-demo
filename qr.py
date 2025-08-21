#!/usr/bin/env python3
"""
🎯 QRコード生成スクリプト
テキストからQRコードを生成し、画像ファイルとして保存します
"""

import argparse
import sys
import os
from pathlib import Path
import qrcode
try:
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
    from qrcode.image.styles.colorfills import SolidFillColorMask
    STYLED_FEATURES = True
except ImportError:
    STYLED_FEATURES = False
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

def create_qr_code(data, output_path, box_size=10, border=4, error_correction='M', style='square', 
                   fill_color='black', back_color='white'):
    """QRコードを生成"""
    
    # エラー訂正レベルの設定
    error_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,  # 約7%
        'M': qrcode.constants.ERROR_CORRECT_M,  # 約15%（デフォルト）
        'Q': qrcode.constants.ERROR_CORRECT_Q,  # 約25%
        'H': qrcode.constants.ERROR_CORRECT_H   # 約30%
    }
    
    # QRCodeオブジェクトを作成
    qr = qrcode.QRCode(
        version=1,  # 自動サイズ調整
        error_correction=error_levels[error_correction],
        box_size=box_size,
        border=border,
    )
    
    # データを追加
    qr.add_data(data)
    qr.make(fit=True)
    
    # スタイルに応じて画像を生成
    if STYLED_FEATURES and style == 'round':
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            color_mask=SolidFillColorMask(front_color=fill_color, back_color=back_color)
        )
    elif STYLED_FEATURES and style == 'circle':
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=CircleModuleDrawer(),
            color_mask=SolidFillColorMask(front_color=fill_color, back_color=back_color)
        )
    else:  # square (default) or fallback
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # ファイル保存
    img.save(output_path)
    return img

def display_qr_info(data, output_path, qr_size, style, error_correction):
    """生成されたQRコードの情報を表示"""
    
    # 情報テーブルの作成
    table = Table(title="📊 生成されたQRコード情報", box=box.ROUNDED)
    table.add_column("項目", style="bold cyan", width=20)
    table.add_column("内容", style="bold white")
    
    table.add_row("📝 入力テキスト", data[:50] + "..." if len(data) > 50 else data)
    table.add_row("💾 出力ファイル", str(output_path))
    table.add_row("📏 画像サイズ", f"{qr_size[0]} x {qr_size[1]} px")
    table.add_row("🎨 スタイル", style.capitalize())
    table.add_row("🛡️ エラー訂正", f"レベル {error_correction}")
    
    # ファイル情報
    if output_path.exists():
        file_size = output_path.stat().st_size
        if file_size < 1024:
            size_str = f"{file_size} B"
        elif file_size < 1024 * 1024:
            size_str = f"{file_size / 1024:.1f} KB"
        else:
            size_str = f"{file_size / (1024 * 1024):.1f} MB"
        table.add_row("📁 ファイルサイズ", size_str)
    
    console.print()
    console.print(table)
    console.print()

def show_help_info():
    """使用方法の詳細を表示"""
    help_text = Text()
    help_text.append("🎯 QRコード生成スクリプト\n\n", style="bold cyan")
    help_text.append("基本的な使用方法:\n", style="bold yellow")
    help_text.append("  python qr.py \"テキスト\" output.png\n\n", style="green")
    help_text.append("オプション:\n", style="bold yellow")
    help_text.append("  --size SIZE        ボックスサイズ (デフォルト: 10)\n", style="white")
    help_text.append("  --border BORDER    ボーダーサイズ (デフォルト: 4)\n", style="white")
    help_text.append("  --error-level L/M/Q/H  エラー訂正レベル (デフォルト: M)\n", style="white")
    help_text.append("  --style square/round/circle  スタイル (デフォルト: square)\n", style="white")
    help_text.append("  --fill-color COLOR  前景色 (デフォルト: black)\n", style="white")
    help_text.append("  --back-color COLOR  背景色 (デフォルト: white)\n\n", style="white")
    help_text.append("使用例:\n", style="bold yellow")
    help_text.append("  python qr.py \"https://example.com\" qr.png\n", style="green")
    help_text.append("  python qr.py \"Hello World\" hello.png --style round\n", style="green")
    help_text.append("  python qr.py \"重要な情報\" important.png --error-level H --size 15\n", style="green")
    
    panel = Panel(help_text, title="📖 ヘルプ", border_style="blue")
    console.print()
    console.print(panel)
    console.print()

def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description="🎯 QRコード生成スクリプト",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  python qr.py "Hello World" output.png
  python qr.py "https://example.com" qr.png --style round
  python qr.py "重要な情報" important.png --error-level H --size 15
        """
    )
    
    parser.add_argument(
        'text',
        help='QRコードに埋め込むテキスト'
    )
    
    parser.add_argument(
        'output',
        help='出力ファイル名（.png, .jpg, .jpeg対応）'
    )
    
    parser.add_argument(
        '--size',
        type=int,
        default=10,
        help='ボックスサイズ（デフォルト: 10）'
    )
    
    parser.add_argument(
        '--border',
        type=int,
        default=4,
        help='ボーダーサイズ（デフォルト: 4）'
    )
    
    parser.add_argument(
        '--error-level',
        choices=['L', 'M', 'Q', 'H'],
        default='M',
        help='エラー訂正レベル L(~7%%) M(~15%%) Q(~25%%) H(~30%%) (デフォルト: M)'
    )
    
    style_choices = ['square']
    if STYLED_FEATURES:
        style_choices.extend(['round', 'circle'])
    
    parser.add_argument(
        '--style',
        choices=style_choices,
        default='square',
        help='QRコードのスタイル (デフォルト: square)'
    )
    
    parser.add_argument(
        '--fill-color',
        default='black',
        help='前景色 (デフォルト: black)'
    )
    
    parser.add_argument(
        '--back-color',
        default='white',
        help='背景色 (デフォルト: white)'
    )
    
    parser.add_argument(
        '--help-detail',
        action='store_true',
        help='詳細なヘルプを表示'
    )
    
    # 引数が不足している場合の処理
    if len(sys.argv) == 1:
        show_help_info()
        return
    
    args = parser.parse_args()
    
    if args.help_detail:
        show_help_info()
        return
    
    try:
        output_path = Path(args.output)
        
        # 出力ディレクトリを作成
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # ローディング表示
        with console.status("[bold green]QRコードを生成中..."):
            img = create_qr_code(
                args.text,
                output_path,
                box_size=args.size,
                border=args.border,
                error_correction=args.error_level,
                style=args.style,
                fill_color=args.fill_color,
                back_color=args.back_color
            )
        
        # 成功メッセージ
        success_panel = Panel(
            f"[bold green]✅ QRコードが正常に生成されました！[/bold green]\n"
            f"📁 ファイル: {output_path}",
            title="🎉 完了",
            border_style="green"
        )
        console.print()
        console.print(success_panel)
        
        # 詳細情報を表示
        display_qr_info(args.text, output_path, img.size, args.style, args.error_level)
        
        # 次のステップの提案
        console.print("[bold cyan]💡 ヒント:[/bold cyan]")
        console.print("  • QRコードをスマートフォンのカメラで読み取ってテストしてください")
        console.print("  • より高いエラー訂正レベル（--error-level H）を使用すると、汚れや破損に強くなります")
        console.print("  • --style round や --style circle でデザインを変更できます")
        console.print()
        
    except Exception as e:
        error_panel = Panel(
            f"[bold red]❌ エラーが発生しました:[/bold red]\n{e}\n\n"
            f"[yellow]💡 解決方法:[/yellow]\n"
            f"• ファイル名に有効な拡張子（.png, .jpg, .jpeg）を使用してください\n"
            f"• 出力先ディレクトリに書き込み権限があることを確認してください\n"
            f"• テキストが長すぎる場合は、短縮するかエラー訂正レベルを下げてください",
            title="🚨 エラー",
            border_style="red"
        )
        console.print()
        console.print(error_panel)
        console.print()
        sys.exit(1)

if __name__ == "__main__":
    main()