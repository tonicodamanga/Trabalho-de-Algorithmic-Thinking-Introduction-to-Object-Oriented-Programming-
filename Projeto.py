import csv

print("=== ORÇAMENTO DE ALUGUEL ===")

tipo = input("Tipo de imóvel (apartamento / casa / estudio): ").lower()
quartos = int(input("Quantidade de quartos: "))
vagas = int(input("Quantidade de vagas/garagem: "))
criancas = input("Possui crianças? (s/n): ").lower()



print("\nForma de pagamento:")
print("1 - Dinheiro")
print("2 - Pix")
print("3 - Cartão de Crédito")

forma_pagamento = input("Escolha a forma de pagamento (1/2/3): ")

valor_aluguel = 0

if tipo == "apartamento":
    valor_aluguel = 700

    if quartos == 2:
        valor_aluguel += 200

    if vagas > 0:
        valor_aluguel += 300

    if criancas == "n":
        valor_aluguel *= 0.95

elif tipo == "casa":
    valor_aluguel = 900

    if quartos == 2:
        valor_aluguel += 250

    if vagas > 0:
        valor_aluguel += 300

elif tipo == "estudio":
    valor_aluguel = 1200

    if vagas >= 2:
        valor_aluguel += 250

    if vagas > 2:
        valor_aluguel += (vagas - 2) * 60

else:
    print("Tipo de imóvel inválido!")
    exit()

valor_contrato = 2000



parcelas_contrato = 1

if forma_pagamento == "3":
    parcelas_contrato = int(input("Em quantas vezes deseja parcelar o contrato? (até 5x): "))
    
    if parcelas_contrato > 5:
        print("Máximo permitido é 5x. Será considerado 5x.")
        parcelas_contrato = 5

valor_parcela_contrato = valor_contrato / parcelas_contrato



if forma_pagamento == "1":
    pagamento = "Dinheiro"
elif forma_pagamento == "2":
    pagamento = "Pix"
elif forma_pagamento == "3":
    pagamento = "Cartão de Crédito"
else:
    pagamento = "Não identificado"

print("\n--- ORÇAMENTO FINAL ---")
print(f"Valor do aluguel mensal: R$ {valor_aluguel:.2f}")
print(f"Forma de pagamento escolhida: {pagamento}")
print(f"Contrato: R$ 2.000,00 em {parcelas_contrato}x de R$ {valor_parcela_contrato:.2f}")


with open("parcelas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Mês", "Valor do Aluguel"])

    for mes in range(1, 13):
        escritor.writerow([mes, f"R$ {valor_aluguel:.2f}"])

print("\nArquivo 'parcelas.csv' criado com sucesso!")
