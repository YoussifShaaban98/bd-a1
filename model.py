def model(df):
        import pandas as pd
        from sklearn.cluster import KMeans

        X = df[['price']]
        y = df[['enginesize']]

        # Initialize and fit the K-means model with k=3
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(X,y)
        cluster_labels = kmeans.labels_

        # Count the number of records in each cluster
        cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()

        # Save the cluster counts to a text file named 'k.txt'
        cluster_counts.to_csv('k.txt', header=False, sep='\t')
        print(cluster_counts)