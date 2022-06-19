import numpy as np
import pandas as pd

# x = np.array([1,2,3,4])
# print(x,type(x))
# arr = np.array([[1,2,3],[4,5,6],[8,9,10]])
# print(arr)
# print()
# print()
#
# print("this is panda series")
# y = pd.Series([1,2,3,4])
# print(y,type(y))
# a = pd.DataFrame([[1,2,3],[4,5,6],[8,9,10]])
# print(a,type(a))

# df = pd.read_csv("survey_results_public.csv")
# print(df)
# print(df.shape)
# print(df.info())

# print(df.head(10))
# print(df.tail(10))
# pd.set_option('display.max_columns',85)
# print(df)
# df = pd.read_csv('survey_results_schema.csv')
# schema_df = pd.read_csv('data/survey_results_schema.csv')

people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)
# print(df)
# print(df.email)
# print(type(df))
# print(df["last"], "square brackets gives the coulmn heading")
# print(df[["last", "email"]],"passed a list of column")
# print(df.columns, "gives the list of columns together")
# print(df.iloc[0], "int location is iloc 0 gives the first row")
# print(df.iloc[[0,1],2], "needs to have 2 brackes in form of list 2 is the column")
# print(df.loc[[0,1],['email','last']], "using index loc is lable location")

print(df.index)
print()
print(df.set_index('email'))
print()
print(df)
print()
print(df.loc['CoreyMSchafer@gmail.com'])



