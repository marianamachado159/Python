nome_vendedor = input()

salario_fixo = float(input())
total_vendas = float(input())

comissao = total_vendas * 0.15
total_a_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_a_receber:.2f}")