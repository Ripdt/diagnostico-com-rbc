# 🤖 IA - Trabalho de Raciocínio Baseado em Casos (RBC)

## 🔧 Etapa 1: Escolher o Tema do RBC
**Tema escolhido:** Diagnóstico de doenças respiratórias leves

### 🔍 Exemplo de Atributos
- **Febre:** Sim / Não  
- **Tosse:** Seca / Produtiva / Não  
- **Dor de garganta:** Sim / Não  
- **Cansaço:** Leve / Moderado / Severo  
- **Coriza:** Sim / Não  
- **Duração dos sintomas:** Número de dias  

---

## 🧠 Etapa 2: Modelagem do Sistema RBC

**Objetivo:**  
Dado um novo caso (paciente com sintomas), buscar os casos mais parecidos em uma base e sugerir o diagnóstico mais similar, com base nos sintomas apresentados.

### 🗂️ Atributos do Caso (cada paciente)
- Febre  
- Tosse  
- Dor de garganta  
- Cansaço  
- Coriza  
- Duração dos sintomas  

---

## ⚖️ Justificativa dos Pesos

Importância de cada sintoma no diagnóstico:

- **Febre** e **tosse** são mais indicativas de Covid ou gripe → peso **maior**  
- **Dor de garganta** e **coriza** são mais comuns, menos determinantes → peso **menor**

> Esses pesos poderão ser ajustados via interface!

---

## 🧮 Fórmula da Similaridade

Para cada atributo:

1. Calculamos a **similaridade local** (valor entre 0 e 1)  
2. Multiplicamos pelo **peso atribuído ao atributo**  
3. Calculamos a **média ponderada** para obter a similaridade total

