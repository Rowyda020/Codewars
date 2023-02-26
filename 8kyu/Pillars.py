#Pillars
def pillars(num_pillars, dist, width):
   dist=dist*100
   if num_pillars > 1:
       return (num_pillars-1) * dist + (width * (num_pillars-2))
   else:
       return 0