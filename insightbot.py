import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io  # Needed for capturing df.info()

# Setup: Create output directory
if not os.path.exists("outputs"):
    os.makedirs("outputs")

print("👋 Welcome to InsightBot - Your Data Assistant\n")

# Ask for file path
file_path = input("📁 Enter the full path to your Excel file (.xlsx): ")

# Check if file exists
if not os.path.exists(file_path):
    print("❌ File not found. Please check the path and try again.")
    exit()

# Load Excel file
try:
    df = pd.read_excel(file_path)
    print("\n✅ Dataset Loaded Successfully!\n")
except Exception as e:
    print(f"❌ Error loading file: {e}")
    exit()

# Show basic preview
print("📊 Dataset Preview:")
print(df.head())

print("\n🔍 Dataset Info:")
df.info()

print("\n🧹 Missing Values Summary:")
print(df.isnull().sum())

# Main menu
while True:
    print("\nWhat would you like to do next?")
    print("1️⃣  Show summary statistics")
    print("2️⃣  Show column data types")
    print("3️⃣  Generate histograms for numeric columns")
    print("4️⃣  Show correlation heatmap")
    print("5️⃣  Detect outliers (IQR method)")
    print("6️⃣  Show value counts for categorical columns")
    print("7️⃣  ML-type suggestion (Classification vs Regression)")
    print("8️⃣  Generate summary report (TXT file)")
    print("9️⃣  Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        print("\n📈 Summary Statistics:")
        print(df.describe())

    elif choice == '2':
        print("\n📦 Column Data Types:")
        print(df.dtypes)

    elif choice == '3':
        print("\n📊 Generating and saving histograms...")
        numeric_cols = df.select_dtypes(include='number')
        ax = numeric_cols.hist(figsize=(12, 8), bins=20)
        plt.tight_layout()
        plt.savefig("outputs/histograms.png")
        plt.show()
        print("✅ Histograms saved to outputs/histograms.png")

    elif choice == '4':
        print("\n🔗 Generating and saving correlation heatmap...")
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig("outputs/correlation_heatmap.png")
        plt.show()
        print("✅ Correlation heatmap saved to outputs/correlation_heatmap.png")

    elif choice == '5':
        print("\n🧪 Detecting outliers using IQR method...\n")
        numeric_cols = df.select_dtypes(include='number')
        for col in numeric_cols.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            outliers = df[(df[col] < lower) | (df[col] > upper)]
            print(f"🔍 {col}: {len(outliers)} outlier(s)")

    elif choice == '6':
        print("\n📊 Value Counts for Categorical Columns:\n")
        cat_cols = df.select_dtypes(include='object')
        for col in cat_cols.columns:
            print(f"\n🔸 {col}:\n{df[col].value_counts()}")

    elif choice == '7':
        print("\n🤖 Analyzing dataset for ML project type...\n")
        for col in df.columns:
            unique_vals = df[col].nunique()
            dtype = df[col].dtype

            if unique_vals < 2:
                continue

            if dtype == 'object':
                if 2 <= unique_vals <= 10:
                    print(f"📌 Column '{col}' could be a target for a **classification** problem ({unique_vals} categories).")
            elif pd.api.types.is_numeric_dtype(df[col]):
                if 2 <= unique_vals <= 10:
                    print(f"📌 Column '{col}' (numeric) may be categorical → classification.")
                elif unique_vals > 10:
                    print(f"📌 Column '{col}' looks continuous → **regression** target.")

    elif choice == '8':
        report_path = "outputs/summary_report.txt"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("InsightBot Summary Report\n")
            f.write("=" * 40 + "\n\n")

            # Dataset Info
            f.write("Dataset Info:\n")
            buffer = io.StringIO()
            df.info(buf=buffer)
            f.write(buffer.getvalue() + "\n")

            # Missing Values
            f.write("Missing Values:\n")
            f.write(str(df.isnull().sum()) + "\n\n")

            # Data Types
            f.write("Column Data Types:\n")
            f.write(str(df.dtypes) + "\n\n")

            # Summary Stats
            f.write("Summary Statistics:\n")
            f.write(str(df.describe()) + "\n\n")

            # ML Target Suggestions
            f.write("Potential ML Targets:\n")
            for col in df.columns:
                unique_vals = df[col].nunique()
                dtype = df[col].dtype

                if unique_vals < 2:
                    continue

                if dtype == 'object':
                    if 2 <= unique_vals <= 10:
                        f.write(f"- Column '{col}' → Classification target ({unique_vals} categories)\n")
                elif pd.api.types.is_numeric_dtype(df[col]):
                    if 2 <= unique_vals <= 10:
                        f.write(f"- Column '{col}' (numeric) may be categorical → Classification\n")
                    elif unique_vals > 10:
                        f.write(f"- Column '{col}' looks continuous → Regression target\n")

        print(f"\n📄 Summary report saved to {report_path}")

    elif choice == '9':
        print("\n👋 Exiting InsightBot. See you next time!")
        break

    else:
        print("❌ Invalid choice. Please enter a number between 1 and 9.")
