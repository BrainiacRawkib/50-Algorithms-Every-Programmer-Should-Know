"""
Dimensionality reduction: Principal component analysis
"""
import pandas as pd

from sklearn.decomposition import PCA


url: str = "https://storage.googleapis.com/neurals/data/iris.csv"

iris = pd.read_csv(url)

if __name__ == '__main__':
    print(iris)

    X = iris.drop('Species', axis=1)
    pca = PCA(n_components=4)
    pca.fit(X)
    pca_df = (pd.DataFrame(pca.components_, columns=X.columns))
    print(pca_df)

    print(pca.explained_variance_ratio_)

    X['PC1'] = X['Sepal.Length'] * pca_df['Sepal.Length'][0] + X['Sepal.Width'] * pca_df['Sepal.Width'][0] + X[
        'Petal.Length'] * pca_df['Petal.Length'][0] + X['Petal.Width'] * pca_df['Petal.Width'][0]
    X['PC2'] = X['Sepal.Length'] * pca_df['Sepal.Length'][1] + X['Sepal.Width'] * pca_df['Sepal.Width'][1] + X[
        'Petal.Length'] * pca_df['Petal.Length'][1] + X['Petal.Width'] * pca_df['Petal.Width'][1]
    X['PC3'] = X['Sepal.Length'] * pca_df['Sepal.Length'][2] + X['Sepal.Width'] * pca_df['Sepal.Width'][2] + X[
        'Petal.Length'] * pca_df['Petal.Length'][2] + X['Petal.Width'] * pca_df['Petal.Width'][2]
    X['PC4'] = X['Sepal.Length'] * pca_df['Sepal.Length'][3] + X['Sepal.Width'] * pca_df['Sepal.Width'][3] + X[
        'Petal.Length'] * pca_df['Petal.Length'][3] + X['Petal.Width'] * pca_df['Petal.Width'][3]
    print(X)
