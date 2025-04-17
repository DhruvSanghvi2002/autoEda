import seaborn as sns
import matplotlib.pyplot as plt


def plot_missing(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False)
    plt.title("Missing Values Heatmap")
    plt.show()


def plot_correlation(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Heatmap")
    plt.show()


def save_plot(df, plot_type='missing', filename="plot.png"):
    plt.figure(figsize=(10, 6))

    if plot_type == 'missing':
        sns.heatmap(df.isnull(), cbar=False)
        plt.title("Missing Values Heatmap")
    elif plot_type == 'correlation':
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Correlation Heatmap")
    else:
        raise ValueError(
            "Unsupported plot type. Choose either 'missing' or 'correlation'.")

    plt.savefig(filename)
    plt.close()
    print(f"Plot saved as {filename}")
