
#getting user inputs
weight = input("Enter the weight:"); 
unit = input("Enter (k)for kg and (l)for lbs:"); 

#coverting basics of the options selected

#coverting pounds to kilogram
if unit.lower() == "k": 
    kg_weight = float(weight) * 0.45359237; 
    print( " weight in kilograms :" +str(kg_weight)); 

#converting kilogram to pounds
elif  unit.lower() == "l" :
    lg_weight = float(weight) / 0.45359237; 
        #lg_weight = weight * 2.20462262185
    print( "weight in pounds :"+str(lg_weight)); 

else :
    unit.lower(); 
    print("invalid"); 
