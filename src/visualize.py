import matplotlib.pyplot as plt
import seaborn as sns

def plot_duplicate_orders_by_region(duplicates_df, save_path=None):
    """
    Shows how duplicate Order IDs are distributed across regions.
    """
    plt.figure(figsize=(8, 5))
    sns.countplot(data=duplicates_df, x='Region')
    plt.title("Duplicate Orders by Region")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    
    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved to {save_path}")
    else:
        plt.show()
