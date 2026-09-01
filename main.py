import random

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto"
,"Setembro","Outubro", "Novembro", "Dezembro"]
vendas_ano = [random.randint(100,999) for _ in meses]

total_ano = sum(vendas_ano)
media = total_ano / len(meses)
meta = media * 1.40
maior_venda = max(vendas_ano)
menor_venda = min(vendas_ano)
melhor_mes = meses[vendas_ano.index(maior_venda)]
pior_mes = meses[vendas_ano.index(menor_venda)]

meses_meta_batida = [
    (mes, venda) for mes, venda in zip(meses, vendas_ano) if venda >= meta
]
taxa_sucesso = (len(meses_meta_batida) / len(meses)) * 100

print(f"Meta de cada mes: {meta:.0f} mil vendas")

print("\n--- Vendas do Ano ---")
for mes, venda in zip(meses, vendas_ano):
    print(f"{mes}: R$ {venda:.0f} mil")
print("\n--- Resultados ao final do ano---")
for mes, venda in zip(meses,vendas_ano):
  if venda > meta:
    print(f"No mês de {mes}, as vendas superaram a meta estabelecida: {venda:.0f} mil")

print("=" * 65)
print(f"Total Faturado no Ano: R$ {total_ano:.0f} mil")
print(f"Média Mensal: R$ {media:.0f} mil")
print(f"Meta Mensal (Média + 40%): R$ {meta:.0f} mil")
print(f"Melhor Mês: {melhor_mes} (R$ {maior_venda:.0f} mil)")
print(f"Pior Mês: {pior_mes} (R$ {menor_venda:.0f} mil)")
print(f"Atingimento da Meta: {len(meses_meta_batida)} de 12 meses ({taxa_sucesso:.1f}%)")
print("=" * 65)
