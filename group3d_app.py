import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import streamlit as st
import plotly.graph_objects as go



plt.style.use(['science', 'nature'])
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['xtick.major.pad']='8'

def load_dtwdata(groupname):

    df = pd.read_csv('clsevt_'+groupname+'.txt', names=('eventid', 'dtw_from85','dtw_from75', 'dtw_from59'))
    
    id = np.array( df['eventid'] )
    y = np.array(df['dtw_from75'])
    z = np.array(df['dtw_from85'])
    x = np.array(df['dtw_from59'])

    return x, y, z

xa, ya, za = load_dtwdata('groupA')
xb, yb, zb = load_dtwdata('groupB')
xc, yc, zc = load_dtwdata('groupC')

xlabel = 'DTW dist. from 59'
ylabel = 'DTW dist. from 75'
zlabel = 'DTW dist. from 85'

df_a = pd.DataFrame({xlabel:xa, ylabel:ya, zlabel:za})
df_b = pd.DataFrame({xlabel:xb, ylabel:yb, zlabel:zb})
df_c = pd.DataFrame({xlabel:xc, ylabel:yc, zlabel:zc})

st.write('# 3d プロット')

# Create an object for 3d scatter
trace1 = go.Scatter3d(
    x = df_a[xlabel], y = df_a[ylabel], z = df_a[zlabel],
    mode = 'markers',
    marker = dict(size=3, color='red'),
    name="group A"
)

trace2 = go.Scatter3d(
    x = df_b[xlabel], y = df_b[ylabel], z = df_b[zlabel],
    mode = 'markers',
    marker = dict(size=3, color='green'),
    name="group B"
)

trace3 = go.Scatter3d(
    x = df_c[xlabel], y = df_c[ylabel], z = df_c[zlabel],
    mode = 'markers',
    marker = dict(size=3, color='blue'),
    name="group C"
)

# Create an object for graph layout
fig = go.Figure(data=[trace1, trace2, trace3])
fig.update_layout(
    scene = dict(
    xaxis_title = xlabel,
    yaxis_title = ylabel,
    zaxis_title = zlabel,
    aspectmode='cube'
    ),
)
#fig.update_xaxes(range=(0,0.055))
#fig.update_yaxes(range=(0,0.055))

fig.update_layout(
    legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=1.0,
    ),
    font=dict(
        size=12,
    )
    )

fig.update_layout(width=800, height=800) # 図の高さを幅を指定
fig.update_layout(template="seaborn") # 白背景のテーマに変更
fig.update_layout(legend = dict(font = dict(size = 24, color = "black")),
                  legend_title = dict(font = dict(size = 24, color = "black")))
fig.update_layout(legend= {'itemsizing': 'constant'})
st.plotly_chart(fig)
