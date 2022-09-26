import random
def alert(temp):
    if temp>60:
        print("High temperature : alarm on")
    else:
        print("Low temperature : alarm off")

while(1):
    tmp=random.randint(40,100)
    hum=random.randint(0,100)
    print("temperature:",tmp)
    print("humidity:",hum)
    alert(tmp)
