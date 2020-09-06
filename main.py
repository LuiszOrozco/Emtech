import os
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

while True:
  user = input("Ingresa tu usuario: ")
  password = input("Ingresa tu contraseña: ")
  if user == "luis" and password == "Password123" or  user== "admin" and password=="root" :
    os.system("clear")  
    print("Contraseña Correcta, bienvenido "+ user)
    input("Presiona alguna tecla para continuar")
    os.system("clear")  
    while True:
      print("\tBienvenido al sistema de análisis de la empresa LifeStore\n")
      print("Este sistema maneja varios reportes, selecciona la opción que necesites\n")
      print("1.-Productos más vendidos y productos rezagados.\n2.- por reseña en el servicio.\n3.- Total de ingresos y ventas promedio mensuales.\n4.-Salir del sistema")
      options=input("\nIngresa una opcion: ")
      if options== "1":
        os.system("clear")  
        print("Has elegido la opción 1\n")
        while True:
          os.system("clear")
          print("\t¿Qué reporte deseas crear?\n")
          print("1.-Listado de los 50 productos con mayores ventas")
          print("2.-Listado 100 productos con mayor búsqueda")
          print("3.-Listado por categoria 50 productos menores ventas")
          print("4.-100 productos con menores búsquedas por categoria")
          print("5.-Regresar al menú anterior") 
          option=input("Ingresa una opción: ") 
          if option == "1":
            os.system("clear")
            print("---------REPORTE PRODUCTOS MAS VENDIDOS ORDENADOS")
            #Se crea una matriz
            size = len(lifestore_products)
            sales = [0] * size
            for s in lifestore_sales:
              idx = s[1]#se obtiene id
              sales[idx-1] += 1 # Se resta ya que se contabiliza desde la posición 1, so, 1-1=0[posición]
            sells=[]
            for i in range(0, len(lifestore_products)):
              name = lifestore_products[i][1]
              times = sales[i]
              item = [ name, times]
              sells.append(item)
            aux = None
            for i in range (0,len(sells)):
              for j in range (0,len(sells)):
                if(sells[i][1] > sells[j][1]):
                  aux = sells[i]
                  sells[i] = sells[j]
                  sells[j] = aux 
            counter = 1
            for i in range(0,len(sells)):
              if sells[i][1] != 0: # Omite las busquedas con 0.
                print(counter,".-Producto: "+sells[i][0]) # tomo el valor de producto
                print("Cantidad vendida : "+str(sells[i][1])) # imprimé  la cantidad.
                counter += 1
            print("------------------------------------")
            mensaje=input(print("Presiona regresar al meno anterior..."))
            os.system("clear")
            continue
          elif option == "2":
            os.system("clear")
            print("---------REPORTE PRODUCTOS MAS BUSCADOS ORDENADOS")
            print("------------------")
            size = len(lifestore_products)
            sales = [0] * size
            searchers = [0] *size
            for s in lifestore_searches:
              idx = s[1]#se obtiene id
              searchers[idx-1] += 1 # Se resta ya que se contabiliza desde la posición 1, so, 1-1=0[posición]
            sells = []
            for i in range(0, len(lifestore_products)):
              name = lifestore_products[i][1]
              times = searchers[i]
              item = [ name, times]
              sells.append(item)
            aux = None
            os.system("clear")
            for i in range (0,len(sells)):
              for j in range (0,len(sells)):
                if(sells[i][1] > sells[j][1]):
                  aux = sells[i]
                  sells[i] = sells[j]
                  sells[j] = aux 
            counter = 1
            for i in range(0,len(sells)):
              if sells[i][1] != 0: # Omite las busquedas con 0.
                print(counter,".-Producto: "+sells[i][0]) # tomo el valor de producto
                print("Busquedas : "+str(sells[i][1])) # imprimé  la cantidad.
                counter += 1
            print("-----------------------------------------")
            mensaje=input(print("Presiona cualquier tecla regresar al menú anterior..."))
            os.system("clear")
            continue
          elif option == "3":

            os.system("clear")
            print("---------REPORTE PRODUCTOS MENOS VENDIDOS POR CATEGORIA")
            #Se crea una matriz
            size = len(lifestore_products)
            sales = [0] * size
            for s in lifestore_sales:
              idx = s[1]#se obtiene id
              sales[idx-1] += 1 # Se resta ya que se contabiliza desde la posición 1, so, 1-1=0[posición]
            sells=[]
            for i in range(0, len(lifestore_products)):
              name = lifestore_products[i][1]
              times = sales[i]
              category = lifestore_products[i][3]
              item = [ name, times,category]
              sells.append(item)
            aux = None
            for i in range (0,len(sells)):
              for j in range (0,len(sells)):
                if(sells[i][1] < sells[j][1]):
                  aux = sells[i]
                  sells[i] = sells[j]
                  sells[j] = aux 
            counter = 1
            for i in range(0,len(sells)):
              if sells[i][1] != 0: # Omite las busquedas con 0.
                print(counter,".-Producto: "+sells[i][0]) # tomo el valor de producto
                print("Cantidad vendida : "+str(sells[i][1])) # imprimé  la cantidad.
                print("Categoría "+str(sells[i][2]))
                counter += 1
            print("------------------------------------")
            mensaje=input(print("Presiona regresar al meno anterior..."))
            os.system("clear")
            continue
          elif option == "4":
            os.system("clear")            
            print("---------Reporte  menores busquedas por categoria")
            size = len(lifestore_products)
            sales = [0] * size
            searchers =[0] *size
            for s in lifestore_searches:
              idx = s[1]#se obtiene id
              searchers[idx-1] += 1 # Se resta ya que se contabiliza desde la posición 1, so, 1-1=0[posición]
            sells = []
            for i in range(0, len(lifestore_products)):
              name = lifestore_products[i][1]
              times = searchers[i]
              category =lifestore_products[i][3] ##se agrega categoria
              item = [ name, times, category]
              sells.append(item)
            aux = None
            for i in range (0,len(sells)):
              for j in range (0,len(sells)):
                if(sells[i][1] < sells[j][1]):
                  aux = sells[i]
                  sells[i] = sells[j]
                  sells[j] = aux 
            counter = 1
            for i in range(0,len(sells)):
              if sells[i][1] != 0: # Omite las busquedas con 0.
                print(counter,".-Producto: "+sells[i][0]) # tomo el valor de producto
                print("Busquedas : "+str(sells[i][1])) # imprimé  la cantidad.
                print("Categoria: " +str(sells[i][2]))
                counter += 1
            print ("-----------------------")
            print(input("Presiona cualquier tecla para continuar"))
            os.system("clear")
            continue
          elif option == "5":
            os.system("clear")
            break
          else:
              os.system("clear")
              print("Ingresa una opción válida")
              print(input("Da clic para continuar"))
              continue
              os.system("clear")
        continue      
      elif options =="2":
        os.system("clear")
        print("Has elegido la opción 2")
        print("\tProductos por Mejor reseña....\n")
        venta = []
        resena=[]
        aux=[0,0]
        #Crear listas de apoyo
        for i in range(0,len(lifestore_products)):
          venta.append([i+1,0])

        for i in range(0,len(lifestore_products)):
          resena.append([i+1,0])

        #Obtención del recuento de estrellas y id
        for i in range (0,len(lifestore_sales)):
            venta[lifestore_sales[i][1]-1][1]=venta[lifestore_sales[i][1]-1][1] + 1

        #Conteo de repeticiones de estrellas
        for i in range (0,len(lifestore_sales)):
            resena[lifestore_sales[i][1]-1][1]=resena[lifestore_sales[i][1]-1][1]+lifestore_sales[i][2]

        # Obtener promedio de estrellas por cada producto.
        for i in range (0,len(resena)):
          if(venta[i][1] > 0):
            resena[i][1]=resena[i][1]/venta[i][1]

        #Ordenar de mayor a menor
        for i in range (0,96):
          for j in range (0,96):
            if(resena[i][1] < resena[j][1]):
              aux[0] = resena[i]
              resena[i] = resena[j]
              resena[j] = aux[0]

        for i in range(0,20):
          print(i+1,".Producto: \n",lifestore_products[resena[95-i][0]-1][1])
          print("Reseña :",resena[95-i][1])
        print(input("\nDa clic para crear segundo reporte"))
        os.system("clear")
        print("\t Productos por peor reseña")
        venta = []
        resena=[]
        aux=[0,0]
        #Crear listas de apoyo
        for i in range(0,len(lifestore_products)):
          venta.append([i+1,0])

        for i in range(0,len(lifestore_products)):
          resena.append([i+1,0])

        #Obtención del recuento de estrellas y id
        for i in range (0,len(lifestore_sales)):
            venta[lifestore_sales[i][1]-1][1]=venta[lifestore_sales[i][1]-1][1] + 1

        #Conteo de repeticiones de estrellas
        for i in range (0,len(lifestore_sales)):
            resena[lifestore_sales[i][1]-1][1]=resena[lifestore_sales[i][1]-1][1]+lifestore_sales[i][2]

        # Obtener promedio de estrellas por cada producto.
        for i in range (0,len(resena)):
          if(venta[i][1] > 0):
            resena[i][1]=resena[i][1]/venta[i][1]

        #Ordenar de mayor a menor
        for i in range (0,96):
          for j in range (0,96):
            if(resena[i][1] > resena[j][1]):
              aux[0] = resena[i]
              resena[i] = resena[j]
              resena[j] = aux[0]

        contador = 0
        while contador<=20:
          for i in range(0,96):
            if contador <=19:
              if resena[95-i][1]>0:
                print(contador+1,".Producto \n:",lifestore_products[resena[95-i][0]-1][1])
                print("Reseña :",resena[95-i][1],"\n")
                contador+=1
          break
        print("---------------------------")        
        print(input("Presiona cualquier tecla para volver al menú anterior"))
        os.system("clear")
        continue
      elif options =="3":
        os.system("clear") 
        prices = []
        for i in range(0,len(lifestore_products)):#Se agrega el precio del producto
          prices.append(lifestore_products[i][2])
        months = []
        for i in range(0,len(lifestore_sales)):
          id_product = lifestore_sales[i][1]-1 # Obtienes el id, pero se resta 1 para  no contar el 0
          date_sale = lifestore_sales[i][3].split("/")[1]# se obtiene el mes, ej: 08
          if len(months) == 0:
            months.append([prices[id_product], date_sale])#Se accede al precio por medio del id, y se agrega la fecha. Solo se usa una vez.
          else:
            flag = False
            for m in months:
              if m[1] == date_sale: # busca si la fecha ya esta agregada
                m[0] += prices[id_product]#Si la encuentra suma el producto
                flag = True #la bandera se hace verdadera.    
            if flag == False:
              months.append([prices[id_product], date_sale])    
        aux=[0,0]
        for i in range (0,len(months)):
          for j in range (0,len(months)):
            if(months[i][1] < months[j][1]):
              aux[0] = months[i]
              months[i] = months[j]
              months[j] = aux[0]
        total = 0
        for i in range (0,len(months)):
          auxi = months[i][0]
          total = total + auxi
        promedio = total/12
        print("-----Reporte de ingresos-------")
        for i in range(0,len(months)):
          print("Mes:",months[i][1],"Ventas de: $"+str(months[i][0]))
        print("\nEl total de ventas anuales fue: $:",str(total))
        print("El promedio mensual fue: $",str(promedio))
        print(input("Da clic para regresa al menu anterior"))
        os.system("clear")
        continue
      elif options =="4":
        os.system("clear")  
        print("Saliendo del sistema")
        break
      else:
        os.system("clear")  
        print("Opción incorrecta , intenta de nuevo")
      salir=input("¿desea salir del programa y/n?")
    break
  else: 
    input("Contraseña incorrecta , presiona alguna tecla para reintentar..")
    os.system("clear")
print("Usted ha salido del sistema, gracias por usarlo.")


