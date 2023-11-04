def vis():
        import matplotlib.pyplot as plt
        import pandas as pd

        # Scatter plot showing the relationship between horsepower and price
        plt.figure(figsize=(8, 6)) 
        plt.scatter(data=df, x='horsepower', y='price')
        plt.xlabel('Horsepower')
        plt.ylabel('Price')
        plt.title('Scatter Plot: Horsepower vs. Price')
        plt.savefig('scatter_plot.png', bbox_inches='tight')  
        plt.show()
        plt.close()
