import xlwt
from datetime import datetime
import time

dick={'January':'jan',
	'February':'feb',
	'March':'mar',
	'April':'apr',
	'May':'may',
	'June':'jun',
	'July':'jul',
	'August':'aug',
	'September':'sep',
	'October':'oct',
	'November':'nov',
	'December':'dec'
	}

dick1={'01':'jan',
	'02':'feb',
	'03':'mar',
	'04':'apr',
	'05':'may',
	'06':'jun',
	'07':'jul',
	'08':'aug',
	'09':'sep',
	'10':'oct',
	'11':'nov',
	'12':'dec'
	}

f=open('DJI.csv', 'r', encoding="utf-8")
new=open("timeline_new.csv","w")
for line in f:
	l=line.split(';')
	#~ f.write(mm[0]+";"+str(date)+";"+str(name)+";"+str(title)+";"+str(b.sentiment.polarity)+"\n")
	#~ print(l)
	dat=l[0].split('.')
	print(dat)
	#~ if len(dat[0])==1:
		#~ dat[0]=str('0'+dat[0])
	dat[1]=dick1[str(dat[1])]
	print(dat)
	new_dat=dat[0]+dat[1]+dat[2]
	new.write(new_dat+";"+"1"+"\n")


