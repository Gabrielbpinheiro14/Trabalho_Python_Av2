def area_do_trapezio():
    base_maior = float(input("Digite a base maior: "))
    base_menor = float(input("Digite a base menor do trapezio: "))
    altura = float(input("Digite a altura do trapezio: "))
    calculo_area = (((base_maior + base_menor)* altura)/ 2)
    print(f"A area do trapezio eh : {calculo_area: .2f}")

pgta = 1

while pgta:
    print("Deseja calcular a area do trapezio ?")
    print("1 para continuar")
    print("0 para sair")

    pgta = int(input("Digite aqui: "))

    if (pgta == 1):
        area_do_trapezio()