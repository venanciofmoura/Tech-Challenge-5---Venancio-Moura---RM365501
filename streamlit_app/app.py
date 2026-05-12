"""
🌟 Passos Mágicos – Previsão de Risco de Defasagem
Aplicação Streamlit para identificação de alunos em risco
Desenvolvido para o Datathon FIAP PosTech 2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Passos Mágicos – Risco de Defasagem",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .main-header h1 { color: #F39C12; font-size: 2.2rem; margin: 0; }
    .main-header p { color: #ECF0F1; margin: 0.5rem 0 0 0; font-size: 1.1rem; }
    
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 1.2rem;
        border-left: 5px solid #3498DB;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
    }
    .metric-card.risco { border-left-color: #E74C3C; }
    .metric-card.ok { border-left-color: #27AE60; }
    
    .risk-high {
        background: linear-gradient(135deg, #E74C3C, #C0392B);
        color: white; padding: 1.5rem; border-radius: 12px;
        text-align: center; font-size: 1.4rem; font-weight: bold;
        margin: 1rem 0;
    }
    .risk-low {
        background: linear-gradient(135deg, #27AE60, #229954);
        color: white; padding: 1.5rem; border-radius: 12px;
        text-align: center; font-size: 1.4rem; font-weight: bold;
        margin: 1rem 0;
    }
    .risk-medium {
        background: linear-gradient(135deg, #F39C12, #D68910);
        color: white; padding: 1.5rem; border-radius: 12px;
        text-align: center; font-size: 1.4rem; font-weight: bold;
        margin: 1rem 0;
    }
    
    .info-box {
        background: #EBF5FB;
        border: 1px solid #3498DB;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .stSlider label { font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# TREINAMENTO DO MODELO (executado quando pkl está desatualizado)
# ============================================================
def train_and_save_model(model_path, meta_path):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import roc_auc_score, f1_score

    # Localiza o Excel na pasta pai ou na pasta atual
    base_dir = os.path.dirname(__file__)
    candidates = [
        os.path.join(base_dir, '..', 'BASE DE DADOS PEDE 2024 DATATHON.xlsx'),
        os.path.join(base_dir, 'BASE DE DADOS PEDE 2024 DATATHON.xlsx'),
    ]
    xlsx_path = next((p for p in candidates if os.path.exists(p)), None)
    if xlsx_path is None:
        raise FileNotFoundError("Arquivo 'BASE DE DADOS PEDE 2024 DATATHON.xlsx' não encontrado.")

    def load_year(df, year):
        if year == 2022:
            df = df.rename(columns={'INDE 22':'INDE','Pedra 22':'Pedra','Atingiu PV':'Ponto_Virada',
                                     'Defas':'Defasagem','Fase ideal':'Fase_Ideal','Gênero':'Genero'})
            df['IPP'] = np.nan
        df['Fase_Num'] = pd.to_numeric(df.get('Fase_Ideal', df.get('Fase_Num', np.nan)), errors='coerce')
        cols = ['INDE','IAA','IEG','IPS','IDA','IPV','IAN','IPP','Defasagem','Fase_Num']
        for c in cols:
            if c not in df.columns:
                df[c] = np.nan
        return df[cols].copy()

    FEATURES = ['IAA','IEG','IPS','IDA','IPV','IAN','IPP',
                'IDA_IEG_ratio','gap_auto','ips_ida_prod','Fase_Num']

    def build_features(df):
        f = df.copy()
        f['em_risco'] = (
            (f['Defasagem'].fillna(0) <= -2) |
            (f['INDE'].fillna(7) < 6.0) |
            (f['IDA'].fillna(6) < 5.0)
        ).astype(int)
        f['IDA_IEG_ratio'] = f['IDA'] / (f['IEG'] + 0.01)
        f['gap_auto']      = f['IAA'] - f['IDA']
        f['ips_ida_prod']  = f['IPS'] * f['IDA']
        return f

    xl = pd.ExcelFile(xlsx_path)
    raw22 = pd.read_excel(xl, sheet_name=xl.sheet_names[0])
    raw23 = pd.read_excel(xl, sheet_name=xl.sheet_names[1])
    raw24 = pd.read_excel(xl, sheet_name=xl.sheet_names[2])

    feat22 = build_features(load_year(raw22, 2022))
    feat23 = build_features(load_year(raw23, 2023))
    feat24 = build_features(load_year(raw24, 2024))

    train = pd.concat([feat22, feat23], ignore_index=True)
    test  = feat24.copy()
    X_train, y_train = train[FEATURES], train['em_risco']
    X_test,  y_test  = test[FEATURES],  test['em_risco']

    pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler',  StandardScaler()),
        ('clf',     RandomForestClassifier(n_estimators=300, max_depth=8,
                                           class_weight='balanced', random_state=42, n_jobs=-1))
    ])
    pipe.fit(X_train, y_train)
    y_pred  = pipe.predict(X_test)
    y_proba = pipe.predict_proba(X_test)[:, 1]

    # Retreina no dataset completo para produção
    all_data = pd.concat([feat22, feat23, feat24], ignore_index=True)
    pipe.fit(all_data[FEATURES], all_data['em_risco'])
    joblib.dump(pipe, model_path)

    meta = {
        "model_name": "Random Forest Classifier",
        "feature_columns": FEATURES,
        "roc_auc_test": round(roc_auc_score(y_test, y_proba), 4),
        "f1_test":      round(f1_score(y_test, y_pred), 4),
        "target":       "Defasagem<=-2 OR INDE<6.0 OR IDA<5.0"
    }
    with open(meta_path, 'w') as f:
        json.dump(meta, f, indent=2)

    return pipe, meta


# ============================================================
# CARREGAMENTO DO MODELO
# ============================================================
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'modelo_risco_defasagem.pkl')
    meta_path  = os.path.join(os.path.dirname(__file__), 'modelo_metadata.json')

    # Tenta carregar pkl existente; se falhar (versão incompatível), retreina
    try:
        model = joblib.load(model_path)
        # Teste rápido para detectar incompatibilidade de versão
        model.predict_proba(pd.DataFrame([[7,7,7,7,7,7,7,1,0,49,4]],
                            columns=['IAA','IEG','IPS','IDA','IPV','IAN','IPP',
                                     'IDA_IEG_ratio','gap_auto','ips_ida_prod','Fase_Num']))
        with open(meta_path, 'r') as f:
            meta = json.load(f)
        return model, meta
    except Exception:
        pass  # Fallback: retreina com scikit-learn local

    model, meta = train_and_save_model(model_path, meta_path)
    return model, meta

try:
    model, meta = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error(f"Erro ao carregar/treinar modelo: {e}")

FEATURE_COLS = [
    'IAA','IEG','IPS','IDA','IPV','IAN','IPP',
    'IDA_IEG_ratio','gap_auto','ips_ida_prod','Fase_Num'
]

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="main-header">
    <h1>⭐ Passos Mágicos</h1>
    <p>Sistema Preditivo de Risco de Defasagem Educacional</p>
    <p style="font-size:0.9rem; opacity:0.8;">Desenvolvido com Machine Learning | FIAP PosTech Datathon 2026</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    page = st.radio("🗂️ Navegação",
                    ["🎯 Previsão Individual", "📈 Dashboard"])

    st.markdown("---")

    if model_loaded:
        st.success("✅ Modelo carregado com sucesso")

    st.markdown("""
    **📖 Como usar:**
    1. Preencha os indicadores do aluno
    2. Clique em "Calcular Risco"
    3. Veja a probabilidade e recomendações

    **⚠️ Definição de Risco:**
    - Defasagem ≤ -2 fases, OU
    - INDE < 6.0 (abaixo de Ágata), OU
    - IDA < 5.0 (desempenho baixo)
    """)

# ============================================================
# PÁGINA 1: PREVISÃO INDIVIDUAL
# ============================================================
if page == "🎯 Previsão Individual":
    st.markdown("## 🎯 Previsão de Risco – Aluno Individual")
    st.markdown("Preencha os indicadores abaixo para calcular a probabilidade de risco de defasagem.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📚 Indicadores Acadêmicos")
        IDA = st.slider("IDA – Indicador de Aprendizagem", 0.0, 10.0, 6.5, 0.1,
                        help="Média das notas de aprendizagem do aluno")
        IAN = st.slider("IAN – Adequação ao Nível", 0.0, 10.0, 7.0, 0.1,
                        help="Indica se o aluno está adequado à sua fase")
        IPP = st.slider("IPP – Psicopedagógico", 0.0, 10.0, 7.0, 0.1,
                        help="Avaliação psicopedagógica do aluno")
        
        st.markdown("### 💪 Indicadores de Engajamento")
        IEG = st.slider("IEG – Engajamento", 0.0, 10.0, 7.5, 0.1,
                        help="Grau de engajamento nas atividades")
        IPV = st.slider("IPV – Ponto de Virada", 0.0, 10.0, 7.5, 0.1,
                        help="Indicador de ponto de virada do aluno")
    
    with col2:
        st.markdown("### 🧠 Indicadores Psicossociais")
        IPS = st.slider("IPS – Psicossocial", 0.0, 10.0, 6.5, 0.1,
                        help="Indicador psicossocial do aluno")
        IAA = st.slider("IAA – Autoavaliação", 0.0, 10.0, 7.0, 0.1,
                        help="Média das notas de autoavaliação")
        
        st.markdown("### 🏫 Informações da Fase")
        Fase_Num = st.selectbox("Fase do Aluno", 
                                 options=[0,1,2,3,4,5,6,7,8],
                                 format_func=lambda x: f"{'ALFA' if x==0 else f'Fase {x}'}",
                                 index=3)
        
    # Features derivadas
    IDA_IEG_ratio = IDA / (IEG + 0.01)
    gap_auto = IAA - IDA
    ips_ida_prod = IPS * IDA
    
    # Botão de predição
    st.markdown("---")
    if st.button("🔮 Calcular Risco de Defasagem", type="primary", use_container_width=True):
        if model_loaded:
            # Preparar input
            X_input = pd.DataFrame([[IAA, IEG, IPS, IDA, IPV, IAN, IPP,
                                      IDA_IEG_ratio, gap_auto, ips_ida_prod, float(Fase_Num)]],
                                    columns=FEATURE_COLS)
            
            proba = model.predict_proba(X_input)[0][1]
            pred = model.predict(X_input)[0]
            
            # Resultado
            st.markdown("---")
            st.markdown("## 📊 Resultado da Análise")
            
            if proba >= 0.7:
                st.markdown(f"""
                <div class="risk-high">
                    ⚠️ ALTO RISCO DE DEFASAGEM<br>
                    <span style="font-size:2rem;">{proba*100:.1f}%</span><br>
                    <span style="font-size:0.9rem;">Probabilidade de risco</span>
                </div>
                """, unsafe_allow_html=True)
                st.error("**Recomendação:** Intervenção imediata necessária. Revisar plano pedagógico e suporte psicossocial.")
            elif proba >= 0.4:
                st.markdown(f"""
                <div class="risk-medium">
                    🔔 RISCO MODERADO<br>
                    <span style="font-size:2rem;">{proba*100:.1f}%</span><br>
                    <span style="font-size:0.9rem;">Probabilidade de risco</span>
                </div>
                """, unsafe_allow_html=True)
                st.warning("**Recomendação:** Monitoramento próximo. Verificar indicadores de engajamento e desempenho.")
            else:
                st.markdown(f"""
                <div class="risk-low">
                    ✅ BAIXO RISCO<br>
                    <span style="font-size:2rem;">{proba*100:.1f}%</span><br>
                    <span style="font-size:0.9rem;">Probabilidade de risco</span>
                </div>
                """, unsafe_allow_html=True)
                st.success("**Recomendação:** Aluno com bom prognóstico. Manter acompanhamento regular.")


# ============================================================
# PÁGINA 2: DASHBOARD
# ============================================================
elif page == "📈 Dashboard":
    st.markdown("## 📈 Dashboard Analítico – Passos Mágicos")
    
    # Dados de referência (estatísticas do programa)
    stats_data = {
        'Ano': [2022, 2023, 2024],
        'N_Alunos': [860, 1014, 1156],
        'INDE_Medio': [7.04, 7.34, 7.40],
        'IDA_Medio': [6.09, 6.66, 6.35],
        'IEG_Medio': [7.89, 8.70, 7.37],
        'Pct_Defasados': [69.9, 54.4, 46.2],
        'Pct_AmTop': [55.6, 65.8, 68.0]
    }
    df_stats = pd.DataFrame(stats_data)
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Alunos 2024", "1.156", "+14,0% vs 2023")
    col2.metric("📊 INDE Médio 2024", "7.40", "+0.06 vs 2023")
    col3.metric("✅ Sem Defasagem", "53.8%", "+8.2 p.p. vs 2023")
    col4.metric("💎 Ametista + Topázio", "68.0%", "+2.2 p.p. vs 2023")
    
    st.markdown("---")
    col_l, col_r = st.columns(2)
    
    with col_l:
        st.markdown("### 📈 Evolução do INDE e IDA")
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(df_stats['Ano'], df_stats['INDE_Medio'], 'o-', color='#3498DB',
                linewidth=2.5, markersize=8, label='INDE')
        ax.plot(df_stats['Ano'], df_stats['IDA_Medio'], 's-', color='#E74C3C',
                linewidth=2.5, markersize=8, label='IDA')
        ax.plot(df_stats['Ano'], df_stats['IEG_Medio'], '^-', color='#27AE60',
                linewidth=2.5, markersize=8, label='IEG')
        for _, row in df_stats.iterrows():
            ax.annotate(f"{row['INDE_Medio']:.2f}", (row['Ano'], row['INDE_Medio']),
                       textcoords="offset points", xytext=(0,8), ha='center', fontsize=9, color='#3498DB')
        ax.set_xticks([2022,2023,2024]); ax.set_ylim(5,10)
        ax.legend(); ax.grid(alpha=0.3)
        ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
        st.pyplot(fig); plt.close()
    
    with col_r:
        st.markdown("### 📉 Redução da Defasagem ao Longo dos Anos")
        fig, ax = plt.subplots(figsize=(8, 4))
        colors_bar = ['#2196F3','#4CAF50','#FF5722']
        bars = ax.bar(df_stats['Ano'], df_stats['Pct_Defasados'],
                      color=colors_bar, edgecolor='white', width=0.6)
        for bar, pct in zip(bars, df_stats['Pct_Defasados']):
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
                    f'{pct:.1f}%', ha='center', fontsize=12, fontweight='bold')
        ax.set_ylabel('% Alunos Defasados'); ax.set_ylim(0, 85)
        ax.set_xticks([2022,2023,2024])
        ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
        st.pyplot(fig); plt.close()
    
    st.markdown("---")
    col_l2, col_r2 = st.columns(2)
    
    with col_l2:
        st.markdown("### 💎 Evolução por Classificação (Pedra)")
        pedra_data = {
            'Pedra': ['Quartzo','Ágata','Ametista','Topázio'],
            '2022': [15.3, 29.1, 40.5, 15.1],
            '2023': [7.1, 24.3, 37.6, 22.9],
            '2024': [9.7, 19.5, 33.9, 28.2]
        }
        df_pedra = pd.DataFrame(pedra_data)
        fig, ax = plt.subplots(figsize=(8, 4))
        x = np.arange(4); w = 0.25
        colors = ['#2196F3','#4CAF50','#FF5722']
        for j, (yr, color) in enumerate(zip(['2022','2023','2024'], colors)):
            ax.bar(x+j*w, df_pedra[yr], w, label=yr, color=color, edgecolor='white')
        ax.set_xticks(x+w); ax.set_xticklabels(df_pedra['Pedra'])
        ax.set_ylabel('% Alunos'); ax.legend()
        ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
        st.pyplot(fig); plt.close()
    
    with col_r2:
        st.markdown("### 🎯 Crescimento do Programa")
        fig, ax = plt.subplots(figsize=(8, 4))
        bars = ax.bar([2022,2023,2024], df_stats['N_Alunos'],
                      color=colors_bar, edgecolor='white', width=0.6)
        for bar, n in zip(bars, df_stats['N_Alunos']):
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+5,
                    f'{n:,}', ha='center', fontsize=12, fontweight='bold')
        ax.set_ylabel('Número de Alunos'); ax.set_ylim(0, 1400)
        ax.set_xticks([2022,2023,2024])
        ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
        st.pyplot(fig); plt.close()


