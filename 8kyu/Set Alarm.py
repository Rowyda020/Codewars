#Set Alarm
def set_alarm(employed, vacation):
   if employed==True and vacation==True:
       return False
   elif employed==True and vacation==False:
       return True
   elif employed==False and vacation==True:
       return False
   elif employed==False and vacation==False:
       return False