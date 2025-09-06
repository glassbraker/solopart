import json
import requests
import csv
import os
import random
from datetime import datetime
import matplotlib.pyplot as plt



adata = []
with open("data/file_graphdata.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        adata.append(row)
ylength = int(adata[0][3])
del adata[0] #forgot to delete the first line -_-

#print(adata)
#import done, now converting date code to weeks
#2015-06-19T09:01:56Z'
sdate = adata[0][2]
syear = int(sdate[0:4])
smonth = int(sdate[5:7])
sday = int(sdate[8:10])
ssdate = datetime(syear, smonth, sday) # finally, start time

llength = len(adata)

while(llength > 0):
	cdate = adata[(llength - 1)][2]
	cyear = int(cdate[0:4])
	cmonth = int(cdate[5:7])
	cday = int(cdate[8:10])
	ccdate = datetime(cyear, cmonth, cday)
	#	TIME FOR MATH
	#print (ccdate)
	#print (ssdate)
	diff = ccdate - ssdate
	#print (diff.days)
	adata[(llength - 1)][2] = (diff.days // 7) # // is divide and trunk :D
	llength = llength - 1
#print(adata)
# date processing done, now need to add each uploader their own special color in dot form
#colour.append([name, r, g, b, t])
random.seed(69196454856418954)
colour = []
rr = random.randint(1, 255)
gg = random.randint(1, 255)
bb = random.randint(1, 255)
tt = rr+gg+bb
colour.append([(adata[0][0]), rr, gg, bb, tt]) #priming the list.

llength = len(adata)
while(llength > 0):
	cname = adata[(llength - 1)][0]
	lllength = len(colour)
	while(lllength > 0):
		if colour[(lllength - 1)][0] == cname:
			break
		if (lllength - 1) == 0:
			rr = random.randint(1, 255)
			gg = random.randint(1, 255)
			bb = random.randint(1, 255)
			tt = rr+gg+bb
			llllength = len(colour)
			while(llllength > 0):
				if tt >= (colour[(llllength - 1)][4] + 5) or tt<= (colour[(llllength - 1)][4] - 5):
					#print("in for statment \n")
					llllength = llllength - 1
				else:
					#print("-----------------------")
					#print(colour[(llllength - 1)][4])
					#print(tt)
					rr = random.randint(1, 255)
					gg = random.randint(1, 255)
					bb = random.randint(1, 255)
					tt = rr+gg+bb
					llllength = len(colour)
					#print(tt)
					#print("-----------------------")
					#print("in else statment \n")
			
			colour.append([cname, rr, gg, bb, tt])
		lllength = lllength - 1
	llength = llength - 1

lllength = len(colour) #scatterplot only has range from 0 to 1..... DIVIDE EVERYHTING,
while(lllength > 0):
	colour[(lllength - 1)][1] = ((colour[(lllength - 1)][1])/255)
	colour[(lllength - 1)][2] = ((colour[(lllength - 1)][2])/255)
	colour[(lllength - 1)][3] = ((colour[(lllength - 1)][3])/255)
	lllength = lllength -1

#print(colour)

xint = []
yint = []
cint = []

llength = len(adata)
x = 0
while(llength > 0):
	xint.append(x)
	x = x + 1
	llength = llength - 1
#print(xint)

'''
yint = []
y = 0
while(ylength > 0):
	yint.append(y)
	y = y + 1
	ylength = ylength - 1
print(yint)
'''
llength = len(adata)
#print("check 1")

while(llength > 0):
	#xint.append(adata[(llength-1)][1])
	yint.append(adata[(llength-1)][2])
	ccname = adata[(llength-1)][0]
	clength = len(colour)
	while(clength > 0):
		#print(ccname + "before")
		#print((colour[(lllength - 1)][0]) + "after")
		if ccname == colour[(clength - 1)][0]:
			cint.append([colour[(clength - 1)][1], colour[(clength - 1)][2], colour[(clength - 1)][3]])
			#print(colour[(lllength - 1)][0])
			clength = 1
		clength = clength - 1
	llength = llength-1
#print(len(cint))
#print(len(xint))
#print(len(yint))

#print(cint)

plt.scatter(xint, yint, c=cint, s=100)
plt.xticks(range(0,(len(xint)), 10)) 
plt.xlabel("Files")
plt.ylabel("Weeks")
#plt.title("")
plt.show()

##--------------------------other graphs
'''
xdata = []
llength = len(adata)
x = 0
while(llength > 0):
	xdata.append(adata[(llength-1)][2])
	x = x + 1
	llength = llength - 1
#print(xint)

plt.xlabel("Weeks")
plt.ylabel("Commits Added")
plt.title("Commits Histogram")
plt.hist(xdata, bins=range(min(xdata), max(xdata)+2), align='left', rwidth=1.0)
plt.show()			


odata = []
llength = len(adata)
clength = len(colour)
x = 0
while(clength > 0):
	x=0
	cname = colour[clength-1][0]
	llength = len(adata)
	while(llength > 0):
		if(adata[(llength-1)][0] == cname):
			x = x + 1
		llength = llength -1
	odata.append([cname , x])
	clength = clength-1
	
xd = []
yd = []	
olength = len(odata)
while(olength > 0):
	xd.append(odata[(olength-1)][0])
	yd.append(odata[(olength-1)][1])
	olength = olength -1

#print(yd)

plt.barh(xd, yd, color='skyblue', edgecolor='black')

# Labels
plt.title("Submission frequencies per person")
plt.xlabel("Submissions")
plt.ylabel("Names")
plt.grid(axis='x')

plt.show()





'''	

##--------------------------other graphs

	
	
