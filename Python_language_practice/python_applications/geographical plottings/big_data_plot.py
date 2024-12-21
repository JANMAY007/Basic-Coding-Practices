import pandas as pd
import chart_studio.plotly as py
import plotly.offline as po
import plotly.graph_objs as pg
import matplotlib.pyplot as plt
po.init_notebook_mode(connected=True)
agri=pd.read_csv('agri.csv')
#print(agri)
data=dict(type='choropleth', locations=agri['code'], locationmode='USA-states',z=agri['total exports'],text=agri['text'])
layout=dict(geo={'scope':'usa'})
x=pg.Figure(data=[data],layout=layout)
po.plot(x)
plt.show()