import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def explore_data(file_path):
    df = pd.read_csv(file_path)
    

    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())
    
    numerical_cols = ['temp', 'sis', 'hygro', 'anem1', 'anem2']
    if 'action' in df.columns:
        sns.pairplot(df, vars=numerical_cols, hue='action', diag_kind='kde')
        plt.suptitle("Pairplot des variables avec 'action'", y=1.02)
        plt.show()
    else:
        sns.pairplot(df, vars=numerical_cols, diag_kind='kde')
        plt.suptitle("Pairplot des variables", y=1.02)
        plt.show()

if __name__ == '__main__':
    explore_data('../data/captor_2_with_null.csv')
