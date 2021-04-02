import pandas as pd 
import plotly.express as px 
df=pd.read_csv("Covid.csv")
print (df)
fig=px.line(df, x="date", y="cases", color="country", title="covid graph")
fig.show()