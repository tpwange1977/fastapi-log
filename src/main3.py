import logging
from fastapi import FastAPI
import uvicorn
import time
import random
import string

app = FastAPI()

log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
uvicorn.run(app, log_config=log_config)


@app.get("/")
async def root():
    return {"status": "alive"}

def main():
    #uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
    uvicorn.run("main3:app", host="127.0.0.1", port=5000, log_config=log_config)

if __name__ == "__main__":
    main()