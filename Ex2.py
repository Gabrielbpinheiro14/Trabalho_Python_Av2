def soma_imposto():
    taxa_imposto = float(input("Digite a quantia de imposto em porcentagem: "))
    custo = float(input("Digite o valor do produto: "))
    pfinal = (((taxa_imposto / 100) * custo) + custo)
    print(f"O valor do produto será de : {pfinal: .2f}")

opcao = 1

while opcao:
    print("Deseja calcular o preço final do produto ?")
    print("1 para sim")
    print("0 para não")

    opcao = int(input("Digite aqui: "))



    if (opcao == 1):
        soma_imposto()