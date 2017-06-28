

OPC_IP = '192.168.0.107'
OPC_PORT = 6060

FIELD_IP = '192.168.0.107'#ip wiSumpLow change according to Virtual Machines IP's
FIELD_PORT = 6061


SIM_TIME = 260
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
SafeValve        = 9

# L2L = 9
heat_coefficient = 200
heat_coefficient_2 = 50
#if V2 == 7:
   
def printvalues(SumpLow, ValvePos_S, ValvePos_CT,Pump, LevelBoiler, TempBoiler, Heater, SteamOutlet, CTankLevel):
    if SteamOutlet == 0.00:
        st =   ( 
           

            "SumpLow: "+str("{0:.1f}".format(SumpLow))+","
            "ValvePos_S: "+str("{0:.1f}".format(ValvePos_S))+","
            "ValvePos_CT:  "+str("{0:.1f}".format(ValvePos_CT))+","
           
            "Pump: "+str("{0:.1f}".format(Pump))+","
            "LevelBoiler: "+str("{0:.2f}".format(LevelBoiler))+","
            "TempBoiler: "+str("{0:.3f}".format(TempBoiler))+","
            "Heater: "+str("{0:.1f}".format(Heater))+","
            "SteamOut"+str(" {0:.1f} ".format(SteamOutlet))+","
            #"L2: "+str("{0:.4f}".format(L2))+",\t"
            "CTankLevel: "+str("{0:.2f}".format(CTankLevel))+","

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
         )
        print st1,'\n'     

seq=30
padding=10
batch_size = 26
nb_classes = 1
nb_epoch = 10