import time
def who_is_muthhal():
    
    attempt=0
    wait=5
    max_mutthi_in_one_day=7
    while attempt<max_mutthi_in_one_day:
        print("thinking.............")
        attempt=attempt+1
        time.sleep(wait)
        if attempt==1:
                                                                          
            print(f"{attempt}.aayush is muthal")
        elif attempt==2:
            print(f"{attempt}.arjun is second muthal")
        elif attempt==3:
            print(f"{attempt}.abhay is third muthal")
        elif attempt==4:
            print(f"{attempt}.divyanshu is coward muthal")
        elif attempt==5:
            print(f"{attempt}.... no report suggest keshav is muthal")
        elif attempt==6:
            print(f"{attempt}...........shayan have no equipment sorry!")
        else:
            print("thankyou")
who_is_muthhal()
print("hope you guys agree with my programm")
print("github successfull!!")
          
