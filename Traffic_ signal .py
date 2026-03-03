while True:
    light = input("Enter light color: \n")
    if(light=="Exit")or (light=="EXIT")or (light=="exit"):
        print ("Exiting prgm ")
        break
    if (light=="red")or (light=="RED")or(light=="Red"):
        print("STOP")
    elif (light=="yellow")or(light=="YELLOW")or(light=="Yellow"):
        print("GET READY")
    elif(light=="green")or(light=="GREEN")or(light=="Green"):
        print("GO")
    else:
        print("LIGHT IS BROKEN")
