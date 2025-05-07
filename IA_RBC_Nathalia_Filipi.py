import random

# Atributos considerados
atributos = ['Febre', 'Tosse', 'Falta de Ar', 'Dor de Garganta', 'Raio-X Alterado']
doencas_possiveis = ['Gripe', 'Resfriado', 'Covid-19', 'Bronquite', 'Pneumonia']

# Criar 50 casos aleatórios
casos = []
for _ in range(50):
    caso = {
        'Febre': random.choice(['sim', 'nao']),
        'Tosse': random.choice(['sim', 'nao']),
        'Falta de Ar': random.choice(['sim', 'nao']),
        'Dor de Garganta': random.choice(['sim', 'nao']),
        'Raio-X Alterado': random.choice(['sim', 'nao']),
        'diagnostico': random.choice(doencas_possiveis)
    }
    casos.append(caso)

# Pesos padrão
pesos_default = {
    'Febre': 2,
    'Tosse': 1,
    'Falta de Ar': 3,
    'Dor de Garganta': 1,
    'Raio-X Alterado': 3
}

def alterar_pesos(pesos):
    print("\n--- Pesos Padrão ---")
    print(f"{'| Atributo':<20} | {'Peso':<4} |")
    print("|" + "-"*20 + "|" + "-"*6 + "|")
    for atributo, peso in pesos.items():
        print(f"| {atributo:<18} | {peso:<4} |")

    print("\nDeseja alterar os pesos dos atributos?")
    escolha = input("Digite 's' para sim, qualquer outra tecla para manter os padrões: ").lower()
    if escolha == 's':
        print("\n--- Alteração de Pesos ---")
        for atributo in pesos:
            atual = pesos[atributo]
            entrada = input(f"Peso para '{atributo}' (padrão = {atual}): ").strip()
            if entrada.isdigit():
                pesos[atributo] = int(entrada)
            elif entrada != '':
                print("⚠️ Peso inválido, mantendo valor padrão.")
    else:
        print("✔️ Mantendo os pesos padrão.")
    return pesos

def entrada_usuario():
    print("\n--- Entrada do Caso Atual ---")
    entrada = {}
    for atributo in atributos:
        valor = input(f"{atributo.replace('_', ' ').capitalize()} (sim/nao): ").strip().lower()
        while valor not in ['sim', 'nao']:
            valor = input(f"Valor inválido. Digite 'sim' ou 'nao' para {atributo}: ").strip().lower()
        entrada[atributo] = valor
    return entrada

def similaridade(caso1, caso2, pesos):
    total_peso = sum(pesos.values())
    score = 0
    for atributo in atributos:
        if caso1[atributo] == caso2[atributo]:
            score += pesos[atributo]
    return (score / total_peso) * 100

def exibir_resultados(entrada, pesos, casos):
    resultados = []
    for idx, caso in enumerate(casos):
        sim = similaridade(entrada, caso, pesos)
        resultados.append((idx, sim, caso['diagnostico'], caso))

    resultados.sort(key=lambda x: x[1], reverse=True)

    print("\n\n=== Resultado da Comparação ===")
    print("📌 Caso de entrada:")
    for a in atributos:
        print(f"- {a.replace('_', ' ').capitalize()}: {entrada[a]}")
    
    print("\n🔍 Casos similares (ordem decrescente):\n")
    for idx, sim, diag, caso in resultados:
        print(f"🔹 Similaridade: {sim:.2f}% | Diagnóstico: {diag}")
        for a in atributos:
            print(f"   {a.replace('_', ' ').capitalize()}: {caso[a]}")
        print("-" * 40)

# Execução principal
if __name__ == "__main__":
    print("📋 RBC - Diagnóstico de Doenças Respiratórias")
    pesos = alterar_pesos(pesos_default.copy())
    entrada = entrada_usuario()
    exibir_resultados(entrada, pesos, casos)
