# source : https://www.geeksforgeeks.org/how-to-use-pandas-filter-with-iqr/

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')


data = pd.read_csv('../data/captor_1_sample_2_with_manual_validation.csv')


print("The shape of the dataframe is: ", data.shape)
print("Colonnes disponibles dans le dataset :", data.columns)
print(data.head())

# Définir une fonction pour supprimer les outliers en utilisant l'IQR
def remove_outliers(data, col):
    Q1 = np.percentile(data[col], 25)  # Premier quartile (25%)
    Q3 = np.percentile(data[col], 75)  # Troisième quartile (75%)
    IQR = Q3 - Q1  # Calcul de l'IQR

    lower_bound = Q1 - 1.5 * IQR  # Seuil inférieur
    upper_bound = Q3 + 1.5 * IQR  # Seuil supérieur

    print(f"IQR pour la colonne {col}: {IQR}")
    
    # Filtrer les valeurs aberrantes
    filtered_data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
    
    return filtered_data

# Appliquer la fonction à toutes les colonnes numériques
for col in data.select_dtypes(include=['float64', 'int64']).columns:
    data = remove_outliers(data, col)

# Afficher les nouvelles dimensions après suppression des outliers
print("Shape of data after outlier removal is: ", data.shape)

# Tracer un boxplot après le filtrage
plt.figure(figsize=(10, 6))
sns.boxplot(data=data.select_dtypes(include=['float64', 'int64']))
plt.title("Boxplot après suppression des valeurs aberrantes")
plt.xticks(rotation=45)
plt.show()

##### result pour sample2 
# The shape of the dataframe is:  (1000, 7)
# Shape of data after outlier removal is:  (828, 7)