



import requests
#print( requests.get('http://ya.ru').text)

# cd foldr
# python request.py






"""
f = requests.get('https://stepic.org/media/attachments/course67/3.6.2/603.txt').text




print(sum(1 for _ in f))
print(len(f.splitlines()))

with open('/home/kde/Загрузки/dataset_3363_4.txt') as f:
    print(sum(1 for _ in f))


"""

f1 = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt').text
f1 = requests.get('https://stepic.org/media/attachments/course67/3.6.3/843785.txt').text
f1 = requests.get('https://stepic.org/media/attachments/course67/3.6.3/987573.txt').text

print(f1)

i = 0
import time


while i < 10:
	i += 1
	try:
		print(">"+f1)
		time.sleep(3)
		f1 = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+f1).text
	except:
		print("*"+f1)





