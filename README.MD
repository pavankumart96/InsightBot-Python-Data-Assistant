# InsightBot 🤖📊 – Python Data Exploration Assistant

InsightBot is an interactive, terminal-based Python tool that helps data analysts quickly explore, clean, and understand datasets. It combines automated reporting, visualization, outlier detection, and even ML project suggestions into a single command-line assistant.

---

## 🚀 Features

- Load Excel/CSV datasets via user input
- Show summary statistics, data types, and missing values
- Generate and save histograms & heatmaps
- Detect outliers using IQR method
- Display value counts for categorical columns
- Recommend ML project types (classification or regression)
- Generate and export a summary report

---

## 🧰 Technologies Used

- Python
- pandas
- matplotlib
- seaborn
- io, os (file handling)

---

## 📁 How to Run

```bash
python insightbot.py

When prompted, enter the path to your .xlsx file.

All output files (charts and reports) will be saved in the outputs/ folder