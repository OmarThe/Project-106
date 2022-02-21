import plotly.express as px
import pandas as pd

# x = [0,1,2,3,4] 
# y = [0,1,4,9,16]

# fig = px.scatter(x,y)
# fig.show()

df1 = pd.read_csv("Data1.csv")
df2 = pd.read_csv("Data2.csv")
df3 = pd.read_csv("Data3.csv")
df4 = pd.read_csv("Data4.csv")

# # print(df1)

# list = df1["Temperature"].to_list()

# print(list)

fig1 = px.scatter(df1, x ="Temperature", y ="Ice-cream Sales")
# fig.show()

fig2 = px.scatter(df2, x ="Size of TV", y ="Average time spent watching TV in a week")
# fig2.show()

fig3 = px.scatter(df3, x ="Marks In Percentage", y ="Days Present")
# fig3.show()

fig4 = px.scatter(df4, x ="Coffee in ml", y ="sleep in hours")
# fig4.show()
