"""
Acciones del menú:

Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""
opcion=0

listaProductos=[]
#producto={"nombre": nombre, "cantidad":stock,"precio":precio}
def solicitarProducto():
    nombreProd= input("Ingrese el nombre del nuevo producto: ")
    try:
        precioProd= int(input("Ingrese el precio del nuevo producto: "))
        stockProd= int(input("Ingrese el stock del nuevo producto: "))
        if precioProd<0 or stockProd<0:
            raise ValueError
        else:
          return[nombreProd,precioProd,stockProd]
    except ValueError:
        print("Debe ingresar valores númericos positivos")

def buscarProducto(nombre):

    for producto in listaProductos:
        if producto["nombre"]==nombre:
            return producto
        
    return None

def guardarProducto(nombre,precio,stock)
    
    if buscarProducto(nombre)==None:
        producto={
            "nombre": nombre,
            "cantidad":stock,
            "precio":precio
            }
        listaProductos.append(producto)
        print("producto guardado de forma exitosa")
    else:
        print("ya existe un producto con ese nombre")

def actualizarProducto(nombre,nuevoStock,nuevoPrecio):
    productoBuscado=buscarProducto(nombre)
    if productoBuscado !=None:
        indice= listaProductos.index(productoBuscado)
        productoBuscado["cantidad"]=nuevoStock
        productoBuscado["precio"]=nuevoPrecio
        #actualizar el producto en la lista de prouctos
        listaProductos[indice]=productoBuscado
        print(f"el producto {nombre} fue actualizado correctamente")
    else:
        print("el producto que intenta actualizar no existe")

def mostrarInventarioCompleto():
    if len(listaProductos)==0:
        print("no hay productos en la lista")
    else:
        for producto in listaProductos:
            print(f"nombre : {producto["nombre"]} \t\t precio: ${producto["precio"]} \t\t stock: {producto["cantidad"]}")

def eliminarProducto(nombre):
    productoBuscado=buscarProducto(nombre)
    if productoBuscado !=None:
        listaProductos.remove(productoBuscado)
        print("el producto fue eliminado exitosamente")
    else:
        print("el producto no existe")


 


while opcion!="6":
    print("**************Menu de gestión de inventario**************")
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion= input("Ingrese la opción que desea(1-6): ")

    match opcion:
        case "1":
            infoProducto=solicitarProducto()
            #[nombreProd,precioProd,stockProd]
            if infoProducto!=None:
                guardarProducto(infoProducto[0],
                                infoProducto[1],
                                infoProducto[2])
        case "2":
            nombre=input("Ingrese el nombre del producto a buscar: ")
            productoEncontrado=buscarProducto(nombre)
            if productoEncontrado!=None:
                print("-"*66)
                print(f"nombre : {productoEncontrado{"nombre"}} \t\t precio: ${productoEncontrado{"precio"}} \t\t stock: {productoEncontrado{"cantidad"}}")
                print("-"*60)    

        case "3":
            infoProducto=solicitarProducto()
            #nombreProd,precioProd,stockProd
            if infoProducto !=None:
                actualizarProducto(nombre=infoProducto[0], nuevoStock=infoProducto[1],nuevoPrecio=infoProducto{2} )

        case "4":
            mostrarInventarioCompleto()

        case "5":
             nombre=input("Ingrese el nombre del producto a eliminar: ")
             eliminarProducto(nombre)

        case "6":
            print("saliendo...")

        case default:
            print("opcion no alida")