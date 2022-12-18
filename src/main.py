# main.py

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from custom_logging import CustomizeLogger
from pathlib import Path
from fastapi import Request, Response
import uvicorn
import logging
import time
import random
from random import randint
import string

# from prometheus_client import generate_latest
# import prometheus_metrics as prometheus_metrics
from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest, CollectorRegistry
import prometheus_client

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='./server.log')
formatter = logging.Formatter("%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s")

ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch) #将日志输出至屏幕
logger.addHandler(fh) #将日志输出至文件

logger = logging.getLogger(__name__)

app = FastAPI()

REGISTRY = CollectorRegistry(auto_describe=False)
counter = Counter('my_counter', 'an example showed how to use counter', ["label1", "label2", "label3"], registry=REGISTRY)
gauge = Gauge('my_gauge', 'an example showed how to use gauge', ["label1", "label2", "label3"], registry=REGISTRY)

buckets = (100, 200, 300, 500, 1000, 3000, 10000, float('inf'))
histogram = Histogram('my_histogram', 'an example showed how to use histogram', ["label1", "label2", "label3"], buckets=buckets, registry=REGISTRY)
summary = Summary('my_summary', 'an example showed how to use summary', ["label1", "label2", "label3"], registry=REGISTRY)


@app.middleware("http")
async def log_requests(request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    
    response = await call_next(request)
    
     = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response


@app.get('/metrics', response_class=PlainTextResponse)
def hello():
   
    counter.labels('127.0.0.1','Program A','Function 1').inc(1)
    gauge.labels('127.0.0.1','Program A','Function 2').set(2)
    histogram.labels('127.0.0.1','Program C','Function 3').observe(1001)
    summary.labels('127.0.0.1','Program B','Function 3').observe(randint(1, 10))

    return prometheus_client.generate_latest(REGISTRY)

@app.get("/")
async def root():
    return {"message": "Hello World"}

#@app.on_event("startup")
#async def startup():
#    logger.info(f"starting Prometheus....")
    #prometheus_metrics.main()

def main():
    #uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
    uvicorn.run(app="main:app", host="127.0.0.1", port=5000, reload=True)

if __name__ == "__main__":
    main()






