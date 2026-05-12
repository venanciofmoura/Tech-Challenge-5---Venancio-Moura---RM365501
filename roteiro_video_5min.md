# Roteiro – Vídeo de Apresentação (até 5 minutos)
## Datathon Passos Mágicos · FIAP PosTech Data Analytics · Maio 2026

> **Tempo total estimado:** 4min 30s – 5min  
> **Ritmo:** ~130 palavras por minuto. Fale com calma, não acelere.  
> **Formato sugerido:** tela cheia do PowerPoint + narração. Câmera opcional.  
> **Dica:** avance o slide ANTES de começar a falar sobre ele.

---

## SLIDE 1 — CAPA
**⏱ ~25 segundos**

Olá! Meu nome é Venancio, e esse é o meu projeto para o Datathon da FIAP PosTech, turma de Data Analytics.

O case é a **Associação Passos Mágicos** — uma ONG que transforma a vida de crianças e jovens de baixa renda em Embu-Guaçu através da educação.

O objetivo foi analisar três anos de dados do programa PEDE, responder 11 perguntas estratégicas sobre o desenvolvimento dos alunos, e construir um modelo preditivo de risco de defasagem.

---

## SLIDE 2 — AGENDA
**⏱ ~15 segundos**

A apresentação passa por cinco blocos: visão geral da base de dados, as principais análises exploratórias, o modelo de Machine Learning, a aplicação Streamlit, e as conclusões com recomendações.

---

## SLIDE 3 — VISÃO GERAL DOS DADOS
**⏱ ~40 segundos**

A base PEDE cobre 2022, 2023 e 2024 — de 860 alunos para **1.156**, um crescimento de 34%.

O INDE médio — que é o índice geral de desenvolvimento educacional — subiu de 7,04 para 7,40.

Mas o número que mais chama atenção: a **taxa de defasagem caiu de 69,9% para 46,2%** — uma queda de quase 24 pontos percentuais em dois anos. Isso é o impacto real do programa se traduzindo em dado.

---

## SLIDE 4 — IAN: DEFASAGEM
**⏱ ~30 segundos**

O IAN mede a adequação do aluno ao nível esperado. Em 2022, apenas 28,7% dos alunos estavam sem defasagem. Em 2024, esse número subiu para 53,8%.

A defasagem moderada e severa praticamente desapareceu. O IAN médio subiu 20% no período — de 6,4 para 7,7. Um dos resultados mais expressivos da análise.

---

## SLIDE 5 — IDA: DESEMPENHO ACADÊMICO
**⏱ ~30 segundos**

O desempenho acadêmico subiu 9,4% de 2022 para 2023 — e depois recuou 4,7% em 2024.

O INDE continuou subindo, o que indica que outros indicadores compensaram essa queda. Mas a trajetória do IDA em 2024 precisa de atenção — e esse dado vai ser importante no modelo preditivo.

---

## SLIDE 6 — IEG, IAA E IPS
**⏱ ~35 segundos**

Três correlações que se destacam nos dados de 2024.

O engajamento — IEG — tem correlação de 0,54 com o desempenho acadêmico E com o Ponto de Virada. Ou seja, **alunos mais engajados performam melhor e chegam mais longe no programa**.

Já a autoavaliação, com r de apenas 0,22, mostra que os alunos não têm percepção precisa do próprio desempenho. E o IPS praticamente não correlaciona com IDA em 2024 — r de 0,01 — o que é um achado que merece aprofundamento.

---

## SLIDE 7 — IPP, IPV E MULTIDIMENSIONALIDADE
**⏱ ~25 segundos**

Os indicadores que mais explicam o INDE são IDA, IEG e IPV — com correlações de 0,80, 0,79 e 0,76. Esses três juntos quase determinam o índice geral.

Um achado relevante: IPP e IAN têm correlação baixíssima entre si, o que confirma que o programa captura dimensões independentes do desenvolvimento — acadêmico e psicopedagógico.

