from pydub import AudioSegment
import os, re


count = 1 #start from 2 in for-loop

dir = "./Unit10"

print(len(os.listdir(dir)))

allSong = AudioSegment.from_mp3(dir + "/1.mp3")
fiveSecBlank = AudioSegment.from_mp3("blank.mp3") # 5 sec blank
endListening = AudioSegment.from_mp3("end_listening.mp3") # End of Listening
dbAllSong = allSong.dBFS

for each in os.listdir(dir):
	count = count + 1
	if count >= len(os.listdir(dir)) :
		break;
	filename = dir + "/" + str(count) + ".mp3"
	if filename:
		print("Adding " + filename)
		song = AudioSegment.from_mp3(filename)
		dbSong = song.dBFS
		dbplus = dbAllSong - dbSong
		if dbplus < 0:
			dbAllSong+=abs(dbplus)
		elif dbplus > 0:
			dbSong+=abs(dbplus)
		allSong = allSong + fiveSecBlank + song

print ("Add Ending")
allSong = allSong + fiveSecBlank + endListening

allSong.export(dir + "/Unit1.mp3", format="mp3") #导出为MP3格式
print ("End Generating")

"""
filename[0] += '.mp3'
mp3 = AudioSegment.from_mp3(filename[0]) # 打开mp3文件
mp3[17*1000+500:].export(filename[0], format="mp3") # 切割前17.5秒并覆盖保存


nPath = "%s%s/%s"%(enDir,file,enfile) #英文文件的路径
cnPath = "%s%s/%s"%(cnDir,file,enfile.replace("en_w","cn_w"))#中文文件的路径
targetPath = "%s%s/%s"%(toDir,file,enfile.replace("en_w","all")) #合并文件的路径

#加载MP3文件
song1 = AudioSegment.from_mp3(enPath)
song2 = AudioSegment.from_mp3(cnPath)
 
#取得两个MP3文件的声音分贝
db1 = song1.dBFS
db2 = song2.dBFS
 
song1 = song1[300:] #从300ms开始截取英文MP3
 
#调整两个MP3的声音大小，防止出现一个声音大一个声音小的情况
dbplus = db1 - db2
if dbplus < 0: # song1的声音更小
    song1+=abs(dbplus)
elif dbplus > 0: #song2的声音更小
    song2+=abs(dbplus)
 
#拼接两个音频文件
song = song1 + song2
 
#导出音频文件
song.export(targetPath, format="mp3") #导出为MP3格式"""