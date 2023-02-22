import time;

def countdown(time_sec): #def is used to define a function
  while time_sec:
    mins,secs = divmod(time_sec, 60);  
     # divmod(4, 2)  gives (2,0) as result  where 2 is the quotient and 0 is the remainder
    timeformat = '{:02d}:{:02d}'.format(mins, secs);
    print(timeformat, end ='\r');
    time.sleep(1);
    time_sec -=1;


    print("stop");


num = int(input("Set your timer in sec : "));

countdown(num);





