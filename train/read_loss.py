

import numpy as np
import math 
from matplotlib import pyplot as plt 



for index in range(1): 
    file="./L1.txt"
    f=open(file,"r")
    lines=f.readlines()
    x = []
    #z = []
    #theta = [] 
    result=[]
    drag = []
    drag_visc = []
    i=0
    for xline in lines:
        if i>=1:
#           tempx=(float(xline.split()[0]))
           temp_result=(float(xline.split()[0]))
           #temp2_result=(float(xline.split()[4]))
           #temp3_result=(float(xline.split()[7]))
           #x.append(tempx)
           x.append(i)
           result.append(temp_result)
    #       tempz=(float(xline.split()[5]))
    #       tempr = math.sqrt(tempx*tempx + tempz*tempz)
    #       temptheta = math.asin(tempz/tempr)*180/math.pi
    #       if tempx<=0:
    #           theta.append(temptheta)
    #           z.append(tempz)
    #           temp_result=(float(xline.split()[9]))*p_1/pt_f
    #           result.append(temp_result)
        i=i+1
    f.close()
    plt.figure()
    plt.plot(x,result,label="Loss")
    #plt.ylim(0.4,0.65)
    plt.legend()
    



for index in range(1): 
    file="./L1val.txt"
    f=open(file,"r")
    lines=f.readlines()
    x = []
    #z = []
    #theta = [] 
    result=[]
    drag = []
    drag_visc = []
    i=0
    for xline in lines:
        if i>=1:
#           tempx=(float(xline.split()[0]))
           temp_result=(float(xline.split()[0]))
           #temp2_result=(float(xline.split()[4]))
           #temp3_result=(float(xline.split()[7]))
           #x.append(tempx)
           x.append(i)
           result.append(temp_result)
    #       tempz=(float(xline.split()[5]))
    #       tempr = math.sqrt(tempx*tempx + tempz*tempz)
    #       temptheta = math.asin(tempz/tempr)*180/math.pi
    #       if tempx<=0:
    #           theta.append(temptheta)
    #           z.append(tempz)
    #           temp_result=(float(xline.split()[9]))*p_1/pt_f
    #           result.append(temp_result)
        i=i+1
    f.close()
#    plt.figure()
    plt.plot(x,result,label="Loss val.")
    #plt.ylim(0.4,0.65)
    plt.legend()
    


plt.xlim(-5,550)
plt.ylim(0,0.025)



plt.xlabel(r'Epochs', fontsize=14)
plt.ylabel(r'Loss', fontsize=14)
plt.savefig('Loss_Re1.eps', format='eps', dpi=1200)
#print [x.split(' ')[1] for xline in open(file).readlines()]
plt.show()





