FIELD_IP = '172.27.22.45'#ip will change according to Virtual Machines IP's
FIELD_PORT = 6060

SIM_TIME = 100
#SIM_STEP = 0.1
#Process Variables

LL  = 0
V1_1= 1
V1_2= 2
P   = 3
L1  = 4
T1  = 5
H   = 6
V2  = 7
L2  = 8
L2L = 9
heat_coefficient = 200
heat_coefficient_2 = 50

def printvalues(mode, LL, V1_1, V1_2, P, L1, T1, H, V2, L2L):
    st =   (mode+",\t" 
           
            "LL: "+str("{0:.4f}".format(LL))+",\t"
            "V1_1: "+str("{0:.4f}".format(V1_1))+",\t"
            "V1_2:  "+str("{0:.4f}".format(V1_2))+",\t"
            "P: "+str("{0:.4f}".format(P))+",\t"
            "L1: "+str("{0:.4f}".format(L1))+",\t"
            "T1: "+str("{0:.4f}".format(T1))+",\t"
            "H: "+str("{0:.4f}".format(H))+",\t"
            "V2: "+str("{0:.4f}".format(V2))+",\t"
            #"L2: "+str("{0:.4f}".format(L2))+",\t"
            "L2L: "+str("{0:.4f}".format(L2L))+",\t"
         )     
    print st
