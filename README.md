# API_ML_AI
## PRD:
### 价值宣言：
一般进出入门口都以人脸识别为核心，产品的价值在于可提供声纹识别进行验证，进一步拓展至通关密语和社交交互（语音转文本留言）。
### 核心价值：
最小可用产品是实现声纹识别，通过用户的声音检测是否本人来进出入门口；可通过通关密语进入宿舍，也可以用声音转化为文本留言进行社交。
### 核心价值与用户痛点：
- 用户在没有多余的手开门时，可以通过声控开门。
- 用户无需掏出饭卡/身份证进行识别，更加便捷。
- 用户在外出的时候，隔壁邻居可以留言。
### 人工智能概率论与用户痛点：
使用声纹识别结合其他生物识别作为门禁系统的开锁方式，可实现无需携带任何物品的验证流程，解决用户无手开门的痛点。也提供了留言功能，可以为其用户留下相应的文本，让用户了解其内容。

微软智能云Azure,做到了100%响应时间达成率，77%的当天解决率以及95%的客户满意度；另一方面也在探索如何让客户通过自服务工具来实现预防问题、自助排查。

[参考内容：人来人往的五年，微软智能云Azure凭什么活着？](http://baijiahao.baidu.com/s?id=1596152335406916681&wfr=spider&for=pc)

因此，声纹识别采用了微软智能云Azure的声纹识别API(说话人识别API)和通关密语（说话人验证API)。

留言功能则是采用讯飞的语音转文本（语音转写API）功能。

讯飞开放平台拥有领先的语音识别技术，核心技术达到国际领先水平，语音识别准确率已经超过98%，在业界遥遥领先。

