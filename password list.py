import time

TimeStart = time.perf_counter()
def cracker():
    p1 = 0
    p2 = 0
    p3 = 0
    
    passward =[]
    crackedpassward = []
    print("Please Give me A three number passward")
    


    
    for i in range(3):
        passward.append(int(input()))

    for l in range(10):
        if passward[0] == p1:
            crackedpassward.append(p1)
            break
        else:
            p1 +=1    
    for j in range(10):
        if passward[1] == p2:
            crackedpassward.append(p2)
            break
        else:
            p2 +=1
    for k in range(10):
        if passward[2] == p3:
            crackedpassward.append(p3)
            break
        else:
            p3 +=1
    print(crackedpassward)



            

cracker()
end = time.time()
TimeEnd = time.perf_counter()
print(f"It took you {TimeEnd-TimeStart:0.4f} seconds")

