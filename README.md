# Stock Analysis CLI Tool

A simple Python-based Command-Line Interface (CLI) tool to analyze and visualize stock or numeric data from CSV files.  
Built for learning, experimentation, and as a foundation for more advanced data analysis projects.

---

## Features

- Read CSV files and extract numeric columns safely
- Compute key statistics:
  - Mean, Median, Mode
  - Variance, Standard Deviation
  - Range, Skewness, Kurtosis
- Visualize data with:
  - Histograms
  - Boxplots
  - Scatter plots
  - Line plots
  - Correlation heatmaps
- Fully modular:
  - `file_handler.py` → CSV reading and validation
  - `analytics.py` → Statistical calculations
  - `visualization.py` → Graphing
  - `main.py` → CLI interface

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Stock-analysis.git
   cd Stock-analysis


   Stock-analysis/
│
├─ main.py             # CLI interface
├─ file_handler.py     # CSV reading + validation
├─ analytics.py        # Statistical calculations
├─ visualization.py    # Data visualization functions
├─ data/               # Example CSV files
└─ README.md

