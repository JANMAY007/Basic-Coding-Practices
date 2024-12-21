import pandas as pd
import chart_studio.plotly as py
import plotly.offline as po
import plotly.graph_objs as pg
import matplotlib.pyplot as plt
po.init_notebook_mode(connected=True)
gdp=pd.read_csv('D:\My data\Python_language_practice\python applications\geographical plottings\gdp.csv')
gdp.head()
data=dict(type='choropleth', locations=gdp['CODE'],z=gdp['GDP (BILLIONS)'],text=gdp['COUNTRY'])
layout=dict(title='GDP geo plot',geo=dict(projection={'type':'stereographic'}))
x=pg.Figure(data=[data],layout=layout)
po.plot(x)
plt.show()