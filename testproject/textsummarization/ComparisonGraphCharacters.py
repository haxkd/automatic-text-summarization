import matplotlib.pyplot as plt
import numpy as np
import csv 
from django.conf import settings
dir = settings.STATICFILES_DIRS[0]

def compareByChar():
    w = 4
    h = 4
    d = 100
    plt.figure(figsize=(w, h), dpi=d)

    lsa=[]
    lexrank=[]
    tf_idf=[]
    kl_sum=[]
    x1 = []
    y1 = []

    x2 = []
    y2 = []

    x3 = []
    y3 = []

    x4 = []
    y4 = []
    with open(str(dir)+'/lsa.csv','rt') as csvfile: 
        reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
        for row in reader:
            lsa.append(row)
        
        for data in lsa:
            x1.append(int(data[0]))
            y1.append(float(data[2]))
            
        x1.sort()
        y1.sort()
        
        
    with open(str(dir)+'/lexrank.csv','rt') as csvfile: 
        reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
        for row in reader:
            lexrank.append(row)
        
        for data in lexrank:
            x2.append(int(data[0]))
            y2.append(float(data[2]))
        
        x2.sort()
        y2.sort()
        
    
    with open(str(dir)+'/TF-IDF.csv','rt') as csvfile: 
        reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
        for row in reader:
            tf_idf.append(row)
        
        for data in tf_idf:
            x3.append(int(data[0]))
            y3.append(float(data[2]))
        
        x3.sort()
        y3.sort()

    with open(str(dir)+'/KL-Sum.csv','rt') as csvfile: 
        reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
        for row in reader:
            kl_sum.append(row)
        
        for data in kl_sum:
            x4.append(int(data[0]))
            y4.append(float(data[2]))
        
        x4.sort()
        y4.sort()
        
    plt.title("Text Summarization Algorithms Character Count - Time Comparison")
    plt.xlim([0, 2000])
    plt.ylim([0, 10])
    plt.xticks(np.arange(0, 2000, 100))
    plt.yticks(np.arange(0, 10, 0.50))
    plt.plot(x1,y1,marker='o',linewidth=3)
    plt.plot(x2,y2,marker='o',linewidth=3)
    plt.plot(x3,y3,marker='o',linewidth=3)
    plt.plot(x4,y4,marker='o',linewidth=3)
    plt.xlabel("Character Count")
    plt.ylabel("Time Taken")
    plt.legend(["LSA", "LEXRANK", "TF-IDF","KL-SUM"])
    # plt.show()
    plt.gcf().set_size_inches(10,5)
    plt.savefig(str(dir)+"\Character_Count_Comparison.png",dpi=300)
    # plt.savefig