from prometheus_client import Gauge, start_http_server, Counter
from prometheus_client.core import CollectorRegistry
import prometheus_client
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

# 定义api对象
app = FastAPI()

# 设置接口访问路径/metrics
# @app语法糖需要放在最终入口函数
@app.get('/metrics', response_class=PlainTextResponse)
def get_data():
    '''
    该函数为最终函数入口（采集数据函数）,该例子模拟采集到数据标签label1、label2和label3，数据data1
    '''
    # 定义client_python里提供的prometheus Gauge数据类型
    REGISTRY = CollectorRegistry(auto_describe=False)
    example_G = Gauge("this_is_a_metric_name", "this is a metric describe", ["label1", "label2", "label3"], registry=REGISTRY)
    
    label1 = '111'
    label2 = '222'
    label3 = '333'
    data1 = '444'
    # 调用Gauge数据类型，把采集的数据放入到设定的example_G
    example_G.labels(label1,label2,label3).set(data1)
    # return需放在函数下最外层，否则返回的数据有缺失
    return prometheus_client.generate_latest(REGISTRY)
 
# 用uvicorn调用接口，启用端口为9330
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")