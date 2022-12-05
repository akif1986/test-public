# # 1
# import plotly.express as px
# import pandas as pd
#
# Beer_Data = 'https://raw.githubusercontent.com/plotly/datasets/master/beers.csv'
#
# df = pd.read_csv(Beer_Data, usecols=[2, 5, 6, 11, 12], nrows=25)
#
# fig = px.sunburst(df, path=[px.Constant("Beer world"), 'city', 'style', 'beer'], values='abv', color='abv',
#                   color_continuous_scale='orrd', hover_data=['style'], title='Happy Monday Hours')
#
# fig.show()



# # 2
#
# import numpy as np
# import plotly.offline as pyo
# import plotly.graph_objs as go
#
# random_x = np.random.randint(1, 20, 10)
# random_y = np.random.randint(1, 20, 10)
#
#
# data = [go.Scatter(x=random_x, y=random_y, mode='markers')]
#
# layout = go.Layout(title='demo plot', xaxis=dict(title='X - axis'),yaxis=dict(title='Y - axis'),
#                    hovermode='closest')
# fig = go.Figure(data=data, layout=layout)
#
# pyo.plot(fig, filename='Try.html')
#
#
# # 3
import plotly.express as px
df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

fig.show()