---

## SLIDE 8 — EFETIVIDADE DO PROGRAMA
**⏱ ~20 segundos**

Em resumo: crescimento de 34% no número de alunos, 12,4 pontos percentuais a mais em Ametista e Topázio, defasagem caindo 23,7 p.p., e **10,6% dos alunos de 2024 indicados para bolsas**. Para um programa social, esses são resultados excepcionais.

---

## SLIDE 9 — MODELO DE MACHINE LEARNING
**⏱ ~45 segundos**

O modelo preditivo usa Random Forest com 300 árvores para classificar alunos em risco — definido como defasagem acima de duas fases, INDE abaixo de 6,0, ou IDA abaixo de 5,0.

Os resultados: **ROC-AUC de 0,97, F1-Score de 0,85 e acurácia de 92%**.

O indicador mais importante foi o IDA — responsável por 32,8% do poder preditivo. Em segundo lugar ficou a interação entre IPS e IDA — uma feature derivada. Isso faz sentido: um aluno com desempenho baixo *e* mal-estar psicossocial ao mesmo tempo é um sinal de alerta muito mais forte do que qualquer um dos dois isoladamente.

---

## SLIDE 10 — APLICAÇÃO STREAMLIT
**⏱ ~35 segundos**

Para colocar o modelo em uso prático, desenvolvi uma aplicação web com Streamlit com duas funcionalidades.

Na **previsão individual**, a equipe pedagógica insere os indicadores de um aluno e recebe em segundos a probabilidade de risco, uma classificação e uma orientação didática — sem precisar de código ou planilha.

No **dashboard analítico**, é possível acompanhar toda a evolução do programa de 2022 a 2024 com KPIs e gráficos interativos.

O deploy foi feito no Streamlit Community Cloud.

---

## SLIDE 11 — INSIGHTS E RECOMENDAÇÕES
**⏱ ~30 segundos**

Alguns achados adicionais: meninas têm INDE consistentemente maior, o que abre espaço para programas diferenciados. Quanto mais tempo o aluno fica no programa, melhor o INDE — r de 0,42 — argumento forte para investir em retenção.

E os alertas: o IEG caiu de 8,70 para 7,37 em 2024, e o IDA também recuou. Isso precisa ser investigado com os dados de 2025.

---

## SLIDE 12 — CONCLUSÕES E PRÓXIMOS PASSOS
**⏱ ~30 segundos**

Três conclusões centrais: **o programa funciona** — os números confirmam. **Engajamento é chave** — o IEG é o melhor preditor comportamental do Ponto de Virada. E **o modelo está pronto para produção** — com AUC de 0,97, ele pode ser usado hoje pela equipe pedagógica.

Os próximos passos são: deploy do app, capacitação da equipe, retreinamento semestral, e investigação da queda de IDA e IEG em 2024.

---

## SLIDE 13 — ENCERRAMENTO
**⏱ ~15 segundos**

Foi um projeto muito gratificante trabalhar com dados que têm impacto social real.

Obrigado pela atenção!

---

## CHECKLIST PRÉ-GRAVAÇÃO

- [ ] PPT em modo apresentação, tela principal
- [ ] Microfone testado e sem eco
- [ ] Notificações do computador desativadas
- [ ] Esse roteiro aberto em segundo monitor ou impresso
- [ ] Câmera focada (se for usar)
- [ ] Copo d'água por perto

## DICAS RÁPIDAS

**Pausa entre slides:** avance o slide e aguarde 1 segundo antes de falar — facilita a edição depois.  
**Erros:** se errar, pare, respire e repita o parágrafo inteiro — na edição é fácil cortar.  
**Ritmo:** fale mais devagar do que parece natural. Na reprodução sempre soa mais rápido.  
**Energia:** destaque os números com variação de voz — especialmente 0,97 de AUC, -24 p.p. de defasagem, e os 10,6% de bolsas. São os momentos de impacto.
