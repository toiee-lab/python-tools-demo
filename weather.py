#!/usr/bin/env python3
"""
Weather display script using OpenWeatherMap API
Beautiful weather information with rich library
"""

import argparse
import sys
import os
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

# Weather icons mapping
WEATHER_ICONS = {
    'clear sky': '☀️',
    'few clouds': '🌤️',
    'scattered clouds': '⛅',
    'broken clouds': '☁️',
    'overcast clouds': '☁️',
    'shower rain': '🌦️',
    'rain': '🌧️',
    'thunderstorm': '⛈️',
    'snow': '❄️',
    'mist': '🌫️',
    'fog': '🌫️',
    'haze': '🌫️',
    'smoke': '💨',
    'dust': '💨',
    'sand': '💨',
    'ash': '💨',
    'squall': '💨',
    'tornado': '🌪️'
}

def get_weather_icon(description):
    """Get weather icon based on description"""
    description = description.lower()
    for key, icon in WEATHER_ICONS.items():
        if key in description:
            return icon
    return '🌍'  # Default icon

def get_weather_data(city, api_key):
    """Fetch weather data from OpenWeatherMap API"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")
    except ValueError as e:
        raise Exception(f"Invalid JSON response: {e}")

def format_weather_display(weather_data):
    """Format weather data for beautiful display"""
    
    # Extract weather information
    main = weather_data['main']
    weather = weather_data['weather'][0]
    wind = weather_data.get('wind', {})
    city_name = weather_data['name']
    country = weather_data['sys']['country']
    
    # Get weather icon
    icon = get_weather_icon(weather['description'])
    
    # Create title with icon
    title = f"{icon} Weather in {city_name}, {country}"
    
    # Create weather table
    table = Table(show_header=False, box=box.ROUNDED, padding=(0, 1))
    table.add_column("Property", style="bold cyan", width=15)
    table.add_column("Value", style="bold white")
    
    # Temperature with color based on value
    temp = main['temp']
    if temp >= 30:
        temp_color = "red"
    elif temp >= 20:
        temp_color = "yellow"
    elif temp >= 10:
        temp_color = "green"
    else:
        temp_color = "blue"
    
    table.add_row("🌡️  Temperature", f"[{temp_color}]{temp:.1f}°C[/{temp_color}]")
    table.add_row("🌡️  Feels like", f"{main['feels_like']:.1f}°C")
    table.add_row("☁️  Condition", f"{weather['description'].title()}")
    table.add_row("💧 Humidity", f"{main['humidity']}%")
    
    # Wind information
    wind_speed = wind.get('speed', 0)
    wind_direction = wind.get('deg', None)
    wind_text = f"{wind_speed:.1f} m/s"
    if wind_direction is not None:
        directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                     'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        direction_idx = int((wind_direction + 11.25) / 22.5) % 16
        wind_text += f" ({directions[direction_idx]})"
    
    table.add_row("💨 Wind", wind_text)
    table.add_row("🔽 Pressure", f"{main['pressure']} hPa")
    
    # Add visibility if available
    if 'visibility' in weather_data:
        visibility = weather_data['visibility'] / 1000  # Convert to km
        table.add_row("👁️  Visibility", f"{visibility:.1f} km")
    
    # Create panel with the table
    panel = Panel(
        table,
        title=title,
        title_align="center",
        border_style="bright_blue",
        padding=(1, 2)
    )
    
    return panel

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Display beautiful weather information for a city",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python weather.py Tokyo
  python weather.py "New York"
  python weather.py Paris --api-key YOUR_API_KEY

Note: Set OPENWEATHER_API_KEY environment variable or use --api-key option
Get your free API key at: https://openweathermap.org/api
        """
    )
    
    parser.add_argument(
        'city',
        help='City name to get weather for'
    )
    
    parser.add_argument(
        '--api-key',
        help='OpenWeatherMap API key (or set OPENWEATHER_API_KEY env var)'
    )
    
    args = parser.parse_args()
    
    # Get API key from argument or environment variable
    api_key = args.api_key or os.getenv('OPENWEATHER_API_KEY')
    
    if not api_key:
        console.print(
            "[red]Error:[/red] OpenWeatherMap API key is required!\n"
            "Set OPENWEATHER_API_KEY environment variable or use --api-key option.\n"
            "Get your free API key at: https://openweathermap.org/api",
            style="bold"
        )
        sys.exit(1)
    
    try:
        # Show loading message
        with console.status(f"[bold green]Fetching weather data for {args.city}..."):
            weather_data = get_weather_data(args.city, api_key)
        
        # Display weather information
        weather_panel = format_weather_display(weather_data)
        console.print("\n")
        console.print(weather_panel)
        console.print("\n")
        
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}", style="bold")
        
        # Provide helpful suggestions based on error type
        error_str = str(e).lower()
        if "not found" in error_str or "404" in error_str:
            console.print(
                f"\n[yellow]Suggestion:[/yellow] Check the city name spelling. "
                f"Try including country code (e.g., 'Tokyo,JP' or 'London,UK')"
            )
        elif "unauthorized" in error_str or "401" in error_str:
            console.print(
                f"\n[yellow]Suggestion:[/yellow] Check your API key. "
                f"Make sure it's valid and activated."
            )
        elif "timeout" in error_str or "connection" in error_str:
            console.print(
                f"\n[yellow]Suggestion:[/yellow] Check your internet connection "
                f"and try again."
            )
        
        sys.exit(1)

if __name__ == "__main__":
    main()