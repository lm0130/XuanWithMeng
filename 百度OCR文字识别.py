import base64
import requests

#获取Access Token令牌
def GetAccessToken(client_id:str,client_secret:str):
    url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&'+'client_id='+client_id+'&client_secret='+client_secret
    response = requests.get(url)
    if(response):
        response =response.json()
        if(response['access_token'] is not None):
            return response['access_token']
    return None

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"#通用文字识别

client_id='9MnmnErZYlj9jKGetOe6QgxC'
client_secret='vMzCP0RxfQQFj1SxK5qXpny9W85PxK1E'
access_token = GetAccessToken(client_id,client_secret)

# 二进制方式打开图片文件
with open('OCR test 1.png','rb') as f:
    img = base64.b64encode(f.read())

    params = {"image":img}

    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())

print("萌萌成功啦，耶")