from logging import makeLogRecord
from tokenize import PlainToken
import matplotlib.pyplot as plt


prize=[13,5,7,14,10,12]
x=[0,1,2,3,4,5]
month=["Jan", "Feb", "March", "April", "May", "June"]
plt.plot(month,prize,lw=2,ms=10,marker="o")
plt.xticks(x,month)
plt.yticks([0,5,10,15])
plt.title("Print Sales for January to June, 2022")
plt.xlabel("Month")
plt.ylabel("Monthly Sales ($1000)")
plt.rc('font', size=14)
plt.rc('figure', titlesize=16)
plt.xlim(0,5)
plt.show()