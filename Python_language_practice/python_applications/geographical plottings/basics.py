import pandas as pd
import chart_studio.plotly as py
import plotly.offline as po
import plotly.graph_objs as pg
import matplotlib.pyplot as plt
po.init_notebook_mode(connected=True)
agri=pd.read_csv('agri.csv')
print(agri)
layout=dict(geo={'scope':'usa'})
data=dict(type='choropleth', locations=['AL','AR','AK','AZ','CA'], locationmode='USA-states',z=[1,2,30,40,50],text=['alaska','arizona','alabama','pugger','california'])
x=pg.Figure(data=[data],layout=layout)
po.plot(x)