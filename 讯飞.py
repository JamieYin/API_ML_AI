
# coding: utf-8

# In[2]:

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '你的APPID'
API_KEY = '你的APIKEY'
SECRET_KEY = '你的密钥'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)



# In[13]:

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
client.asr(get_file_content(r'C:\Users\1\Music\Apowersoft\Streaming Audio Recorder\Convert\Walk as Long as You Can.wav'), 'wav', 16000, {
    'dev_pid': 1536,
})


# In[ ]:




# In[ ]:




# In[ ]:



