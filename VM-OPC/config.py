FIELD_IP = '172.27.22.45' #ip will change according to Virtual Machines IP's
FIELD_PORT = 6060

#SIM_TIME = 100
#SIM_STEP = 0.1
#Process Variables
HL  = 0
LL  = 1
V1_1= 2
V1_2= 3
P   = 4
L1  = 5
T1  = 6
H   = 7
V2  = 8
L2  = 9
L2L = 10
heat_coefficient = 10
heat_coefficient_2 = 50

def printvalues(mode, HL, LL, V1_1, V1_2, P, L1, T1, H, V2, L2, L2L):
    st =   (mode+",\t" 
            "HL: "+str("{0:.4f}".format(HL))+",\t"
            "LL: "+str("{0:.4f}".format(LL))+",\t"
            "V1_1: "+str("{0:.4f}".format(V1_1))+",\t"
            "V1_2:  "+str("{0:.4f}".format(V1_2))+",\t"
            "P: "+str("{0:.4f}".format(P))+",\t"
            "L1: "+str("{0:.4f}".format(L1))+",\t"
            "T1: "+str("{0:.4f}".format(T1))+",\t"
            "H: "+str("{0:.4f}".format(H))+",\t"
            "V2: "+str("{0:.4f}".format(V2))+",\t"
            "L2: "+str("{0:.4f}".format(L2))+",\t"
            "L2L: "+str("{0:.4f}".format(L2L))+",\t"
         )     
    print st
