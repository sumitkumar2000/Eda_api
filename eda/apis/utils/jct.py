import warnings
import pandas as pd

warnings.filterwarnings("ignore")
from statsmodels.tsa.vector_ar.vecm import coint_johansen

def output_johansen(res,columns):
    ls=[]
    for i in range(len(columns)):
      ls.append('r<='+str(i))
    output_trace=pd.DataFrame(res.cvm,index=ls,columns=['10 pct','5 pct','1 pct'])
    output_trace.insert(0,'Trace_stat',res.lr1)
    output_eigen=pd.DataFrame(res.cvt,index=ls,columns=['10 pct','5 pct','1 pct'])
    output_eigen.insert(0,'eigen_stat',res.lr2)

    return (output_trace,output_eigen)
    
def johansen(data,columns,order):  
  z=coint_johansen(data[columns],0,order)
  return output_johansen(z,columns)

#ans=johansen(data,columns,1)