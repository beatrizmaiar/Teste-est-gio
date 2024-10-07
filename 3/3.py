import json

def analisar_faturamento(dados_faturamento):

  faturamentos = list(dados_faturamento.values())
  
  # Ignora dias sem faturamento (0)
  faturamentos_validos = [f for f in faturamentos if f > 0]

  menor_valor = min(faturamentos_validos)
  maior_valor = max(faturamentos_validos)

  media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

  dias_acima_media = sum(1 for f in faturamentos_validos if f > media_mensal)

  return {
    "menor_valor": menor_valor,
    "maior_valor": maior_valor,
    "dias_acima_media": dias_acima_media
  }

# Carrega os dados de faturamento do arquivo JSON
with open("faturamento_diario.json", "r") as arquivo:
  dados_faturamento = json.load(arquivo)

# Analisa os dados e imprime os resultados
resultados = analisar_faturamento(dados_faturamento)
print("Menor valor de faturamento:", resultados["menor_valor"])
print("Maior valor de faturamento:", resultados["maior_valor"])
print("Número de dias com faturamento acima da média:", resultados["dias_acima_media"])
