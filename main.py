# 主程式
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from mqtt_client import *

app = FastAPI() 
# app.mount("/static", StaticFiles(directory="static"), name="static") # 將靜態檔案目錄 static 掛載到 /static 路由

# 當路由發生錯誤時，回傳 HTMLResponse 物件 /errorpage.html
@app.exception_handler(Exception)
async def exception_handler(request, exc):
    errormsg = f"Error: {exc}"
    return HTMLResponse(content=open("./page/errorpage.html", "r").read().replace("{{errormsg}}", errormsg), status_code=500)

# 當發生404錯誤時，回傳 HTMLResponse 物件 /404.html
@app.exception_handler(404)
async def not_found(request, exc):
    return HTMLResponse(content=open("./page/errorpage.html", "r").read().replace("{{errormsg}}", "404 Not Found"), status_code=404)

# 當路由指向根目錄時，回傳 HTMLResponse 物件 /index.html
@app.get("/")
async def root():
    with open("./page/index.html", "r", encoding="utf-8") as file:
        content = file.read()
    return HTMLResponse(content=content, status_code=200)

# 使用POST方法，用於發送訊息到指定主題，並回傳JSON格式的訊息
# 格式範例: {"server": "test.io", "port": 1883, "topic": "test", "message": "Hello, MQTT!"}
@app.post("/mqtt")
async def mqtt_post(data: dict):
    try:
        # 發送訊息到指定主題
        send_message(data["server"], data["port"], data["topic"], data["message"])
    except Exception as e:
        print(f"Error sending message: {e}")
        return {"error": f"{e}"} # 回傳錯誤訊息
    return {"message": "Message sent successfully"} # 回傳成功訊息

# PWA Service Worker
@app.get("/service-worker.js", response_class=HTMLResponse)
async def service_worker():
    with open("./pwa/service-worker.js", "r", encoding="utf-8") as file:
        content = file.read()
    return HTMLResponse(content=content, media_type="application/javascript", status_code=200)

# PWA Manifest
@app.get("/manifest.json", response_class=HTMLResponse)
async def manifest():
    with open("./pwa/manifest.json", "r", encoding="utf-8") as file:
        content = file.read()
    return HTMLResponse(content=content, media_type="application/json", status_code=200)

# PWA icon
@app.get("/icon-512x512.png", response_class=HTMLResponse)
async def pwa_icon():
    with open("./pwa/icon-512x512.png", "rb") as file:
        content = file.read()
    return HTMLResponse(content=content, media_type="image/png", status_code=200)

# 啟動伺服器
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0" , port=80) # 開啟伺服器，監聽 8000 port
