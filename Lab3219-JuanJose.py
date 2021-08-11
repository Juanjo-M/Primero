import time
palabra=input("Adivina la palabra :")

while palabra!="chupacabra":
    palabra=input("No era esa palabra sigue escribiendo :")
    if palabra=="chupacabra":               
        break 
print("Bien acertastes la palabra")
time.sleep(0.5)
print("El programa se apagara en 1. ")
time.sleep(1)
print("El programa se apagara en 1. 2.. ")
time.sleep(1)
print("El programa se apagara en 1. 2.. 3...1001101011000....")
time.sleep(1)
print("✔ programa apagado 😴😴😴")