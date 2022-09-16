import math
print("Give me 3 numbers pls")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = num3 + num2 + num1
print("Your average is: ",num4/3)
print("Give me two more numbers")
num5 = int(input())
num6 = int(input())
num7 = (math.sqrt(num5))
num8 = num6*num6
print("The square root is: ", num7)
print("The square root is: ", num8)











#------------------------------------------------------------------------------------------------------
print("Question 2")

def PythagoreanCheck(a,b,c):
    if math.sqrt((a**a) + (b**b)) == (c**c):
        print("BOOM")
        return True
    elif math.sqrt((a**2) + (b**2)) != (c**2):
        print("Nope sorry")
        return False
    else:
        print("miiiiiiissssss")
        return False
    
    

xa = int(input(print ("Enter triangles hyponose a: ")))
xb = int(input(print ("Enter triangles opposite: ")))
ya = int(input(print ("Enter triangles sin: ")))


PythagoreanCheck(xa,ya,xb)
