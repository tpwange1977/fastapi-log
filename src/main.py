# main.py

from fastapi import FastAPI
from custom_logging import CustomizeLogger
from pathlib import Path
from fastapi import Request
import uvicorn
import logging
import time
import random
import string

import example as example

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

@app.middleware("http")
async def log_requests(request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup():
    logger.info(f"starting Prometheus....")
    example.main()

def main():
    #uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
   
    uvicorn.run("main:app", port=5000, reload=True)

if __name__ == "__main__":
    main()






