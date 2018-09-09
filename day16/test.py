import  requests

### 1、首先登陆任何页面，获取cookie

i1 = requests.get(url= "http://dig.chouti.com/help/service")

### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
i2 = requests.post(
    url= "http://dig.chouti.com/login",
    data= {
        'phone': "8613764236450",
        'password': "lpwoaini123",
        'oneMonth': ""
    },
    cookies = i1.cookies.get_dict()
)

### 3、点赞（只需要携带已经被授权的gpsd即可）
gpsd = i1.cookies.get_dict()['gpsd']
i3 = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=16958066",
    cookies={'gpsd': gpsd }
)
print(i3.text)