def eda():
    # Commented out IPython magic to ensure Python compatibility.
    import pandas as pd
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    # %matplotlib inline
    import seaborn as sns
    # Read the CSV file
    df = pd.read_csv('CarPriceBigdata1.csv')

    df.head()

    df.describe

    df.info

    # Insight 1: Find the number of rows and columns in the dataset
    num_rows, num_cols = df.shape
    with open('eda-in-1.txt', 'w') as f:
        f.write(f'The dataset has {num_rows} rows and {num_cols} columns.')

    # Insight 2: Find the mean of a column
    mean_col = df['price'].mean()
    with open('eda-in-2.txt', 'w') as f:
        f.write(f'The mean of price is {mean_col}.')

    # Insight 3: Find the number of unique values in a column
    unique_vals = df['price'].nunique()
    with open('eda-in-3.txt', 'w') as f:
        f.write(f'The number of unique values in price is {unique_vals}.')

    df = pd.read_csv('eda-in-1.txt')



    # Load the dataset
    data = pd.read_csv('CarPriceBigdata1.csv')

    """# ***Data Description***"""

    data.describe()

    data.shape

    data.size

    data.info()

    def save_insight(insight, filename):
        with open(filename, 'w') as file:
            file.write(insight)

    def perform_eda(dataset):
        insights = []

        # Insight 1: Get the number of rows and columns in the dataset
        num_rows = len(dataset)
        num_columns = len(dataset.columns)
        insights.append(f"Number of rows: {num_rows}\nNumber of columns: {num_columns}")

        # Insight 2: Check for missing values
        missing_values = dataset.isnull().sum().sum()
        insights.append(f"Number of missing values: {missing_values}")

        # Insight 3: Display the summary statistics of numeric columns
        numeric_columns = dataset.select_dtypes(include=[float, int]).columns
        summary_stats = dataset[numeric_columns].describe().to_string()
        insights.append(f"Summary statistics of numeric columns:\n{summary_stats}")

        # Save the insights as text files
        for i, insight in enumerate(insights):
            filename = f"eda-in-{i+1}.txt"
            save_insight(insight, filename)

    # Read the dataset file
    file_path = input("C:\bd-a1\CarPriceBigdata1.csv:")
    dataset = pd.read_csv(file_path)

    # Perform EDA and save insights
    perform_eda(dataset)

    print("Exploratory data analysis completed and insights saved as text files.")

