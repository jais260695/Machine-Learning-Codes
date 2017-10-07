import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import uniform

import xlrd
workbook = xlrd.open_workbook('my_file.xlsx')
worksheet = workbook.sheet_by_name('my_file_name')

price=[]
a=[]
m=[]
v=[]
e=[]

w1=(random.uniform(0.0,1.0))
w2=(random.uniform(0.0,1.0))
w3=(random.uniform(0.0,1.0))
w4=(random.uniform(0.0,1.0))
w5=(random.uniform(0.0,1.0))
w6=(random.uniform(0.0,1.0))
w7=(random.uniform(0.0,1.0))
w8=(random.uniform(0.0,1.0))
w9=(random.uniform(0.0,1.0))

rows = (int)(worksheet.nrows*0.8)
for i in range(1,(int)((worksheet.nrows)*0.8)):
    price.append((float)(worksheet.cell(rows-i, 0).value))

norm_val=max(price)
w=[]
#column = worksheet.ncols

for i in range(1,rows):

    a.append((worksheet.cell(rows-i, 0).value)/norm_val)
    m1=0.0
    for j in range(rows-i,rows-(i+10)):
        m1=m1+(worksheet.cell(j, 0).value)/norm_val
    m1=m1/10
    m.append(m1)
    
    v1=0.0
    for k in range(rows-i,rows-(i+10)):
        v1=v1+(((worksheet.cell(k, 0).value)/norm_val - m1)**2)
    v.append(v1/10)

for i in range(len(a)):
    result=(a[i]*w1)+(math.sin(a[i])*w2)+(math.cos(a[i])*w3)+(m[i]*w4)+(math.sin(m[i])*w5)+(math.cos(m[i])*w6)+(v[i]*w7)+(math.sin(v[i])*w8)+(math.cos(v[i])*w9)
    error=(worksheet.cell(i+11, 0).value)/norm_val - result
    w=[]
    w1=w1+2*0.8*error*a[i]
    w.append(w1)
    w2=w2+2*0.8*error*(math.sin(a[i]))
    w.append(w2)
    w3=w3+2*0.8*error*(math.cos(a[i]))
    w.append(w3)
    w4=w4+2*0.8*error*m[i]
    w.append(w4)
    w5=w5+2*0.8*error*(math.sin(m[i]))
    w.append(w5)
    w6=w6+2*0.8*error*(math.cos(m[i]))
    w.append(w6)
    w7=w7+2*0.8*error*v[i]
    w.append(w7)
    w8=w8+2*0.8*error*(math.sin(v[i]))
    w.append(w8)
    w9=w9+2*0.8*error*(math.cos(v[i]))
    w.append(w9)
    max_wgt=max(w)
    w1=w1/max_wgt
    w2=w2/max_wgt
    w3=w3/max_wgt
    w4=w4/max_wgt
    w5=w5/max_wgt
    w6=w6/max_wgt
    w7=w7/max_wgt
    w8=w8/max_wgt
    w9=w9/max_wgt
    e.append(error)
print(e)
print(w1,w2,w3,w4,w5,w6,w7,w8,w9)



         

    
