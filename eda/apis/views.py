from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils.st import *
from .utils.granular import *
from .utils.jct import *
class StationaryTestView(APIView): 

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            try:
                table = pd.read_csv(r"F:\Time_series_EDA\eda\data.csv")
            except Exception as ex:
                print(ex)
                return Response({"msg":"Table not found"},status=400)

            st = stationary_test(table, data['columns'])
            graphs = st.plots()
            if data['method'] == 'AD_Fuller':
                x = st.AD_Fuller()
            if data['method'] == 'KPSS':
                x = st.KPSS()
            if data['method'] == 'phillips':
                x= st.phillips()
            print(x)
            output = {'charts': "url",
                          'tables': [{"data":x.to_json(orient='records'),"id":3,"header":"Percentile Table"}],
                        #   'table_id': [t1.id, t2.id, t3.id],
                          'isChart' : True,
                          'isTable' : True,
                          'isGrid': False}
            return Response({"result":output},status=200)
        except Exception as ex:
            print(ex)
            return Response({"msg":str(ex)},status=500)
        

class grangers_api(APIView): 

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            try:
                table = pd.read_csv(r"F:\Time_series_EDA\eda\data.csv")
            except Exception as ex:
                print(ex)
                return Response({"msg":"Table not found"},status=400)

            ans = grangers_causality_matrix(table, data['order'],data["columns"])
            
            print(ans)
            output = {'charts': "url",
                          'tables': [{"data":ans.to_json(orient='records'),"id":3,"header":"Percentile Table"}],
                        #   'table_id': [t1.id, t2.id, t3.id],
                          'isChart' : True,
                          'isTable' : True,
                          'isGrid': False}
            return Response({"result":output},status=200)
        except Exception as ex:
            print(ex)
            return Response({"msg":str(ex)},status=500)
        



class johansen_api(APIView): 

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            try:
                table = pd.read_csv(r"F:\Time_series_EDA\eda\data.csv")
            except Exception as ex:
                print(ex)
                return Response({"msg":"Table not found"},status=400)

            ans = johansen(table,data["columns"], data['order'])
            
            print(ans)
            output = {'charts': "url",
                          'tables': [{"data":ans[1].to_json(orient='records'),"id":3,"header":"Percentile Table"}],
                        #   'table_id': [t1.id, t2.id, t3.id],
                          'isChart' : True,
                          'isTable' : True,
                          'isGrid': False}
            return Response({"result":output},status=200)
        except Exception as ex:
            print(ex)
            return Response({"msg":str(ex)},status=500)