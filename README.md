# API_ML_AI
## PRD:
### 价值宣言：
一般宿舍进出入门口都以人脸识别为核心，产品的价值在于可提供声纹识别进行验证，进一步拓展至通关密语和社交交互（语音转文本留言）。
### 核心价值：
最小可用产品是实现声纹识别，通过用户的声音检测是否本人来进出入宿舍门口；可通过通关密语进入宿舍，也可以用声音转化为文本留言进行社交。
### 核心价值与用户痛点：
- 用户在没有多余的手开门时，可以通过声控开门。
- 用户无需掏出饭卡/身份证进行识别，更加便捷。
- 用户在外出的时候，隔壁邻居可以留言。
### 人工智能概率论与用户痛点：
使用声纹识别结合其他生物识别作为门禁系统的开锁方式，可实现无需携带任何物品的验证流程，解决用户处于无手开门的痛点出现。

科大讯飞于2010年率先对外发布语音云，语音合成、语音识别、口语评测、自然语言处理等多项人工智能技术均代表世界最高水平。早在2014年10月，科大讯飞的声纹识别技术就已经加入到了讯飞的开放平台。

据了解，目前语音听写识别率现在已经达到了97%，人脸识别已经到了99%，语音唤醒95%，自然度已经超过普通人，语音云的应用数超过30万，活跃终端数10亿以上。同时科大讯飞还有智能硬件业务部，包括语音能力，集成商、硬件商。据张良春介绍：“科大讯飞的声纹识别技术，可以在未声纹注册情况下，可识别性别和年龄段；合音效果是非常出色，EER小于2%；鉴别范围比较广，可以达到10个人复杂场景下依然可以有效识别；分布式声纹库，离线情况下也可以使用。”
相应资料：[2017生物识别论坛：深耕智能家居市场，科大讯飞发布远场声纹识别技术](https://baijiahao.baidu.com/s?id=1577429457128771788&wfr=spider&for=pc)[「致敬40年」科大讯飞刘庆峰：这件事我们坚持了19年，终于做到了](https://baijiahao.baidu.com/s?id=1620427567388903097&wfr=spider&for=pc)

### 需求列表与人工智能API:

Title | User story | importance | Notes | API
---|---|--------|------|-----
声控开门 | 用户在没有多余的手开门的时候，可以通过声音识别从而开门 | 重要 | 声纹识别 | 声纹识别API
密令 | 用户通过设定的通关密语验证卡门 | 重要 | 通关密语 | 说话人验证API
留言 | 用户在外出的情况下，隔壁邻居可以通过声音留言 | 次要 | 语音转文本 | 语音转写API

## 原型：
### 交互及界面设计：
![图片](https://github.com/JamieYin/API_ML_AI/blob/master/img/appuse1.jpg)

![图片](https://github.com/JamieYin/API_ML_AI/blob/master/img/appuse2.jpg)

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
1. **核心功能：声纹识别**，（Voiceprint Recognize），是一项提取说话人声音特征和说话内容信息，自动核验说话人身份的技术。MSC SDK 声纹识别（IdentityVerfier）的使用包括注册（训练）、验证和模型操作。类似于一个网站的用户登录一样，用户必须先注册，才能登录（验证），在用户忘记密码时，可以提供重设密码的操作（模型操作）。

  - 声纹注册（目前 MSC SDK 支持两种类型的声纹密码：数字密码和文本密码。文本密码的效果在优化中，建议使用数字密码。密码类型的取值说明如下表所示：[详情sdk](https://doc.xfyun.cn/msc_android/index.html)
  

取值 |说明
---|---
 1 | 文本密码。用户通过读出指定的文本内容来进行声纹注册和验证，现阶段不支持。
2| 自由说。用户通过录入一段任意20s以上音频进行注册，验证时录入任意5s以上音频即可完成验证，现阶段不支持。
3 | 数字密码。从云端拉取若干组特定的数字串（默认有5组，每组8位数字），用户依次读出这5组数字进行注册，在验证过程中会生成一串特定的数字，用户通过读出这串数字进行验证。
注册时使用的密码通过调用 getPasswordList 方法获取：
```
// 设置会话场景
mIdVerifier.setParameter(SpeechConstant.MFV_SCENES, "ivp");

// 子业务执行参数，若无可以传空字符传
StringBuffer params = new StringBuffer();
// 设置模型操作的密码类型
params.append("pwdt=" + mPwdType + ",");
// 执行密码下载操作
mIdVerifier.execute("ivp", "download", params.toString(), mDownloadPwdListener);
```
通过 mDownloadPwdListener 回调中获取的密码，进行声纹注册。

```
// 设置会话场景
mIdVerifier.setParameter(SpeechConstant.MFV_SCENES, "ivp");
// 设置会话类型
mIdVerifier.setParameter(SpeechConstant.MFV_SST, "enroll");
// 设置训练次数(可以不做设置，sdk中默认设置为5次)
mIdVerifier.setParameter(SpeechConstant.MFV_RGN, "5");
// 用户id
mIdVerifier.setParameter(SpeechConstant.AUTH_ID, authid);
// 设置监听器，开始会话
mIdVerifier.startWorking(mEnrollListener);
```
声纹结果：

```
{
    "ret": 0,
    "group_id": "xxxxxx",
    "group_name": "xxxxxx",
    "ifv_result": {
        "candidates": [
            {
                "model_id": "xxxxxxxx",
                "decision": "accepted",
                "score": 88.888888,
                "user": "user_name"
            }
        ]
    },
    "sst": "identify",
    "ssub": "ivp",
    "topc": 1
}
```

**2. 通关密语API(说话人验证)**
- 注册：
演讲者验证的注册与文本有关，这意味着演讲者需要选择在注册和验证阶段使用的特定密码短语。

- 在登记中，记录说话者的语音，说出特定短语，然后提取许多特征并识别所选择的短语。所有提取的特征和所选择的短语一起形成独特的语音签名。

- 验证：
在验证中，将输入语音和短语与登记的语音签名和短语进行比较 - 以便验证他们是否来自同一个人，以及他们是否说出正确的短语。

示例操作：[Speaker Recognition API（运用的是微软说话人验证API）](https://westus.dev.cognitive.microsoft.com/docs/services/563309b6778daf02acc0a508/operations/5645c3271984551c84ec6797)

**3. 留言消息（语音转文本）**

代码示例：（运用的是讯飞的语音转写API)

```
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '15289844'
API_KEY = 'WSnyOreo4uh89LLmrfSvGNIo'
SECRET_KEY = '2VUdjOTPk2tZ9qMqPABn3DZIqmGCAc6L'

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
{'corpus_no': '6639707836891425049',
 'err_msg': 'success.',
 'err_no': 0,
 'result': ['嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯'],
 'sn': '58275652451545927448'}
```
[使用讯飞API-python调用](https://github.com/JamieYin/API_ML_AI/blob/master/%E8%AE%AF%E9%A3%9E.py)

### 使用比较分析：
- [**讯飞声纹识别API:**](https://www.xfyun.cn/services/isv)
已有相关的SDK下载调用，免费试用，成熟度高：响应时间：注册—500ms，验证—900ms；已经应用于考勤系统、远程认证、门禁系统、娱乐应用领域上。
- [**百度声纹识别API:**](http://ai.baidu.com/docs#/ASR-API/top) 百度AI里暂没有声纹识别的功能，只有语音识别，而语音识别只是将语音转化为文本，与声纹识别差别较大。
- [**腾讯云声纹识别VPR:**](https://cloud.tencent.com/product/vpr#userDefined16) 在开发的过程中，有相关的页面内容展示。

##### **总结**：由此可见，目前讯飞的声纹识别API成熟度相对于两外两者更成熟，运用案例居多，免费使用，性价比高。


### 使用后风险报告
##### 现在和未来发展趋势：
- 融合方面：
  - **验证结果更稳定**：
 单一生物特征存在可变性，如声音会随着音量、语速和音质的变化而变化，从而降低识别率，而融合验证能对各生物特征取长补短，确保稳定的识别结果。
  - **安全阈值可设置**：可根据不同的应用场景需求，选择合适的阈值，设置安全级别，能在保障校验准确度的同时有效地提高通过率。
  
- SDK方面
  - **集成方式灵活**：应用可以根据需求灵活选择生物特征，实现需要的服务能力。

  - **接入方式统一**：一套接口实现多种生物特征的接入，维护方便，同时后期新的生物特征接入，SDK无需重新集成即可使用。

  - **数据传输可靠**：通过对数据通道加密，以及与三方业务服务器的闭环校验策略，有效解决客户端数据的挟持问题。

##### 其他的优势：

1、蕴含声纹特征的语音获取方便、自然；

2、获取语音的成本低廉，使用简单，像麦克风、通讯设备等皆可；

3、适合远程身份确认；

4、声纹辨认和确认的算法复杂度低；

5、配合一些其他措施，如通过语音识别进行内容鉴别等，可以提高准确率。

虽说声纹识别发展前景不错，但也存在相关的难题。[声纹识别技术：安全指数更高但发展仍面临阻碍](http://tech.163.com/16/1205/08/C7GR92C200097U80.html)

###### 操作声纹都是很简单直接的。因此，有些安全性也是应用应该考虑的：

- 更新模型： 应用在给用户更新声纹模型等操作时，为了安全性，应该考虑必要的验证，如，必须先通过声纹密码或应用登录密码验证，才能进行下一步更新声纹模型（重新注册）——类似修改密码时，必须先进行安全性验证一样。

- APPID： 从前面的特征可以看到，如果 APPID 与 libmsc.so 泄漏后，使用这个 APPID 和 libmsc.so 就可以绕过应用层的安全验证，操作该 APPID 的所有用户ID的模型。所以，应用的 APPID 须保证不泄漏给他人——如不要以明文方式在代码中以字符串保存；在论坛发帖求助时，不要在所有浏览者都可见的正文中带 APPID 内容等。

- 用户ID： SDK 对通过验证 APPID 的应用，只要指定用户 ID 就可以进行更新模型操作（先删除，再注册，或注册时指定替换）。所以，应用应当考虑用户可能会恶意指定他人的用户 ID，进行注册或验证的情况。应用可以在展示给用户的账号和用来注册 MSC SDK 声纹的用户 ID 间，做一层映射，使用户无法直接看到或猜测到实际用于 MSC SDK 声纹时的用户 ID 值；同时，应用在用户操作声纹密码的页面中，应尽可能的把账号设置为只读——避免恶意修改他人账号声纹密码的情况。

- 验证密码： 因为人的声音是可以录制下来的，当验证的密码固定不变时，用户的声音就比较大可能被别人录制下来，然后再次用来验证——在密码相同时。所以，用来验证的密码时，每次都不一样时，安全性可以更大的提搞——随机数字密码，比固定文本密码更安全。同时，也应该提醒用户，在注意声音的泄漏或被盗用——如留意不要随意输入银行卡密码一样。

- 1:N检索： 鉴别与验证的过程相似，不过鉴别需要设置组 ID，以指定要鉴别的组。 

### 四、API使用：声纹识别、说话人验证、语音转文本
