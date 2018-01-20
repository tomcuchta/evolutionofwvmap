#!/usr/bin/python

import shapefile as shp
import matplotlib.pyplot as plt
#import matplotlib.patches as patches
import textwrap
import numpy as np
badindices=range(0,13)+[14,16,21,22,25,28,29]+range(32,45)+[46,51,52,53]+range(69,78)+[84,87,88,89,90,126,133,184,185,189,191,193,199,211,243,244,245,253,270,271,288,297,298,299,314,403]+[213,219,231,320,323,376,447,459]+[340,388,413,455,461,492,501,522,533,539,549,568,576,581,590,596,617,622,628,633,644,649,669]

textwraplength=23

#This function is used as the key defining recsorted
def outputshapedate(shape):
	return shape.record[5]

def plotshape(kvalue,fillcolor,alphaval=1.0):
	x = [j[0] for j in recsorted[kvalue].shape.points[:]]
	y = [j[1] for j in recsorted[kvalue].shape.points[:]]
	plt.fill(x,y,color=fillcolor,zorder=kvalue,alpha=alphaval)
	plt.plot(x,y,color="Black",zorder=kvalue,linewidth=1.5)

def month(num):
	if(num==1):
		return "January"
	elif(num==2):
		return "February"
	elif(num==3):
		return "March"
	elif(num==4):
		return "April"
	elif(num==5):
		return "May"
	elif(num==6):
		return "June"
	elif(num==7):
		return "July"
	elif(num==8):
		return "August"
	elif(num==9):
		return "September"
	elif(num==10):
		return "October"
	elif(num==11):
		return "November"
	elif(num==12):
		return "December"
	else:
		return "E R R O R"

def pad_left(n,width,pad="0"):
        return ((pad*width)+str(n))[-width:]

sf = shp.Reader("vawvmerge.shp")
recinfo=[]
	
for shape in sf.shapeRecords():
	recinfo.append(shape)

recsorted=sorted(recinfo, key=outputshapedate)

#iterator for rows in the data set
k=0
#iterator for filename
j=0

while(k<len(recinfo)):
	print k
	fig = plt.figure()
	plt.fill([-85,-85,-82.7,-82.7],[36.5,41,41,36.5],color="White",zorder=999)
	plt.axis('off')


	plt.axes().set_aspect('equal')	
	plt.xlim(-85,-76.89)
	plt.ylim(36.5,41)

	m=0
	while(m<k):
		if("lost to" not in recsorted[m].record[7] and "independent city" not in recsorted[m].record[7] and "Independent city" not in recsorted[m].record[7] and m not in badindices or m in [213,219,220,231,232,238, 239, 241,319,320,323,324,376,377,447,448,459,460,669,670,724]):
			plotshape(m,"Blue")
			if(k>665 and recsorted[m].record[2]=="WV"):
				plotshape(m,"#00B140")				
			if(k>665 and recsorted[m].record[2]=="VA"):
				plotshape(m,"Gray")
		m+=1

#	if(k>220):
#		plotshape(219,"Blue")
#		plotshape(220,"Blue")
	if(k>665):
		plotshape(220,"Gray")
	if(k>238):
		plotshape(206,"Gray")
	if(k>240):
		plotshape(229,"Blue")
	if(k>241):
		plotshape(204,"Gray")
		plotshape(205,"Gray")	
		plotshape(238,"Blue")
		plotshape(236,"Gray")
		plotshape(239,"Blue")
		plotshape(241,"Blue")
		if(k>665):
			plotshape(241,"#00B140")


	if("lost to" not in recsorted[k].record[7] and "independent city" not in recsorted[m].record[7] and "Independent city" not in recsorted[m].record[7] and k not in badindices or k in [238, 239, 241,724]):
		plotshape(k,"Red")

#Exchange between STAFFORD and KING GEORGE occurs with k=213 and k=214
#Make both red
		if(k==214):
			plotshape(213,"Red")
			plotshape(214,"Red")
#Exchange between MONTGOMERY and WASHINGTON occurs with k=219 and k=220
#Make both red
		if(k==220):
			plotshape(219,"Red")
			plotshape(219,"Red")
#Exchange between WESTMORELAND and KING GEORGE occurs with k=231 and k=232
#Make both red
		if(k==232):
			plotshape(231,"Red")
			plotshape(232,"Red")
