import requests

def notifysend(token, msg):
    #line伺服器位址
    url = "https://notify-api.line.me/api/notify"
    #token認證
    headers={   
                "Authorization": "Bearer " + token, 
                # "Content-Type" : "application/x-www-form-urlencoded",
                # "Content-Type" : "multipart/form-data"
            }
    
    #欲傳送之訊息
    payload={
                #發送訊息
                "message": msg, 
                #發送貼圖
                "stickerPackageId": 446,
                "stickerId": 1988,          
            }
    #發送圖片
    files = {'imageFile': open("pexels-mayur-gawade-14417597.jpg","rb")}
    
    #將headers和data.files傳送至url，也就是將token和訊息傳送至line伺服器
    r = requests.post(url, headers=headers, data=payload, files=files)
    # #status_code為requests除錯用，回傳錯誤代碼，不用理會
    return r.status_code

#從linenotify申請的token
token = "VyJOVkIL4I1551pWi18igZAmHz1QzH4SoJEx6iWZFvu"
#傳送的訊息
msg = "\n來場說走就走的旅行!"
#呼叫函式
notifysend(token, msg)
