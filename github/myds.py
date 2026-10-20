import pandas as pd
singers={'Singers':['Justin Bieber','Taylor Swift','Sabrina Carpenter','Ed Sheeran','Lana Del Rey','The Weeknd',' Shawn Mendes',' Camila Cabello',
               'Katy Perry','Eminem','Olivia','Michael Jackson','Billie Eilish','Ariana Grande','Lady Gaga','Olivia Rodrigo ','ADELA ','Zayn Malik'],
    'Nationality':['Canadian','American','American','British','American','Canadian','Canadian','Cuban-American','American','American',
                   'American','American','American','American','American','American','British','British'], 
    'Net_Worth':[200_000_000,    2_000_000_000,    22_000_000,    400_000_000,    30_000_000,    300_000_000,    40_000_000,    18_000_000,    400_000_000,    250_000_000,    16_000_000, 
                    2_000_000_000,    50_000_000,    240_000_000,    320_000_000,    16_000_000,    220_000_000,    75_000_000],
    'Collaborations':[25,40,15,30,12,35,20,18,22,45,10,20,15,25,18,10,20,12],
    'Solo':          [80,180,50,90,90,100,60,50,60,120,30,100,50,90,60,30,70,35],
    'Total Songs':   [105,220,65,120,102,135,80,68,72,165,40,120,65,115,78,40,90,45]
} 

ds = pd.DataFrame(singers)
print("\n________________________________")
print()
print("1|Explore The Data")
print("___________________________________")
print(ds.head(10))
print(ds.tail(8))
print(ds.info())
print(ds.describe())
print(ds.columns)
print(ds.index)
print()
print("\n________________________________")
print("2|Accessing & Filtering data")
print("\n________________________________")
print()
print("A|Basic Access")
print(ds['Net_Worth'])                  # Single column
print(ds[['Singers', 'Nationality']])        # Multiple columns
print(ds.iloc[0] )                # First row by position
print(ds.loc[0])                  # First row by label
print()
print("\n______________________________")
print("B|Conditional Filtering")
print()
print(ds[ds['Net_Worth'] > 30_000_000])                                      # Networth over 30_000_000
print(ds[ds['Nationality'] == 'American'])                                     # Nationality match
print(ds[(ds['Net_Worth'] >22_000_000 ) & (ds['Nationality'] == 'Canadian')])  # Multiple conditionsConditional Filtering")
print()
print("\n_______________________________")
print("C|Advanced Filtering")
print()
print(ds[ds['Singers'].str.startswith('L')])                     # Names starting with L
print(ds[ds['Nationality'].isin(['Canadian', 'American'])])      # Match multiple values
print(ds[~ds['Nationality'].isin(['American'])])                 # NOT condition
print()
print("D|Advanced Filtering")
print("\n________________________________")
print(ds[ds['Nationality'].isin(['Canadian', 'American'])])      # Match multiple values
print(ds[~ds['Nationality'].isin(['British'])])                 # NOT condition
print()
print("3|Delete Access")
print("\n__________________________________")
print()
df= ds.drop(2, axis=0)  # Drop row with index 2
print(df)
df= ds[ds['Singers'] != 'Ariana Grande']  # Drop rows where name == Ariana Grande
print(df)               
df = ds.drop('Net_Worth', axis=1)     #Drop Column   
print(df)                