[参考内容：讯飞语音识别准确率提升至98% 启动“AI方言发音人”招募](http://baijiahao.baidu.com/s?id=1603130852014133085&wfr=spider&for=pc)
### 需求列表与人工智能API:

Title | User story | importance | Notes | API
---|---|--------|------|-----
声控开门 | 用户在没有多余的手开门的时候，可以通过声音识别从而开门 | 重要 | 声纹识别 | 说话人识别API
密令 | 用户通过设定的通关密语验证卡门 | 重要 | 通关密语 | 说话人验证API
留言 | 用户在外出的情况下，隔壁邻居可以通过声音留言 | 次要 | 语音转文本 | 语音听写API



## 原型：
### 交互及界面设计：
##### 声纹识别：
![图片](https://github.com/JamieYin/API_ML_AI/blob/master/img/appuse1.jpg)

##### 通关密语：
![图片](https://github.com/JamieYin/API_ML_AI/blob/master/img/appuse2.jpg)

##### 留言消息：
![图片](https://github.com/JamieYin/API_ML_AI/blob/master/img/appuse3.jpg)

### 信息设计：
##### 用户的声纹识别：
![图片](https://github.com/JamieYin/API_ML_AI/blob/master/img/design1.jpg)
##### 用户的密语通关：
![图片](https://github.com/JamieYin/API_ML_AI/blob/master/img/design2.jpg)
##### 用户点击留言按钮：
![图片](https://github.com/JamieYin/API_ML_AI/blob/master/img/design3.jpg)

### 原型文档
[下载原型文档](https://github.com/JamieYin/API_ML_AI/blob/master/%E5%8E%9F%E5%9E%8B%E6%96%87%E6%A1%A3.rp)


## API:
### 使用水平：
**1.核心功能：声纹识别VPR（Voice Print Recognition）**。

采用的是Microsoft Azure的说话人识别API(Speaker Recognition API)。

用户需要在其门户下注册账号，订阅相关的API资源，方可使用其API。
用户注册声音三次后，即可进行声纹识别，验证是否为本人。

以下是我使用的代码：

```
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '你的密钥,
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/spid/v1.0/verificationProfiles?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
```
结果：
```
b'[\r\n  {\r\n    "verificationProfileId": "669c521b-6695-4a3e-9c9b-34b5bacf4207",\r\n    "locale": "en-us",\r\n    "enrollmentsCount": 0,\r\n    "remainingEnrollmentsCount": 3,\r\n    "createdDateTime": "2019-01-07T12:44:22.260Z",\r\n    "lastActionDateTime": "2019-01-07T12:44:22.260Z",\r\n    "enrollmentStatus": "Enrolling"\r\n  }\r\n]'
```
```
{
  "Result": "Accept",
  "Confidence": "Normal",
}
```
参考内容：
- [微软说话人识别API](https://westus.dev.cognitive.microsoft.com/docs/services/563309b6778daf02acc0a508/operations/5645c3271984551c84ec6797)

**2. 通关密语API(说话人验证)**
- 注册：
演讲者验证的注册与文本有关，这意味着演讲者需要选择在注册和验证阶段使用的特定密码短语。

- 在登记中，记录说话者的语音，说出特定短语，然后提取许多特征并识别所选择的短语。所有提取的特征和所选择的短语一起形成独特的语音签名。

- 验证：
在验证中，将输入语音和短语与登记的语音签名和短语进行比较 - 以便验证他们是否来自同一个人，以及他们是否说出正确的短语。

采用的是微软说话人验证API代码：将我录制的密语录入，即可进行验证。

```
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '你的密钥',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/spid/v1.0/identificationProfiles?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
```
结果：
```
b'[\r\n  {\r\n    "identificationProfileId": "12363eb4-3d67-4c20-8ae0-297024d96311",\r\n    "locale": "zh-cn",\r\n    "enrollmentSpeechTime": 0.0,\r\n    "remainingEnrollmentSpeechTime": 30.0,\r\n    "createdDateTime": "2019-01-07T13:00:21.047Z",\r\n    "lastActionDateTime": "2019-01-07T13:00:21.047Z",\r\n    "enrollmentStatus": "Enrolling"\r\n  },\r\n  {\r\n    "identificationProfileId": "cd948285-9fa0-48b7-8a9e-7a0cad3c359e",\r\n    "locale": "zh-cn",\r\n    "enrollmentSpeechTime": 0.0,\r\n    "remainingEnrollmentSpeechTime": 30.0,\r\n    "createdDateTime": "2019-01-07T13:00:31.574Z",\r\n    "lastActionDateTime": "2019-01-07T13:00:31.574Z",\r\n    "enrollmentStatus": "Enrolling"\r\n  },\r\n  {\r\n    "identificationProfileId": "fafc58d3-8bf5-49cf-9fdf-95fc2747c853",\r\n    "locale": "zh-cn",\r\n    "enrollmentSpeechTime": 0.0,\r\n    "remainingEnrollmentSpeechTime": 30.0,\r\n    "createdDateTime": "2019-01-07T12:49:05.578Z",\r\n    "lastActionDateTime": "2019-01-07T12:49:05.578Z",\r\n    "enrollmentStatus": "Enrolling"\r\n  }\r\n]'
```
```
  "Result": "Accept",
  "Confidence": "Normal",
  "Phrase": "i am going to make him an offer he cannot refuse"
```
参考内容：
- [微软说话人验证API）](https://westus.dev.cognitive.microsoft.com/docs/services/563309b6778daf02acc0a508/operations/5645c3271984551c84ec6797)

- [两个微软的代码调用](https://github.com/JamieYin/API_ML_AI/blob/master/%E5%BE%AE%E8%BD%AF%E4%B8%A4%E4%B8%AAapi%E8%B0%83%E7%94%A8.py)

**3. 留言消息（语音转文本）**

用户可以按下留言按钮，用户留言的语音即可转化为文本留言，与其用户进行交互。

代码示例：（由于微软没有python的api调用，所以运用的是讯飞的语音听写API)

```
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '你的APPID'
API_KEY = '你的APIKEY'
SECRET_KEY = '你的密钥'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
client.asr(get_file_content(r'C:\Users\1\Music\Apowersoft\Streaming Audio Recorder\Convert\Walk as Long as You Can.wav'), 'wav', 16000, {
    'dev_pid': 1536,
})

```
运行结果：

```
'corpus_no': '6639707836891425049',
 'err_msg': 'success.',
 'err_no': 0,
 'result': ['嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯'],
 'sn': '58275652451545927448'
```

参考内容：
- [讯飞语音听写API](https://doc.xfyun.cn/rest_api/%E8%AF%AD%E9%9F%B3%E5%90%AC%E5%86%99.html)
- [使用代码情况](https://github.com/JamieYin/API_ML_AI/blob/master/%E8%AE%AF%E9%A3%9E.py)


### 使用比较分析：
- [**微软声纹识别API:**](https://azure.microsoft.com/zh-cn/services/cognitive-services/speaker-recognition/)已有相关的API调用，且有进行声纹匹配身份的API进行调用，有相关的账户即可使用，做到了100%响应时间达成率。

- [**百度声纹识别API:**](http://ai.baidu.com/docs#/ASR-API/top) 百度AI里暂没有声纹识别的功能，只有语音识别，而语音识别只是将语音转化为文本，与声纹识别差别较大。
- [**腾讯云声纹识别VPR:**](https://cloud.tencent.com/product/vpr#userDefined16) 在开发的过程中，有相关的页面内容展示，但还没可使用的API调用，还在开发中。

##### **总结**：由此可见，目前微软的声纹识别API成熟度相对于两外两者更成熟，运用案例居多，免费使用，性价比高。


### 使用后风险报告
##### 现在和未来发展趋势：
- 融合方面：
  - **验证结果更稳定**：
 单一生物特征存在可变性，如声音会随着音量、语速和音质的变化而变化，从而降低识别率，而融合验证能对各生物特征取长补短，确保稳定的识别结果。
  - **安全阈值可设置**：可根据不同的应用场景需求，选择合适的阈值，设置安全级别，能在保障校验准确度的同时有效地提高通过率。


##### 其他的优势：

1、蕴含声纹特征的语音获取方便、自然；

2、获取语音的成本低廉，使用简单，像麦克风、通讯设备等皆可；

3、适合远程身份确认；

4、声纹辨认和确认的算法复杂度低；

5、配合一些其他措施，如通过语音识别进行内容鉴别等，可以提高准确率。

虽说声纹识别发展前景不错，但也存在相关的难题。[声纹识别技术：安全指数更高但发展仍面临阻碍](http://tech.163.com/16/1205/08/C7GR92C200097U80.html)


### 四、API使用：声纹识别（说话人识别）、说话人验证、语音转文本
