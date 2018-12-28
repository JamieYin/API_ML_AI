
# coding: utf-8

# In[2]:

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '15289844'
API_KEY = 'WSnyOreo4uh89LLmrfSvGNIo'
SECRET_KEY = '2VUdjOTPk2tZ9qMqPABn3DZIqmGCAc6L'

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



