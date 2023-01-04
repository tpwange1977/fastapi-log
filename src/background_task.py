from fastapi import FastAPI, BackgroundTasks
import uvicorn
import time

app = FastAPI()

# 這裡是 background 要做的事情
def sao(email: str, message=""):
    time.sleep(10)
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.get('/sao/{email}')
async def send(email: str, background_tasks: BackgroundTasks):
    # 把事情交到 background 後，注意 add_task 第一個參數是 method, 接著才開始傳參數
    background_tasks.add_task(sao, email, message="some notification")
    
    #交到background 後，直接回傳收到訊息
    return {"message": "Notification sent in the background"}

def main():
    #uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
    uvicorn.run(app="background_task:app", host="127.0.0.1", port=5000, reload=True)

if __name__ == "__main__":
    main()    