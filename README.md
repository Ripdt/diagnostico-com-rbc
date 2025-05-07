# 🤖 IA - Trabalho de Raciocínio Baseado em Casos (RBC)

## 📚 Sumário

- [IA - Trabalho de Raciocínio Baseado em Casos (RBC)](#-ia---trabalho-de-raciocínio-baseado-em-casos-rbc)
  - [🔧 Etapa 1: Escolher o Tema do RBC](#-etapa-1-escolher-o-tema-do-rbc)
  - [🧠 Etapa 2: Modelagem do Sistema RBC](#-etapa-2-modelagem-do-sistema-rbc)
  - [🚀 Etapa 3: Como Executar o Código](#-etapa-3-como-executar-o-código)

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

---

## 🚀 Etapa 3: Como Executar o Código

### 📁 Arquivo principal
O código principal do projeto está no arquivo:
```
IA_RBC_Nathalia_Filipi.py
```

### ▶️ Passo a passo para execução

1. **Clone ou baixe o repositório** em sua máquina:

```bash
   git clone https://github.com/Ripdt/diagnostico-com-rbc.git
   cd diagnostico-com-rbc
   ```
   2. **Verifique se você tem o Python instalado** (recomendado: Python 3.8 ou superior):
```
python --version
```
3. **Execute o script** principal:
```
python IA_RBC_Nathalia_Filipi.py
```

