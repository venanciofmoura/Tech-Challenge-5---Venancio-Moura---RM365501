# Datathon FIAP PosTech – Passos Mágicos 2026

## 📋 Sobre o Projeto

Análise de dados educacionais da **Associação Passos Mágicos** utilizando os dados do PEDE (Pesquisa Extensiva do Desenvolvimento Educacional) de 2022, 2023 e 2024.

**Objetivo:** Responder 11 perguntas analíticas sobre o desenvolvimento educacional de 3.030 alunos e construir um modelo preditivo de risco de defasagem.

---

## 📁 Estrutura dos Entregáveis

```
├── analise_exploratoria_passos_magicos.ipynb  # Notebook EDA (11 análises)
├── modelo_preditivo_risco_defasagem.ipynb     # Notebook ML
├── apresentacao_passos_magicos.pptx           # Apresentação gerencial (14 slides)
├── streamlit_app/
│   ├── app.py                                 # Aplicação Streamlit
│   ├── modelo_risco_defasagem.pkl             # Modelo treinado (Random Forest)
│   ├── modelo_metadata.json                   # Metadados do modelo
│   ├── requirements.txt                       # Dependências
│   └── .streamlit/config.toml                 # Tema do app
└── BASE DE DADOS PEDE 2024 DATATHON.xlsx      # Base de dados
```

---

## 🤖 Modelo de Machine Learning

**Algoritmo:** Random Forest Classifier  
**Features:** IAA, IEG, IPS, IDA, IPV, IAN, IPP + features derivadas  
**Target:** Aluno em risco (Defasagem ≤ -2 OU INDE < 6.0 OU IDA < 5.0)  

**Métricas no Teste (2024):**
- ROC-AUC: **0.9706**
- F1-Score: **0.8537**
- Accuracy: **92%**

---

## 🚀 Streamlit: https://venanciofmoura-tech-challenge-5.streamlit.app/

---

## 📊 Principais Resultados

- ✅ **Crescimento:** 860 → 1.156 alunos atendidos (+34%)
- ✅ **INDE subiu:** 7,04 → 7,40 (+5,1%)
- ✅ **Defasagem caiu:** 69,9% → 46,2% (-23,7 p.p.)
- ✅ **Ametista+Topázio:** 55,6% → 68,0% (+12,4 p.p.)
- ⚠️ **Atenção:** IDA e IEG caíram em 2024 – requer monitoramento

---

## 📦 Tecnologias Utilizadas

- Python 3.10 | pandas | scikit-learn | matplotlib | seaborn
- Jupyter Notebook | Streamlit | joblib
- Random Forest Classifier | Feature Engineering

---

**FIAP PosTech – Data Analytics | Maio 2026**
