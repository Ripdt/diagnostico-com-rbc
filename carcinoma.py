import math
import csv

# Atributos considerados para carcinoma tireoidiano
atributos = [
    'Age',
    'Gender',
    'Smoking',
    'Hx Smoking',
    'Hx Radiotherapy',
    'Physical Examination',
    'Adenopathy'
]

carcinomas_possiveis = [
    'Micropapillary Low', 'Micropapillary Intermediate',
    'Papillary Low', 'Papillary Intermediate', 'Papillary High',
    'Follicular Low', 'Follicular Intermediate', 'Follicular High',
    'Hurthel cell Low', 'Hurthel cell Intermediate', 'Hurthel cell High'
]

categorico_exame = {
    'normal': 0.0,
    'diffuse goiter': 0.3,
    'multinodular goiter': 0.6,
    'single nodular goiter-left': 0.8,
    'single nodular goiter-right': 0.8
}
categorico_adenopathy = {
    'no': 0.0,
    'posterior': 0.4,
    'right': 0.5,
    'left': 0.5,
    'bilateral': 0.8,
    'extensive': 1.0
}

pesos_default = {
    'Age': 0.8,
    'Gender': 0.3,
    'Smoking': 0.2,
    'Hx Smoking': 0.1,
    'Hx Radiotherapy': 1.0,
    'Physical Examination': 0.9,
    'Adenopathy': 1.0
}

def ler_casos_csv(caminho_arquivo):
    """
    Lê um arquivo CSV com os atributos do carcinoma tireoidiano e retorna uma lista de dicionários representando os casos.
    """
    casos = []
    with open(caminho_arquivo, mode='r', encoding='utf-8-sig') as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=';')
        for linha in leitor:
            try:
                caso = {
                    'Age': int(linha['Age']),
                    'Gender': linha['Gender'].strip().lower(),
                    'Smoking': linha['Smoking'].strip().lower(),
                    'Hx Smoking': linha['Hx Smoking'].strip().lower(),
                    'Hx Radiotherapy': linha['Hx Radiotherapy'].strip().lower(),
                    'Physical Examination': linha['Physical Examination'].strip().lower(),
                    'Adenopathy': linha['Adenopathy'].strip().lower(),
                    'diagnostico': linha['Pathology Risk'].strip()
                }
                casos.append(caso)
            except ValueError as e:
                continue
    return casos

def entrada_usuario():
    print("\n--- Entrada do Caso Atual ---")
    entrada = {}
    # Entrada de idade
    while True:
        try:
            entrada['Age'] = int(input("Idade: ").strip())
            break
        except ValueError:
            print("❌ Por favor, insira uma idade válida (número inteiro).")

    # Gênero
    while True:
        val = input("Gênero (F/M): ").strip().lower()
        if val in ['f', 'm']:
            entrada['Gender'] = val
            break
        print("❌ Entrada inválida. Digite 'F' ou 'M'.")

    opcoes_binarias = ['yes', 'no']

    # Smoking
    while True:
        val = input("Fumante? (Yes/No): ").strip().lower()
        if val in opcoes_binarias:
            entrada['Smoking'] = val
            break
        print("❌ Entrada inválida. Digite 'Yes' ou 'No'.")

    # Histórico de tabagismo
    while True:
        val = input("Histórico de tabagismo? (Yes/No): ").strip().lower()
        if val in opcoes_binarias:
            entrada['Hx Smoking'] = val
            break
        print("❌ Entrada inválida. Digite 'Yes' ou 'No'.")

    # Histórico de radioterapia
    while True:
        val = input("Histórico de radioterapia? (Yes/No): ").strip().lower()
        if val in opcoes_binarias:
            entrada['Hx Radiotherapy'] = val
            break
        print("❌ Entrada inválida. Digite 'Yes' ou 'No'.")

    # Exame físico
    opcoes_exame_fisico = [
        'Normal',
        'Single nodular goiter-left',
        'Single nodular goiter-right',
        'Multinodular goiter',
        'Diffuse goiter'
    ]
    print("\nOpções de Exame Físico:")
    for i, opcao in enumerate(opcoes_exame_fisico, 1):
        print(f" {i}. {opcao}")
    while True:
        val = input("Escolha uma opção (1 a 5): ").strip()
        if val.isdigit() and 1 <= int(val) <= len(opcoes_exame_fisico):
            entrada['Physical Examination'] = opcoes_exame_fisico[int(val) - 1].lower()
            break
        print("❌ Opção inválida. Escolha um número entre 1 e 5.")

    # Adenopatia
    opcoes_adenopatia = [
        'No', 'Right', 'Left', 'Extensive', 'Bilateral', 'Posterior'
    ]
    print("\nOpções de Adenopatia:")
    for i, opcao in enumerate(opcoes_adenopatia, 1):
        print(f" {i}. {opcao}")
    while True:
        val = input("Escolha uma opção (1 a 6): ").strip()
        if val.isdigit() and 1 <= int(val) <= len(opcoes_adenopatia):
            entrada['Adenopathy'] = opcoes_adenopatia[int(val) - 1].lower()
            break
        print("❌ Opção inválida. Escolha um número entre 1 e 6.")

    return entrada

def similaridade(c1, c2, pesos):
    score = 0
    total_peso = sum(pesos.values())

    print('similaridade')
    print(c1)
    print(c2)
    for atributo in atributos:
        print(atributo)
        peso = pesos[atributo]
        v1 = c1[atributo]
        v2 = c2[atributo]

        if atributo == 'Age': # categórico numérico - similaridade gaussiana
            sigma = 10.0 # desvio padrão pode ser ajustado conforme o domínio
            sim = math.exp(-((v1 - v2) ** 2) / (2 * sigma ** 2))
        elif atributo in ['Gender', 'Smoking', 'Hx Smoking', 'Hx Radiotherapy']: # categórico binário
            sim = 1.0 if v1 == v2 else 0.0
        elif atributo == 'Physical Examination': # categórico multinomial
            sim = 1.0 - abs(categorico_exame[v1] - categorico_exame[v2])
        elif atributo == 'Adenopathy': # categórico multinomial
            sim = 1.0 - abs(categorico_adenopathy[v1] - categorico_adenopathy[v2])

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
        print(f"- {a.replace('_', ' ').lower()}: {entrada[a]}")

    print("\n🔍 Casos similares (ordem decrescente por similaridade):\n")
    for idx, sim, diag, caso in resultados:
        print(f"🔹 Similaridade: {sim:.2f}% | Diagnóstico: {diag}")
        for a in atributos:
            print(f"   {a.replace('_', ' ').lower()}: {caso[a]}")
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
    casos = ler_casos_csv('Thyroid_Diff_adapted.csv')
    pesos = alterar_pesos(pesos_default.copy())
    entrada = entrada_usuario()
    exibir_resultados(entrada, pesos, casos)
