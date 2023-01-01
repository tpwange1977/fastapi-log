
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from custom_logging import CustomizeLogger
from pathlib import Path
from fastapi import Request, Response
import uvicorn
import logging
from kubernetes import client, config

app = FastAPI()

@app.get('/hello', response_class=JSONResponse)
def hello():
# Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()
    result = []

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)

    for i in ret.items:
        #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        item = {}
        item["pod_ip"] = i.status.pod_ip
        item["namespace"] = i.metadata.namespace
        result.append(item)

    return JSONResponse(status_code=200, content=result)


def main():
    #uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
    uvicorn.run(app="kubernates:app", host="127.0.0.1", port=5000, reload=True)

if __name__ == "__main__":
    main()    