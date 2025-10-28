import pandas as pd
# lire fichier et affichier
df = pd.read_csv('earthquake_data_tsunami.csv')
print(df)
# data in  on row
data = [4, 8, 9, 0, 4, 3, 1]
S = pd.Series(data)
print(S)
# trier selon valeur dindex
print(S.sort_index())
# accessing by position
print(S.iloc[3])
# afficher du pos 2 jusqua pos 4
print(S[2:5])
# afficher les valeurs
print(S.values)
# afficher start end and step
print(S.index)
# nombre de (ligne,colonne)
print(S.shape)
print(S.size)
# --------------------------------
data2 = [4, 8, 9, None, 4, 3, 1]
index = ['Lundi', 'Mardi', 'Mercredi',
         'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
V = pd.Series(data2, index=index)
print(V)
# afficher nan
print(V.unique())
# compte nombre des data different de none et le compte une seul fois se existe plusieur equal
print(V.nunique())
# trier croissant du data
print(V.sort_values())
# afficher true dans nan
print(V.isnull())
# afficher false dans nan
print(V.notnull())

# multuplier valeur par deux lmbda is valeur de chaque index
S_doublée = S.apply(lambda x: x * 2)

print(S_doublée)
