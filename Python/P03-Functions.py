a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 2)
print(a[x])

##########

def f1_print():
    print ("This is F1_Function")

f1_print()

#########

def f2_Subnet(Mask):
    if Mask=="255.0.0.0":
        print ("Class A Subnet")
    elif Mask=="255.255.0.0":
        print ("Class B Subnet")
    elif Mask=="255.255.255.0":
        print ("Class C Subnet")
    else :
        print ("Undefined Class")

Mask = input("Please enter your Subnet Mask: ")
f2_Subnet(Mask)

##########
