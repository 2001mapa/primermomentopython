inventarios = []

print("***********Menu salpicon***********")

option = 15
while (option != 5):
    print("***********************************")
    print("1.- Ingresa la fruta")
    print("2.- Valor total Salpicon") 
    print("3.- Cual es la fruta mas barata")
    print("4.- Cancelar")
    
    option = int(input("Dijita una opcion: "))
    print("***********************************")
    
    if option == 1:
        inventario = {}
        inventario ["id"] = input("Dijita el ID: ")
        inventario ["nombre"] = input("Dijita el Nombre de la fruta: ")
        inventario ["precio"] = int(input("Dijita el precio de la fruta: "))
        inventario ["cantidad"] = int(input("Dijita la cantidad de frutas: "))
        
        inventarios.append(inventario)


    elif option == 2:
        inventarios_ordenados = sorted(inventarios, key=lambda x: x["precio"], reverse=True)
        
        total_salpicon = 0
        print("Frutas de mayor a menor por precio:")
        print("***********************************")
        for fruta in inventarios_ordenados:
            total_salpicon += fruta["precio"] * fruta["cantidad"]
            print(f"{fruta['nombre']}: ${fruta['precio']}")    
        print(f"\nTotal del Salpicón: ${total_salpicon}")
        
    elif option == 3:
        fruta_mas_barata = min(inventarios, key=lambda x: x["precio"])
        print(f"La fruta más barata es: {fruta_mas_barata['nombre']} con un precio de ${fruta_mas_barata['precio']}")
        
    elif option == 4:
        pass
    
    else:
        pass