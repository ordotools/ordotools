#!/usr/bin/env python3
"""
Performance benchmark tool for Ordotools.

This script runs a comprehensive benchmark of the LiturgicalCalendar 
generation process, comparing results with historical data to track
performance improvements or regressions over time.

Usage:
  python benchmark.py [--years YEARS] [--runs RUNS] [--dioceses DIOCESES]

Options:
  --years YEARS       Comma-separated list of years to test [default: 2025,2026,2027]
  --runs RUNS         Number of runs per test for averaging [default: 5]
  --dioceses DIOCESES Comma-separated list of dioceses to test [default: roman]
"""

import sys
import os
import time
import json
import argparse
from datetime import datetime
from statistics import mean, stdev
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table

from ordotools import LiturgicalCalendar

# Path to store performance history
PERFORMANCE_HISTORY_FILE = os.path.join(os.path.dirname(__file__), 'benchmark_history.json')

console = Console()

def load_performance_history():
    """Load performance history from JSON file."""
    if os.path.exists(PERFORMANCE_HISTORY_FILE):
        try:
            with open(PERFORMANCE_HISTORY_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"builds": [], "build_times": []}
    return {"builds": [], "build_times": []}

def save_performance_history(history):
    """Save performance history to JSON file."""
    with open(PERFORMANCE_HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def plot_performance_trend(history):
    """Plot the performance trend over time."""
    try:
        # Check if we have enough data points
        if len(history["builds"]) < 2:
            console.print("[yellow]Not enough data points to plot trend.[/yellow]")
            return
            
        # Extract data
        timestamps = [build["timestamp"] for build in history["builds"]]
        times = [build["average_time"] for build in history["builds"]]
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, times, 'b-o')
        plt.title('Calendar Generation Performance Over Time')
        plt.xlabel('Date')
        plt.ylabel('Average Build Time (seconds)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save the plot
        plot_file = os.path.join(os.path.dirname(__file__), 'performance_trend.png')
        plt.savefig(plot_file)
        
        console.print(f"[green]Performance trend plotted to {plot_file}[/green]")
    except ImportError:
        console.print("[yellow]Matplotlib not installed. Skipping trend plot.[/yellow]")
    except Exception as e:
        console.print(f"[red]Error plotting trend: {e}[/red]")

def run_benchmark(years, num_runs, dioceses):
    """Run the performance benchmark."""
    history = load_performance_history()
    
    # Get timestamp for this run
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a results table
    table = Table(title="Ordotools Performance Benchmark")
    table.add_column("Diocese")
    table.add_column("Year")
    table.add_column("Avg Time (s)", justify="right")
    table.add_column("Std Dev", justify="right")
    
    # Track overall results
    all_times = []
    diocese_results = {}
    
    # Run benchmarks
    for diocese in dioceses:
        diocese_times = []
        diocese_results[diocese] = {}
        
        for year in years:
            times = []
            
            with console.status(f"Benchmarking {diocese} calendar for {year}..."):
                for i in range(num_runs):
                    start_time = time.time()
                    cal = LiturgicalCalendar(year, diocese, "la")
                    calendar = cal.build()
                    end_time = time.time()
                    
                    elapsed = end_time - start_time
                    times.append(elapsed)
            
            # Calculate statistics
            avg_time = mean(times)
            std_dev = stdev(times) if len(times) > 1 else 0
            
            # Add to results
            diocese_times.append(avg_time)
            all_times.append(avg_time)
            diocese_results[diocese][str(year)] = avg_time
            
            # Add to table
            table.add_row(
                diocese, 
                str(year), 
                f"{avg_time:.4f}", 
                f"{std_dev:.4f}"
            )
    
    # Calculate overall average
    overall_avg = mean(all_times)
    
    # Add to history
    history["builds"].append({
        "timestamp": timestamp,
        "average_time": overall_avg,
        "details": diocese_results
    })
    
    # For tracking trend, also maintain a simple list of build times
    history["build_times"].append(overall_avg)
    
    # Save updated history
    save_performance_history(history)
    
    # Print results
    console.print(table)
    console.print(f"\nOverall average build time: [bold]{overall_avg:.4f}[/bold] seconds")
    
    # Assess performance trend
    if len(history["build_times"]) > 1:
        previous_avg = history["build_times"][-2]
        pct_change = ((overall_avg - previous_avg) / previous_avg) * 100
        
        # Compare with previous run
        if overall_avg < previous_avg:
            console.print(f"[green]✅ Performance improved by {abs(pct_change):.2f}% from last run[/green]")
        elif overall_avg > previous_avg:
            console.print(f"[yellow]⚠️ Performance degraded by {pct_change:.2f}% from last run[/yellow]")
        else:
            console.print("[blue]✓ Performance unchanged from last run[/blue]")
        
        # Compare with historical best
        best_time = min(history["build_times"])
        if overall_avg == best_time:
            console.print("[green]🏆 This is the fastest run on record![/green]")
        else:
            pct_from_best = ((overall_avg - best_time) / best_time) * 100
            console.print(f"[blue]📊 Current performance is {pct_from_best:.2f}% slower than the best recorded time[/blue]")
    else:
        console.print("[blue]📝 First performance measurement recorded as baseline[/blue]")
    
    # Show performance history
    if len(history["build_times"]) >= 3:
        console.print("\nRecent performance history:")
        
        history_table = Table("Date", "Avg Time (s)", "Change")
        for i in range(min(5, len(history["builds"]))):
            idx = len(history["builds"]) - i - 1
            build = history["builds"][idx]
            
            if i > 0:
                prev_build = history["builds"][idx+1]
                pct_change = ((build["average_time"] - prev_build["average_time"]) / prev_build["average_time"]) * 100
                change = f"{pct_change:+.2f}%"
            else:
                change = "-"
                
            history_table.add_row(
                build["timestamp"], 
                f"{build['average_time']:.4f}", 
                change
            )
            
        console.print(history_table)
    
    # Generate plot
    plot_performance_trend(history)
    
    return overall_avg

def main():
    parser = argparse.ArgumentParser(description="Ordotools performance benchmark")
    parser.add_argument("--years", default="2025,2026,2027", help="Comma-separated years to test")
    parser.add_argument("--runs", type=int, default=5, help="Number of runs per test")
    parser.add_argument("--dioceses", default="roman", help="Comma-separated dioceses to test")
    
    args = parser.parse_args()
    
    years = [int(year.strip()) for year in args.years.split(",")]
    dioceses = [diocese.strip() for diocese in args.dioceses.split(",")]
    
    console.print(f"[bold]Ordotools Performance Benchmark[/bold]")
    console.print(f"Testing years: {', '.join(map(str, years))}")
    console.print(f"Number of runs per test: {args.runs}")
    console.print(f"Testing dioceses: {', '.join(dioceses)}")
    console.print("")
    
    try:
        run_benchmark(years, args.runs, dioceses)
    except KeyboardInterrupt:
        console.print("\n[yellow]Benchmark interrupted![/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]Error during benchmark: {e}[/red]")
        raise

if __name__ == "__main__":
    main()