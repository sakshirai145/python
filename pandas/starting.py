import pandas as pd

data_1 = {
    'id': [1,2,3,4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']

}

data_2 ={
       'id': [1,2,3],
      'pesonality_devlepment': ["A++","B","D+"],
      'company_name':["TCS","Infosys","Wipro"]
}

df1 = pd.DataFrame(data_1)
df2 = pd.DataFrame(data_2)

result = pd.merge(df1, df2, on='id', how='inner')
print(result)


#left_join = pd.merge(df1, df2, on='id', how='left')
#print(left_join)

df2["id"].groupby(df2["company_name"]).count()

#df = pd.DataFrame(data)
#print(df)

#print(df.iloc[0:2, 0:3])

#df["intrest"]=["football","hocky","basketball"]
#print(df)