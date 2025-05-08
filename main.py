import random
import math

# Atributos considerados
atributos = ['Febre', 'Tosse', 'Falta de Ar', 'Dor de Garganta', 'Raio-X Alterado', 'Coriza', 'Duração dos sintomas']
doencas_possiveis = ['Gripe', 'Resfriado', 'Covid-19', 'Bronquite', 'Pneumonia']

# Tabelas auxiliares
categorico_multinomial = {
    'seca': {'seca': 1.0, 'produtiva': 0.5, 'nao': 0.0},
    'produtiva': {'seca': 0.5, 'produtiva': 1.0, 'nao': 0.0},
    'nao': {'seca': 0.0, 'produtiva': 0.0, 'nao': 1.0}
}

categorico_ordenado = {'nao': 0, 'leve' : 1, 'moderado': 2, 'severo': 3}

# Gerar 50 casos aleatórios
casos = []
for _ in range(50):
    caso = {
        'Febre': random.choice(['sim', 'nao']), # categórico binário
        'Tosse': random.choice(['seca', 'produtiva', 'nao']), # categórico multinomial
        'Falta de Ar': random.choice(['nao', 'leve', 'moderado', 'severo']), # categórico ordenado
        'Cansaço': random.choice(['nao', 'leve', 'moderado', 'severo']),
        'Dor de Garganta': random.choice(['sim', 'nao']),
        'Raio-X Alterado': random.choice(['sim', 'nao']),
        'Coriza': random.choice(['sim', 'nao']),
        'Duração dos sintomas': random.randint(1, 14), # numérico inteiro
        'diagnostico': random.choice(doencas_possiveis)
    }
    casos.append(caso)

# Pesos padrão
pesos_default = {
    'Febre': .5,
    'Tosse': .5,
    'Falta de Ar': .8,
    'Cansaço': .4,
    'Dor de Garganta': .3,
    'Raio-X Alterado': .75,
    'Coriza': .25,
    'Duração dos sintomas': .5
}

def entrada_usuario():
    print("\n--- Entrada do Caso Atual ---")
    entrada = {}
    entrada['Febre'] = input("Febre (sim/nao): ").strip().lower()
    entrada['Tosse'] = input("Tosse (seca/produtiva/nao): ").strip().lower()
    entrada['Falta de Ar'] = input("Falta de Ar (nao/leve/moderado/severo): ").strip().lower()
    entrada['Cansaço'] = input("Cansaço (nao/leve/moderado/severo): ").strip().lower()
    entrada['Dor de Garganta'] = input("Dor de Garganta (sim/nao): ").strip().lower()
    entrada['Raio-X Alterado'] = input("Raio-X Alterado (sim/nao): ").strip().lower()
    entrada['Coriza'] = input("Coriza (sim/nao): ").strip().lower()
    entrada['Duração dos sintomas'] = int(input("Duração dos sintomas (em dias): ").strip())
    return entrada

def similaridade(c1, c2, pesos):
    score = 0
    total_peso = sum(pesos.values())

    for atributo in atributos:
        peso = pesos[atributo]
        v1 = c1[atributo]
        v2 = c2[atributo]

        if atributo == 'Tosse': # similaridade multinomial
            sim = categorico_multinomial[v1][v2]
        elif atributo == 'Falta de Ar' or atributo == 'Cansaço': # similaridade ordenada
            diff = abs(categorico_ordenado[v1] - categorico_ordenado[v2])
            sim = 1 - (diff / 3)  # 3 é o máximo possível
        elif atributo == 'Duração dos sintomas': # similaridade gaussiana
            sigma = 3.0  # desvio padrão pode ser ajustado conforme o domínio
            sim = math.exp(-((v1 - v2) ** 2) / (2 * sigma ** 2))
        else: # similaridade binária
            sim = 1.0 if v1 == v2 else 0.0 

        score += peso * sim

    return (score / total_peso) * 100

def exibir_resultados(entrada, pesos, casos):
    resultados = []
    for idx, caso in enumerate(casos):
        sim = similaridade(entrada, caso, pesos)
        resultados.append((idx, sim, caso['diagnostico'], caso))

    resultados.sort(key=lambda x: x[1])

    print("\n\n=== Resultado da Comparação ===")
    print("📌 Caso de entrada:")
    for a in atributos:
        print(f"- {a.replace('_', ' ').capitalize()}: {entrada[a]}")

    print("\n🔍 Casos similares (ordem decrescente por similaridade):\n")
    for idx, sim, diag, caso in resultados:
        print(f"🔹 Similaridade: {sim:.2f}% | Diagnóstico: {diag}")
        for a in atributos:
            print(f"   {a.replace('_', ' ').capitalize()}: {caso[a]}")
        print("-" * 40)

def alterar_pesos(pesos):
    print("\n--- Pesos Padrão ---")
    for atributo, peso in pesos.items():
        print(f"{atributo:<20}: {peso}")
    if input("\nDeseja alterar os pesos? (s/n): ").lower() == 's':
        for atributo in pesos:
            try:
                novo_peso = float(input(f"Novo peso para '{atributo}' (padrão = {pesos[atributo]}): ").strip())
                pesos[atributo] = novo_peso
            except:
                print("⚠️ Entrada inválida. Peso mantido.")
    return pesos

if __name__ == "__main__":
    print("📋 RBC - Diagnóstico de Doenças Respiratórias (com variáveis adaptadas)")
    pesos = alterar_pesos(pesos_default.copy())
    entrada = entrada_usuario()
    exibir_resultados(entrada, pesos, casos)
