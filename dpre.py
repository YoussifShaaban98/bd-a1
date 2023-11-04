def dpre():
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import KBinsDiscretizer

    # Read the dataset file
    dataset = pd.read_csv("CarPriceBigdata1.csv")

    # Data Cleaning
    # Drop rows with missing values
    dataset = dataset.dropna()

    # Separate non-numeric columns
    non_numeric_cols = dataset.select_dtypes(exclude=['float', 'int']).columns

    # Data Transformation
    # Perform standardization on numeric columns using StandardScaler
    numeric_cols = dataset.select_dtypes(include=['float', 'int']).columns
    scaler = StandardScaler()
    dataset[numeric_cols] = scaler.fit_transform(dataset[numeric_cols])

    # Data Reduction
    # Perform dimensionality reduction using PCA
    pca = PCA(n_components=2)
    dataset_reduced = pca.fit_transform(dataset[numeric_cols])

    # Data Discretization
    # Perform data discretization using KBinsDiscretizer
    discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
    dataset_discretized = discretizer.fit_transform(dataset_reduced)

    # Convert the discretized data back to a dataframe
    dataset_discretized = pd.DataFrame(dataset_discretized, columns=['Feature1', 'Feature2'])

    # Save the cleaned, transformed, reduced, and discretized dataset to a new file
    new_file_path = "processed_dataset.csv"
    dataset_discretized.to_csv(new_file_path, index=False)

    print("Data cleaning, transformation, reduction, and discretization completed.")
    print(f"Processed dataset saved to {new_file_path}.")