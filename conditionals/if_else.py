light=input("enter light name: ")
if (light=="green"):
    print("go")
elif(light=="red"):
    print("stop")
elif(light=="orange"):
    print("Waite")
else:
    print("invalid light")

#nesting

age=34
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
