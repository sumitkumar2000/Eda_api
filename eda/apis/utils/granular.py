import warnings
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests
import numpy as np

warnings.filterwarnings("ignore")

def grangers_causality_matrix(data,order, variables, test = 'ssr_chi2test', verbose=False):
    data=data[variables]
    dataset = pd.DataFrame(np.zeros((len(variables), len(variables))), columns=variables, index=variables)

    for c in dataset.columns:
        for r in dataset.index:
            test_result = grangercausalitytests(data[[r,c]], maxlag=order, verbose=False)
            p_values = [round(test_result[i+1][0][test][1],4) for i in range(order)]
            if verbose: print(f'Y = {r}, X = {c}, P Values = {p_values}')

            min_p_value = np.min(p_values)
            dataset.loc[r,c] = min_p_value

    dataset.columns = [var + '_x' for var in variables]

    dataset.index = [var + '_y' for var in variables]

    return dataset