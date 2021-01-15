def lcm(x, y):
 
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
 
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           result = greater
           break
       greater += 1
 
   return result

#example use
print(lcm(21,14)) # 2*7 and  3*7, answer is 2*3*7= 42