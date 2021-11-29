import warnings
import pandas as pd
from arch.unitroot import PhillipsPerron
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
import plotly.express as px

warnings.filterwarnings("ignore")


class stationary_test:
    """
    Class to calculate various test related to stationarity of time series
    """

    def __init__(self, data, columns):
        """
        Init function of stationary_test class

        Args:
            data ([pandas_dataframe]): dataset for doing operations
            columns ([list]): list of columns
        """
        self.data = data
        self.columns = columns

    def phillips(self):
        """
        Function takes input as dataframe and columns and generate
        PP Test result for the same

        Returns:
            pandas dataframe: Return the dataframe containing the PP statistics,
            p-value and interpretation
        """
        df = {}
        for x in self.columns:
            d = PhillipsPerron(self.data[x])
            if d.pvalue <= 0.05:
                y = "Data has no unit root and is stationary"
            else:
                y = "Time series has a unit root, indicating it is non-stationary "

            df[x] = {
                "PP Statistic": d.stat,
                "p-value": d.pvalue,
                "#Lags Used": d.lags,
                "Interpretation": y,
            }
        result = pd.DataFrame(df)
        return result.transpose()

    def AD_Fuller(self):
        """
        Function takes input as dataframe and columns and
        generate ADF Test result for the same

        Returns:
            pandas dataframe: Return the dataframe containing the ADF statistics,p-value and interpretation
        """
        df = {}
        for x in self.columns:
            d = adfuller(self.data[x])
            if d[1] <= 0.05:
                y = "Data has no unit root and is stationary"
            else:
                y = "Time series has a unit root, indicating it is non-stationary "

            df[x] = {
                "ADF Test Statistic": d[0],
                "p-value": d[1],
                "#Lags Used": d[2],
                "#Observations Used": d[3],
                "Interpretation": y,
            }
        result = pd.DataFrame(df)
        return result.transpose()

    def KPSS(self):
        """
        Function takes input as dataframe and columns and
        generate KPSS Test result for the same

        Returns:
            pandas dataframe: Return the dataframe containing the KPSS statistics,p-value and interpretation
        """
        df = {}
        for x in self.columns:
            d = kpss(self.data[x])
            if d[1] >= 0.05:
                y = "The series is stationary"
            else:
                y = "The series is non-stationary "

            df[x] = {
                "KPSS Statistic": d[0],
                "p-value": d[1],
                "#Lags Used": d[2],
                "Interpretation": y,
            }
        result = pd.DataFrame(df)
        return result.transpose()

    def plots(self):
        """Generating time plot for all variables

        Returns:
            [plotly figure]: Return the list of plotly figure
        """
        result = []
        for x in self.columns:
            fig = px.line(self.data, x=self.data.index, y=x, title="abhi pata nahi")
            fig.update_xaxes(
                title_text="<b>" + "Date" + "<b>",
                title_font=dict(
                    family="Courier New, monospace", size=18, color="#7f7f7f"
                ),
            )
            fig.update_xaxes(rangeslider_visible=True)
            result.append(fig)
        return result


# data = pd.read_csv("data.csv")
# columns = [
#     "Real GDP growth",
#     "Nominal GDP growth",
#     "Unemployment rate",
#     "CPI inflation rate",
# ]
# st = stationary_test(data, columns)
# graphs = st.plots()
# x = st.AD_Fuller()
# y = st.KPSS()
# z = st.phillips()
