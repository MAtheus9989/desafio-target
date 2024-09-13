import json

def analisar_faturamento(arquivo):
    
    with open(arquivo, 'r') as f:
        dados = json.load(f)

    faturamentos = [dado['valor'] for dado in dados if dado['valor'] > 0]
    if not faturamentos:
        return None, None, 0

    media = sum(faturamentos) / len(faturamentos)
    menor_valor = min(faturamentos)
    maior_valor = max(faturamentos)
    dias_acima_media = sum(1 for valor in faturamentos if valor > media)

    return menor_valor, maior_valor, dias_acima_media

# Exemplo de uso:
arquivo_json = 'faturamento.json'  # Substitua pelo nome do seu arquivo
menor, maior, dias_acima = analisar_faturamento(arquivo_json)

if menor is not None:
    print(f"Menor valor: R$ {menor:.2f}")
    print(f"Maior valor: R$ {maior:.2f}")
    print(f"Dias acima da média: {dias_acima}")
else:
    print("Não há dados de faturamento válidos.")