import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')

# Charger les données
input_file = '../data/captor_1_sample_2_with_manual_validation.csv'
output_file = '../data/captor_1_sample_2_cleaned.csv'
params_file = '../models/testiqr.json'

data = pd.read_csv(input_file)

print("The shape of the dataframe is: ", data.shape)
print("Colonnes disponibles dans le dataset :", data.columns)
print(data.head())

# Sauvegarde des paramètres IQR
def dfprocess(df, save_path=params_file):
    numerical_cols = ['temp', 'sis', 'hygro', 'anem1', 'anem2']
    params = {}

    for col in numerical_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        median = df[col].median()

        params[col] = {
            'median': median,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound
        }

    with open(save_path, 'w') as f:
        json.dump(params, f)

    print(f"Paramètres sauvegardés dans {save_path}")


# Remplacement des valeurs aberrantes
def replace_outliers(df, params_path=params_file):
    with open(params_path, 'r') as f:
        params = json.load(f)

    numerical_cols = ['temp', 'sis', 'hygro', 'anem1', 'anem2']

    for col in numerical_cols:
        df[col] = df[col].fillna(params[col]['median'])
        df[col] = df[col].clip(lower=params[col]['lower_bound'], upper=params[col]['upper_bound'])

    print("Valeurs extrêmes remplacées.")
    return df


dfprocess(data)
data_cleaned = replace_outliers(data)

data_cleaned.to_csv(output_file, index=False)

# plt.figure(figsize=(10, 6))
# sns.boxplot(data=data_cleaned.select_dtypes(include=['float64', 'int64']))
# plt.title("Boxplot après remplacement des valeurs extrêmes")
# plt.xticks(rotation=45)
# plt.show()
