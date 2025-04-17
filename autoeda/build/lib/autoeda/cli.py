import argparse
import pandas as pd
from autoeda.analyzer import analyze_dataframe
from autoeda.visualizer import target_relationship
from autoeda.outliers import detect_outliers
from autoeda.imbalance import check_class_imbalance
from autoeda.reporter import generate_html_report


def main():
    parser = argparse.ArgumentParser(description="Auto EDA CLI Tool")
    parser.add_argument(
        'file', type=str, help="Path to the dataset (CSV file)")
    parser.add_argument('--target', type=str,
                        help="Target column name for analysis (optional)")
    parser.add_argument('--outliers', action='store_true',
                        help="Detect outliers in the dataset")
    parser.add_argument('--imbalance', action='store_true',
                        help="Check class imbalance in target column")
    parser.add_argument('--report', action='store_true',
                        help="Generate an HTML EDA report")
    args = parser.parse_args()

    # Load the dataset
    df = pd.read_csv(args.file)

    # Perform analysis based on provided arguments
    if args.outliers:
        print("Detecting outliers...")
        outliers = detect_outliers(df)
        print(outliers)

    if args.imbalance:
        if not args.target:
            print("Please provide a target column for imbalance check using --target")
        else:
            print(f"Checking class imbalance for '{args.target}'...")
            imbalance, is_imbalanced = check_class_imbalance(df, args.target)
            print(imbalance)
            print(f"Is the class distribution imbalanced? {is_imbalanced}")

    if args.target:
        print(
            f"Analyzing relationship between features and target '{args.target}'...")
        target_relationship(df, args.target)

    if args.report:
        print("Generating HTML EDA report...")
        generate_html_report(df)


if __name__ == "__main__":
    main()
