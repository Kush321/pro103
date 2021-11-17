import pandas as pd
import plotly_express as px

df = pd.read_csv("C:\P\pythonprojects\pro103\data.csv")

fx = px.scatter(df, x = "Date", y = "Cases", color = "Country", title = "Covid Cases")
fx.show()

