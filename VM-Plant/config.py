
FIELD_IP = '172.27.30.182'#ip wiSumpLow change according to Virtual Machines IP's
FIELD_PORT = 6061

#OPC_IP = '192.168.1.11'
#OPC_PORT = 6060

SIM_TIME = 6
SIM_STEP = 0.1
#Process Variables

SumpLow          = 0
ValvePos_S       = 1
ValvePos_CT      = 2
Pump             = 3
LevelBoiler      = 4
TempBoiler       = 5
Heater           = 6
SteamOutlet      = 7
CTankLevel       = 8
SafeValve        = 10

# L2L = 9
heat_coefficient = 200
heat_coefficient_2 = 50
#if V2 == 7:
   
def printvalues(SumpLow, ValvePos_S, ValvePos_CT,Pump, LevelBoiler, TempBoiler, Heater, SteamOutlet, CTankLevel,SafeValve):
    if SteamOutlet == 0.00:
        st =   ( 
           

            "SumpLow: "+str("{0:.1f}".format(SumpLow))+","
            "ValvePos_S: "+str("{0:.1f}".format(ValvePos_S))+","
            "ValvePos_CT:  "+str("{0:.1f}".format(ValvePos_CT))+","
           
            "Pump: "+str("{0:.1f}".format(Pump))+","
            "LevelBoiler: "+str("{0:.2f}".format(LevelBoiler))+","
            "TempBoiler: "+str("{0:.2f}".format(TempBoiler))+","
            "Heater: "+str("{0:.1f}".format(Heater))+","
            "SteamOut"+str(" {0:.1f} ".format(SteamOutlet))+","
            #"L2: "+str("{0:.4f}".format(L2))+",\t"
            "CTankLevel: "+str("{0:.2f}".format(CTankLevel))+","
            "SafeValve: "+str("{0:.2f}".format(SafeValve))+","
         )     
        print st,'\n' 
    
    if SteamOutlet==1.00:
        st1 =   ( 
           

            "SumpLow: "+str("{0:.1f}".format(SumpLow))+","
            "ValvePos_S: "+str("{0:.1f}".format(ValvePos_S))+","
            "ValvePos_CT:  "+str("{0:.1f}".format(ValvePos_CT))+","
            
            "Pump: "+str("{0:.1f}".format(Pump))+","
            "LevelBoiler: "+str("{0:.2f}".format(LevelBoiler))+","
            "TempBoiler: "+str("{0:.2f}".format(TempBoiler))+","
            "Heater: "+str("{0:.1f}".format(Heater))+","
            "SteamOut: "+str("'\033[1;42m {0:.1f} \033[1;m'".format(SteamOutlet))+","
            #"L2: "+str("{0:.4f}".format(L2))+",\t"
            "CTankLevel: "+str("{0:.2f}".format(CTankLevel))+","
            "SafeValve: "+str("{0:.2f}".format(SafeValve))+","
         )
        print st1,'\n'     


        


    
# else:
#     def printvalues(mode, SumpLow, ValvePosition_S, ValvePoition_CT, P, L1, T1, H, V2, L2L):
#         st =   (mode+",\t" 
               
#                 "SumpLow: "+str("{0:.4f}".format(SumpLow))+",\t"
#                 "ValvePosition_S: "+str("{0:.4f}".format(ValvePosition_S))+",\t"
#                 "ValvePoition_CT:  "+str("{0:.4f}".format(ValvePoition_CT))+",\t"
#                 "P: "+str("{0:.4f}".format(P))+",\t"
#                 "L1: "+str("{0:.4f}".format(L1))+",\t"
#                 "T1: "+str("{0:.4f}".format(T1))+",\t"
#                 "H: "+str("{0:.4f}".format(H))+",\t"
#                 "'\033[1;34mV2: \033[1;m'"+str("{0:.4f}'\033[1;36m\033[1;m'".format('\033[1;36m\033[1;m))+",\t"
#                 #"L2: "+str("{0:.4f}".format(L2))+",\t"
#                 "L2L: "+str("{0:.4f}".format(L2L))+",\t"
#              )     
#         print st
