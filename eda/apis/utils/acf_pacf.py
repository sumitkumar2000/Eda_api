
import warnings
warnings.filterwarnings('ignore')
import numpy as np 

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.stattools import acf

import plotly.graph_objects as go


def acf_pacf(series):
    corr_array = pacf(series.dropna(), alpha=0.05)
    lower_y = corr_array[1][:,0] - corr_array[0]
    upper_y = corr_array[1][:,1] - corr_array[0]

    fig = go.Figure()
    [fig.add_scatter(x=(x,x), y=(0,corr_array[0][x]), mode='lines',line_color='#3f3f3f') 
     for x in range(len(corr_array[0]))]
    fig.add_scatter(x=np.arange(len(corr_array[0])), y=corr_array[0], mode='markers', marker_color='#1f77b4',
                   marker_size=12)
    fig.add_scatter(x=np.arange(len(corr_array[0])), y=upper_y, mode='lines', line_color='rgba(255,255,255,0)')
    fig.add_scatter(x=np.arange(len(corr_array[0])), y=lower_y, mode='lines',fillcolor='rgba(32, 146, 230,0.3)',
            fill='tonexty', line_color='rgba(255,255,255,0)')
    fig.update_traces(showlegend=False)
    fig.update_xaxes(range=[-1,30])
    fig.update_yaxes(zerolinecolor='#000000')
    
    title='Partial Autocorrelation (PACF)'
    fig.update_layout(title=title, xaxis_title="Lag")

    corr1_array = acf(series.dropna(), alpha=0.05)
    lower_y = corr1_array[1][:,0] - corr1_array[0]
    upper_y = corr1_array[1][:,1] - corr1_array[0]

    fig1 = go.Figure()
    [fig1.add_scatter(x=(x,x), y=(0,corr1_array[0][x]), mode='lines',line_color='#3f3f3f') 
     for x in range(len(corr_array[0]))]
    fig1.add_scatter(x=np.arange(len(corr1_array[0])), y=corr1_array[0], mode='markers', marker_color='#1f77b4',
                   marker_size=12)
    fig1.add_scatter(x=np.arange(len(corr1_array[0])), y=upper_y, mode='lines', line_color='rgba(255,255,255,0)')
    fig1.add_scatter(x=np.arange(len(corr1_array[0])), y=lower_y, mode='lines',fillcolor='rgba(32, 146, 230,0.3)',
            fill='tonexty', line_color='rgba(255,255,255,0)')
    fig1.update_traces(showlegend=False)
    fig1.update_xaxes(range=[-1,30])
    fig1.update_yaxes(zerolinecolor='#000000')
    
    title='Autocorrelation (ACF)'
    fig1.update_layout(title=title, xaxis_title="Lag",)

    return (fig,fig1)

