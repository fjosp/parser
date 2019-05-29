from bs4 import BeautifulSoup
import xlwt
from datetime import datetime
import time
from textblob import TextBlob

#~ names_dick={
			#~ "I0":"Agriculture",
			#~ "iaut":"Automotive",
			#~ "ibasicm":"Basic Materials/Resources",
			#~ "ibcs":"Business/Consumer Services",
			#~ "icnp":"Consumer Goods",
			#~ "i1":"Energy",
			#~ "ifinal":"Financial Services",
			#~ "i951":"Health Care/Life Sciences",
			#~ "iindstrls":"Industrial Goods",
			#~ "ilea":"Leisure/Arts/Hospitality",
			#~ "imed":"Media/Entertainment",
			#~ "icre":"Real Estate/Construction",
			#~ "i64":"Retail/Wholesale",
			#~ "itech":"Technology",
			#~ "i7902":"Telecommunication Services ",
			#~ "itsp":"Transportation/Logistics",
			#~ "iutil":"Utilities"
			#~ }
#~ sources=   {
			#~ "TDJW":"Dow Jones Newswires",
			#~ "TMNB":"Major News and Business Sources",
			#~ "TPRW":"Press Release Wires",
			#~ "TRTW":"Reuters Newswires",
			#~ "SFWSJ":"The Wall Street Journal - All sources",
			#~ "others":"All other sources"
			#~ }

			
			#~ "I0",
			#~ "iaut",
			#~ "ibasicm",
			#~ "ibcs",
			#~ "icnp",
			#~ "i1",
			#~ "ifinal",
			#~ "i951",
			#~ "iindstrls",
			#~ "ilea",
			#~ "imed",
			#~ "icre",
			#~ "i64",
			#~ "itech",
			#~ "i7902",
			#~ "itsp",


			
			#~ "TDJW",
			#~ "TMNB",
			#~ "TPRW",
			#~ "SFWSJ",
			#~ "others"

industries=["I0",
			"iaut",
			"ibasicm",
			"ibcs",
			"icnp",
			"i1",
			"ifinal",
			"i951",
			"iindstrls",
			"ilea",
			"imed",
			"icre",
			"i64",
			"itech",
			"i7902",
			"itsp",
			"iutil"
			]
			
sources=   ["TRTW",
			"TDJW",
			"TMNB",
			"TPRW",
			"SFWSJ",
			"others"]


wb = xlwt.Workbook()
ws = wb.add_sheet("MEGA SHEET")

n=0

titles=[]
f=open("mega.csv","w")
for name_ind in industries:
	print(name_ind)
	for name_source in sources:
		#~ headline=["Title","Publisher","Date","Words"]
		#~ for title in headline:ws.write(0,headline.index(title),title)
		name="{}_{}".format(name_ind,name_source)
		
		html_doc = open("{}.html".format(name),"rb")

		#~ soup = BeautifulSoup(html_doc, 'html.parser')
		try:
			soup = BeautifulSoup(html_doc, 'html.parser')
		except:
			print("ERROR WITH {}".format(name))
			time.sleep(5)
			break
		headlines=soup.find_all(class_="enHeadline")
		leadfields=soup.find_all(class_="leadFields")
		count=soup.find_all(class_="count")
		
		#~ print(len(headlines),len(leadfields))
		
		for line in headlines:
			title=line.get_text()
			#~ print(title)
			
			
		#~ for i in leadfields:
			i=leadfields[headlines.index(line)]
			attributes=i.get_text()
			#~ print(i)
			hh=str(count[headlines.index(line)].get_text())
			mm=hh.replace(u'\xa0', u'').split('.')
			#~ print(hh.replace(u'\xa0', u'').split('.'))
			if not bool(mm[1]):
				lib=attributes.split(",")
				#~ print(lib)
				if ":" in lib[1] or lib[1][1] not in ['0','1','2','3','4','5','6','7','8','9']:
					date=lib[2]
					words=lib[3]
				else:
					date=lib[1]
					words=lib[2]
				
				if title not in titles:
					title= title.replace(';', ' ')
					title= title.replace('\n', '')
					titles.append(title)
					b=TextBlob(str(title))
					f.write(mm[0]+";"+str(date)+";"+str(name)+";"+str(title)+";"+str(b.sentiment.polarity)+"\n")
				else:
					n=n+1
					print(n)
					#~ print(date,";",name)
			
	#~ ws.write(row_b,3,words)
	#~ wb.save(name_ind+".xls")
