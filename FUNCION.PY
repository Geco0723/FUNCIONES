import os
os.system("cls")

#funciones
def IVA(subtotal):
    total= 1.21 * subtotal
    return total
#ingresar datos del cliente

ape= input("Ingrese el apellido del cliente: ")
dni=int(input("Ingrse el DNI del cliente: "))
localidad=input("Ingrese la localidad a la que pertenece: ")

#ingresar los productos
primer_producto=input("Ingrese el producto a comprar: ")
valor_primer_producto=float(input("Ingrese el valor del producto en pesos: $ "))
cantidad_primer_producto=int(input("Ingrese la cantidad de productos a llevar: "))
total_primer_producto= cantidad_primer_producto * valor_primer_producto

segundo_producto=input("Ingrese el producto a comprar: ")
valor_segundo_producto=float(input("Ingrese el valor del producto en pesos: $ "))
cantidad_segundo_producto=int(input("Ingrese la cantidad de productos a llevar: "))
total_segundo_producto= cantidad_segundo_producto * valor_segundo_producto

subtotal= total_primer_producto + total_segundo_producto
#total de la compra utilizando a la funcion IVA

print("############# TICKET DE COMPRA ################")
print("EL CLIENTE ", ape , "DE DNI " , dni, "DE LA LOCALIDAD DE ",localidad)
print("REALIZO UNA COMPRA DE: ", primer_producto, "Y" , segundo_producto)
print("EL TOTAL DE LA COMPRA MAS IVA ES DE: $", IVA(subtotal))
