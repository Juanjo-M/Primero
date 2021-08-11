#print ("¿Que palabra desea escribir?"):

#P=str(input(""))

P = input("¿Que palabra desea escribir? ")


while (P !="chupacabra"):
    #print("Puede seguir escribiendo palabras")
    if (P == "chupacabra"):
        break    
    P = input("¿Que palabra desea escribir? ")
print("Aqui se detiene el bucle")