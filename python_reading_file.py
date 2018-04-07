#python reading file

import urllib 
import urllib2 
import requests
import os  

"""path = "./list2"
files= os.listdir(path) #Get all file names  
s = []  
for file in files: #Go throught the folder
     if not os.path.isdir(file):
          f = open(path+"/"+file); #Open a file
          iter_f = iter(f); #Create iterator
           #readline of the file
          for line in iter_f:"""

file = open("./list/Unit8.tsv")
count = 0

for line in file:
	count = count + 1
	singleWord = line.split("\t")[0]
	print (str(count) + " " + singleWord)

	try:
		url = "http://media.shanbay.com/audio/us/" + singleWord +".mp3"  
		req2 = urllib2.Request(url)
		response = urllib2.urlopen(req2)
		#grab the data
		data = response.read()
		mp3Name = str(count) + ".mp3"
		song = open(mp3Name, "wb")
		song.write(data)    # was data2
		song.close()
	except urllib2.HTTPError:
		print "Error: HTTP Error"