#Exchange between BOTETOURT and MONTGOMERY occurs with k=319 and k=320
#Make both red
		if(k==319):
			plotshape(319,"Red")
			plotshape(320,"Red")
#Exchange between BOTETOURT and MONTGOMERY occurs with k=323 and k=324
#Make both red
		if(k==324):
			plotshape(323,"Red")
			plotshape(324,"Red")
#Exchange between KANAWHA and MASON occurs with k=376 and k=377
#Make both red
		if(k==377):
			plotshape(376,"Red")
			plotshape(377,"Red")
#Exchange between GREENBRIAR and FAYETTE occurs with k=447 and k=448
#Make both red
		if(k==448):
			plotshape(447,"Red")
			plotshape(448,"Red")
#Exchange between RUSSELL and TAZEWELL occurs with k=459 and k=460
#Make both red
		if(k==460):
			plotshape(459,"Red")
			plotshape(460,"Red")
#Exchange between RANDOLPH and UPSHUR
#Make both red
		if(k==670):
			plotshape(669,"Red")
			plotshape(670,"Red")
#ILLINOIS should be gray after 29 February 1784 (because of the creation of the Northwest Territoy (https://en.wikipedia.org/wiki/Illinois_County,_Virginia) 
#The k-vaulue for ILLINOIS is k=235.
#We have k=249 being 1 February 1782 and k=251 being 20 July 1784 
#So force ILLINOIS gray on and after k=251
		if(k>=251):
			plotshape(235,"Gray")
#Kentucky should be gray after 1 June 1792. We have k=308 being 30 November 1791 and k=309 being 1 May 1793. 
#The counties we observe in Kentucky are FAYETTE (k=242), BOURBON (k=266), MASON (k=287).
#Therefore k=242, 266, and 287 should be grayed at and pas k=309.
		if(k>=309):
			plotshape(242,"Gray")
			plotshape(266,"Gray")
			plotshape(287,"Gray")
#Pennsylvania should be gray starting with k=238
#The part that needs to be gray is the shape k=201 set minus minus k=204, 205, 238, 239,241
#Also relevant are MONONGALIA county k=204 and OHIO county k=205
		if(k==238):
			plotshape(201,"Gray")
			plotshape(204,"Blue")
			plotshape(205,"Blue")
			plotshape(238,"Red")
		if(k==239):
			plotshape(201,"Gray")
			plotshape(204,"Blue")
			plotshape(205,"Gray")
			plotshape(238,"Blue")
			plotshape(239,"Red")	
		if(k==240):
			plotshape(201,"Gray")
			plotshape(204,"Blue")
			plotshape(205,"Gray")
			plotshape(238,"Blue")
			plotshape(239,"Red"),
		if(k==241):
			plotshape(201,"Gray")
			plotshape(204,"Gray")
			plotshape(205,"Gray")
			plotshape(238,"Blue")
			plotshape(236,"Gray")
			plotshape(239,"Blue")
			plotshape(241,"Red")

#
# Berkeley k=195
# jefferson k=342
# in limbo from statehood til 6 March 1871
# k=709 is the first frame after Virginia v West Virginia (https://en.wikipedia.org/wiki/Virginia_v._West_Virginia)
#
		if(k>665 and k<709):
			plotshape(195,"White")
			plotshape(342,"White")

			plotshape(195,"#00B140",0.5)
			plotshape(342,"#00B140",0.5)
# Final slide, don't let that last VA county turn red so we get a nice final frame of WV.
		if(k==724):
			plotshape(724,"Gray")


#Write the date for all but the last slide
		if(k!=724):
			plt.text(-85.5,40.5,str(recsorted[k].record[5][2])+" "+month(recsorted[k].record[5][1])+" "+str(recsorted[k].record[5][0]),backgroundcolor='1',zorder=99999999,fontsize=15)
#Write the documentation for the change for all but the last slide
			changedescription=textwrap.wrap(recsorted[k].record[7],textwraplength)
			changeiterator=0
			while(changeiterator<len(changedescription)):
				plt.text(-85.5,39.9-changeiterator*0.3,changedescription[changeiterator], fontsize=10, zorder=999999999, backgroundcolor='1')

				changeiterator+=1

#Save it!
#		plt.savefig(pad_left(j,4)+".png",bbox_inches='tight', pad_inches=0)	
		plt.savefig(pad_left(k,4)+".png",bbox_inches='tight', pad_inches=0, dpi=666)	

		j+=1	
	
	plt.close()
	k+=1
