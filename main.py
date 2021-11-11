import pandas as pd
covid = pd.read_csv("COVID.csv")

# Choose entries with county Name of Cork.
Corkonly  = covid[covid['CountyName'] == 'Cork']
Dublinonly  = covid[covid['CountyName'] == 'Dublin']
Belfast  = covid[covid['CountyName'] == 'Belfast']

print(Corkonly.to_string())
print(Dublinonly.to_string())
