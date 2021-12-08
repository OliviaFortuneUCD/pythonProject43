import pandas as pd
covid = pd.read_csv("COVID.csv")
#This is my code 
# Choose entries with county Name of Cork.
Corkonly  = covid[covid['CountyName'] == 'Cork']
Dublinonly  = covid[covid['CountyName'] == 'Dublin']
Belfast  = covid[covid['CountyName'] == 'Belfast']
Limeick  = covid[covid['CountyName'] == 'Limerick']

print(Corkonly.to_string())
print(Dublinonly.to_string())
print(Belfast.to_string())
