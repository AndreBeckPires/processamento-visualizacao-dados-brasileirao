import kagglehub
import pandas as pd


# Download latest version
path = kagglehub.dataset_download("regazze/brasileirao-2003-2022")
path = path+'/brasileirao/nome-do-arquivo.xlsx'
print(path)
df = pd.read_excel(path,"/brasileirao/nome-do-arquivo.xlsx")
#print(df.head())