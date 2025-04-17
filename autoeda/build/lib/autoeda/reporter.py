from ydata_profiling import ProfileReport


def generate_html_report(df, output_file="eda_report.html"):
    profile = ProfileReport(df, title="Auto EDA Report", explorative=True)
    profile.to_file(output_file)
    print(f"Report saved to {output_file}")
