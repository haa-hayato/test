import cv2
import time
import datetime
import requests

def send_message(Discovery_time):
    url = "https://notify-api.line.me/api/notify" 
    token = "5kc9kZmNrl9Phup1qq770mqCO4PR0dbs21VG4PzZaQY"
    headers = {"Authorization" : "Bearer "+ token}
    files = {'imageFile': open("tmp.jpg", "rb")}
    message =  (Discovery_time,"トイレしてるニャー")
    payload = {"message" :  message} 
    r = requests.post(url, headers = headers, params=payload, files=files)

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    
    key = cv2.waitKey(1)

    #特徴量学習データhaarcascade_frontalcatface_extended.xmlを読み込みface_cascadeに代入
    face_cascade=cv2.CascadeClassifier('/home/pi/cat/model/opencv-master/data/haarcascades/haarcascade_frontalcatface_extended.xml')
    # 顔検出のパラメータの設定
    faces=face_cascade.detectMultiScale(gray)
    # 顔検出時に四角い枠を表示
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    
    # imshow関数で結果を表示する
    cv2.imshow("faces",frame)
  
    if key == 13:
        ret, frame = camera.read()
        cv2.imwrite('tmp.jpg', frame)
        #camera.release()
        dt_now = datetime.datetime.now()
        Discovery_time = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
        send_message(Discovery_time)
  # Escキーを入力されたら画面を閉じる
    if key == 27:
        break

