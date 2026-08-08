# Hungary Youth Economic Pulse Dashboard

A Python-based automated report on what the Hungarian economy looks like for young people. Pulls public [Eurostat](https://ec.europa.eu/eurostat) data, cleans it with pandas, visualizes it with matplotlib, and outputs a self-contained HTML report — no ongoing costs, runs 100% locally and offline.

## Status

🚧 Work in progress — built day by day as a learning project.

## Charts

1. **Youth vs. total unemployment** (`une_rt_a`) — Hungary, ages 15-24 vs. 15-74, 2010-latest.
2. **House price index** (`prc_hpi_a`) — Hungary, 2015=100, 2010-latest.
3. **Housing cost overburden rate, ages 15-29** (`ilc_lvho07a`) — Hungary vs. EU-27 average.
4. *(Stretch goal)* Home ownership rate by age (`ilc_lvho02`).

## Tech stack

- Python 3
- [`eurostat`](https://pypi.org/project/eurostat/) — fetches data as pandas DataFrames
- pandas
- matplotlib

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Generates `report.html` with embedded PNG charts.

## Why this project

Built as a portfolio piece connecting an Applied Economics background (Corvinus University of Budapest) with applied data skills — real public data, real analysis, no black-box code.

## AI usage

Built using Claude Code as a pair programmer. Claude helped explain pandas/matplotlib concepts and provided guidance along the way, but every line was written and understood by me — I can walk through and explain any part of this codebase.
