import warnings
import plotly.graph_objects as go

warnings.filterwarnings("ignore")

from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.tools as tls
from plotly.subplots import make_subplots

def plotSeasonalDecompose(x,model='additive',period=12):
  result = seasonal_decompose(x, model=model,period=period)
  fig = make_subplots(
            rows=4, cols=1,
            subplot_titles=["Observed", "Trend", "Seasonal", "Residuals"])
  fig.add_trace(
            go.Scatter(x=result.seasonal.index, y=result.observed, mode='lines'),
                row=1, col=1,
            )

  fig.add_trace(
            go.Scatter(x=result.trend.index, y=result.trend, mode='lines'),
                row=2, col=1,
            )

  fig.add_trace(
            go.Scatter(x=result.seasonal.index, y=result.seasonal, mode='lines'),
                row=3, col=1,
            )

  fig.add_trace(
            go.Scatter(x=result.resid.index, y=result.resid, mode='lines'),
                row=4, col=1,
            )
  fig.update_layout(height=1000, width=1000,title="Seasonal Decomposition")

  return fig


#plotSeasonalDecompose(data['Real GDP growth'],model='additive',period=4)