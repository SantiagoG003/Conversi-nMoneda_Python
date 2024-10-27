divisas = {
    "usd":1.09,
    "mxn":21.62,     #Editar valores para tener los actuales
    "gbp":0.83,
    "mad":10.73
}

cantidad = int(input("Cantidad: "))
div = input("Divisa: ")
if div in divisas.keys():
    resultado = divisas[div] * cantidad
    print(f"Resultado: {resultado}")