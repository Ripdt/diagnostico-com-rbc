# 🤖 IA - Trabalho de Raciocínio Baseado em Casos (RBC) - Filipi da Costa e Nathália Greiffo

## 📚 Sumário

- [IA - Trabalho de Raciocínio Baseado em Casos (RBC)](#-ia---trabalho-de-raciocínio-baseado-em-casos-rbc)
  - [🔧 Etapa 1: Escolher o Tema do RBC](#-etapa-1-escolher-o-tema-do-rbc)
  - [🧠 Etapa 2: Modelagem do Sistema RBC](#-etapa-2-modelagem-do-sistema-rbc)
  - [🚀 Etapa 3: Como Executar o Código](#-etapa-3-como-executar-o-código)

## 🔧 Etapa 1: Escolher o Tema do RBC

**Tema escolhido:** Diagnóstico de carcinoma tireodiano

### 🔍 Atributos

- **Age:** Número da idade
- **Gender:** Feminino / Masculino
- **Smoking:** Sim / Não
- **Hx Smoking:** Sim / Não
- **Hx Radiothreapy:** Sim / Não
- **Physical Examination:** Normal / Single nodular goiter-left / Single nodular goiter-right / Multinodular goiter / Diffuse goiter
- **Adenopathy:** No / Right / Left / Extensive / Bilateral / Posterior

---

## 🧠 Etapa 2: Modelagem do Sistema RBC

**Objetivo:**  
Dado um novo caso (paciente com sintomas), buscar os casos mais parecidos em uma base e sugerir o diagnóstico mais similar, com base nos sintomas apresentados.

### 🗂️ Atributos do Caso (cada paciente)

```
| Atributo             | Peso |
|----------------------|------|
| Age                  | 0.8  |
| Gender               | 0.3  |
| Smoking              | 0.2  |
| Hx Smoking           | 0.1  |
| Hx Radiotherapy      | 1.0  |
| Physical Examination | 0.9  |
| Adenopathy           | 1.0  |
```

---

## ⚖️ Justificativa dos Pesos

Importância de cada sintoma no diagnóstico:

- ### 🧓 Age – Peso: 0.8

  > Pacientes mais jovens tendem a ter melhor prognóstico, enquanto pacientes acima de 55 anos têm maior risco de doença agressiva.

- ### 🚻 Gender – Peso: 0.3

  > Embora o carcinoma tireoidiano seja mais comum em mulheres, a presença em homens costuma ser associada a maior agressividade. Entretanto, seu valor preditivo isolado é limitado.

- ### 🚬 Smoking – Peso: 0.2

  > O tabagismo não é um fator causal direto bem estabelecido para câncer de tireoide, mas pode causar um prognóstico pior.

- ### 🔄 Hx Smoking (Histórico de tabagismo) – Peso: 0.1

  > Tem relevância menor do que o tabagismo atual, mas pode indicar exposição prolongada a fatores de risco.

- ### ☢️ Hx Radiotherapy – Peso: 1.0

  > O histórico de radioterapia cervical é um dos principais fatores de risco conhecidos para câncer de tireoide.

- ### 🩺 Physical Examination – Peso: 0.9

  > Presença de bócio nodular único ou múltiplo é altamente relevante. Nódulos solitários têm maior suspeita de malignidade do que bócios multinodulares. A localização (esquerda/direita) pode importar menos, mas o padrão de apresentação é crítico.

- ### 🧠 Adenopathy – Peso: 1.0
  > A aparição de linfonodos é altamente sugestiva de malignidade ou metástase linfática.

## Possíveis resultados

Os resultados consistem no tipo de carcinoma e o nível de risco do diagnóstico

- **Micropapillary Low**
- **Micropapillary Intermediate**
- **Papillary Low**
- **Papillary Intermediate**
- **Papillary High**
- **Follicular Low**
- **Follicular Intermediate**
- **Follicular High**
- **Hurthel cell Low**
- **Hurthel cell Intermediate**
- **Hurthel cell High**

---

## 🧮 Fórmula da Similaridade

A similaridade entre dois casos é calculada com base na correspondência dos atributos e seus respectivos pesos.

### 📐 Fórmula

$$
\text{Similaridade}(C_1, C_2) = \left( \frac{ \sum_{i=1}^{n} w_i \cdot \delta(a_i^{(1)}, a_i^{(2)}) }{ \sum_{i=1}^{n} w_i } \right) \times 100
$$

### 🧾 Legenda dos símbolos

- `C₁` e `C₂`: os dois casos a serem comparados
- `aᵢ(¹)` e `aᵢ(²)`: valor do atributo `i` em cada caso
- `wᵢ`: peso associado ao atributo `i`
- `δ(aᵢ(¹), aᵢ(²))`: função de similaridade do atributo (cálculos diferentes para cada tipo categóricos)
- `n`: número total de atributos

> O resultado é uma porcentagem de similaridade entre 0 e 100.

## 🚀 Etapa 3: Como Executar o Código

### 📁 Arquivo principal

O código principal do projeto está no arquivo:

```
carcinoma.py
```

### ▶️ Passo a passo para execução

1. **Clone ou baixe o repositório** em sua máquina:

```bash
   git clone https://github.com/Ripdt/diagnostico-com-rbc.git
   cd diagnostico-com-rbc
```

2.  **Verifique se você tem o Python instalado** (recomendado: Python 3.8 ou superior):

```
python --version
```

3. **Execute o script**:

```
python carcinoma.py
```
