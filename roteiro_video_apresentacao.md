# Roteiro – Vídeo de Apresentação  
## Datathon Passos Mágicos 2026 · FIAP PosTech Data Analytics

> **Duração estimada:** 7–8 minutos  
> **Formato sugerido:** screenshare do PowerPoint com narração em câmera ou voz over  
> **Dica:** fale em ritmo natural, sem pressa. Pause entre slides (~1 segundo de silêncio ajuda na edição).

---

## 🎬 SLIDE 1 — CAPA
**⏱ ~30 segundos**

Olá! Meu nome é Venancio, e esse é o meu projeto para o Datathon da FIAP PosTech, turma de Data Analytics.

O tema é a **Associação Passos Mágicos** — uma organização sem fins lucrativos que transforma a vida de crianças e jovens de baixa renda em Embu-Guaçu, através da educação.

A proposta aqui foi mergulhar na base de dados PEDE — o sistema de avaliação deles —, extrair insights estratégicos sobre o programa, e construir um modelo preditivo para identificar alunos em risco de defasagem escolar.

---

## 🎬 SLIDE 2 — AGENDA
**⏱ ~20 segundos**

Vou estruturar a apresentação em cinco blocos:

Começo com a base de dados, mostro as principais análises exploratórias, o modelo de machine learning, a aplicação Streamlit que construí, e encerro com as conclusões e recomendações.

Vamos lá.

---

## 🎬 SLIDE 3 — VISÃO GERAL DOS DADOS
**⏱ ~50 segundos**

A base de dados PEDE cobre três anos: **2022, 2023 e 2024**, com 860, 1.014 e 1.156 alunos respectivamente — um crescimento de 34% no período.

O INDE, que é o Índice de Desenvolvimento Educacional, subiu de 7,04 para 7,40 ao longo dos anos — uma evolução consistente.

Mas o dado mais expressivo está aqui: a **taxa de defasagem escolar caiu de 69,9% para 46,2%** entre 2022 e 2024. Quase uma redução de 24 pontos percentuais em dois anos. Isso é a efetividade do programa se traduzindo em número.

E a proporção de alunos nas pedras mais avançadas — Ametista e Topázio — subiu de 55,6% para 68%. O programa não apenas reduz o atraso, ele promove progressão.

---

## 🎬 SLIDE 4 — IAN: DEFASAGEM
**⏱ ~45 segundos**

Entrando nas análises exploratórias, começo pelo IAN — o indicador de adequação ao nível, que mede a defasagem.

Esse gráfico mostra a distribuição por nível de defasagem em cada ano. A barra teal escura são os alunos **sem defasagem** — repara como ela cresce ano a ano: de 28,7% em 2022 para **53,8% em 2024**.

A defasagem moderada e severa quase desapareceram em 2024. Em 2022, 23,6% dos alunos estavam com defasagem moderada ou severa. Em 2024, são apenas 8,1%.

O IAN médio subiu de 6,4 para 7,7 — um incremento de 20%. Esse indicador por si só já é evidência forte da efetividade pedagógica do programa.

---

## 🎬 SLIDE 5 — IDA: DESEMPENHO ACADÊMICO
**⏱ ~45 segundos**

O IDA — desempenho acadêmico — teve uma trajetória interessante. Subiu de 6,09 para 6,66 entre 2022 e 2023, uma alta de quase 10%. Mas em 2024 caiu para 6,35.

Olhando o IEG — engajamento — a queda foi ainda mais visível: de 8,70 em 2023 para 7,37 em 2024.

Isso é um sinal que merece atenção. Pode refletir uma mudança de metodologia de avaliação, um efeito pós-pandemia no perfil dos alunos novos, ou realmente uma queda de engajamento que o programa precisa investigar.

O INDE continuou subindo, o que indica que outros indicadores compensaram — mas o monitoramento do IDA e do IEG em 2025 vai ser crucial.

---

## 🎬 SLIDE 6 — IEG, IAA E IPS
**⏱ ~50 segundos**

Aqui vemos três indicadores juntos: IEG, IAA e IPS.

Um dos achados mais importantes desse slide é a correlação entre **IPS e IDA em 2024: r = 0,01**. Praticamente zero. Isso significa que o indicador psicossocial, na forma como está sendo medido, não se correlaciona com o desempenho acadêmico nesse período.

Isso pode ter várias explicações: o IPS pode capturar dimensões importantes mas mais difíceis de operacionalizar, ou pode haver uma defasagem temporal no efeito.

Já o IEG mostra correlações mais consistentes: r = 0,54 com IDA e r = 0,54 com o Ponto de Virada. Ou seja, **alunos mais engajados apresentam melhor desempenho e chegam ao Ponto de Virada com mais frequência**.

---

## 🎬 SLIDE 7 — IPP, IPV E MULTIDIMENSIONALIDADE
**⏱ ~50 segundos**

Esse slide mostra as correlações de cada indicador com o INDE — o índice geral — em 2024.

O resultado é revelador: **IDA lidera com r = 0,80**, seguido de IEG com 0,79 e IPV com 0,76. Esses três juntos explicam a maior parte da variação do INDE.

Um achado que corrige uma intuição comum: a correlação entre IPP e IAN é baixíssima — r entre 0,10 e 0,15. Isso mostra que a avaliação psicopedagógica e a adequação ao nível escolar são dimensões essencialmente independentes. O programa captura aspectos multidimensionais do desenvolvimento do aluno — e isso é uma força do modelo PEDE.

Menos de 1% dos alunos têm avaliações contraditórias entre IPP e IAN — o que indica consistência pedagógica alta.

---

## 🎬 SLIDE 8 — EFETIVIDADE DO PROGRAMA
**⏱ ~45 segundos**

Esse slide consolida a efetividade do programa através da distribuição por Pedra ao longo dos anos.

Em 2022, 15,3% dos alunos estavam na Pedra Quartzo — o nível mais básico. Em 2024, caiu para 10,6%. No outro extremo, a Topázio — o nível mais avançado — saiu de 15,1% para **30,9%**. Quase dobrou.

Os alunos na Ametista ou Topázio juntos passaram de 55,6% para 68% — e **10,6% dos alunos de 2024 foram indicados para bolsas universitárias**. Isso, para um programa que atende crianças de baixa renda, é transformador.

---

## 🎬 SLIDE 9 — MODELO DE MACHINE LEARNING
**⏱ ~75 segundos**

Agora o coração técnico do projeto: o modelo preditivo de risco de defasagem.

O objetivo era construir um classificador que identificasse proativamente quais alunos têm maior probabilidade de estar em situação de risco — definida como: defasagem moderada ou severa, INDE abaixo de 6,0, ou IDA abaixo de 5,0.

Esses limiares não foram escolhas arbitrárias. Foram calibrados nos dados: defasagem ≤ -2 afeta 14,1% dos alunos, INDE < 6,0 afeta 11,1%, e IDA < 5,0 afeta 22,3% — cada um identificando o quartil ou decil inferior das distribuições observadas.

O algoritmo escolhido foi o **Random Forest com 300 árvores**, com engenharia de features para capturar interações entre indicadores. Os resultados foram expressivos: **ROC-AUC de 0,97, F1-Score de 0,85, Acurácia de 92%**.

O indicador mais importante para o modelo foi o IDA, com 32,8% de importância. Em segundo, o produto entre IPS e IDA — uma feature derivada que captura a interação entre bem-estar e desempenho. Isso faz sentido pedagógico: um aluno com IDA baixo e IPS baixo é um sinal de alerta muito mais forte do que qualquer um dos dois isolados.

---

## 🎬 SLIDE 10 — APLICAÇÃO STREAMLIT
**⏱ ~50 segundos**

Para tornar o modelo acessível à equipe pedagógica, desenvolvi uma aplicação web usando Streamlit, com duas funcionalidades principais.

A **Previsão Individual** permite que um coordenador insira os 11 indicadores de um aluno e receba em segundos a probabilidade de risco, uma classificação e uma recomendação pedagógica personalizada. Sem precisar de código, sem planilha — direto no navegador.

O **Dashboard Analítico** oferece uma visão consolidada da evolução do programa 2022–2024: KPIs de INDE e defasagem, distribuição por Pedra, e tendências por indicador.

O app foi desenvolvido com Python, scikit-learn e Streamlit, e pode ser publicado no Streamlit Community Cloud de forma gratuita.

---

## 🎬 SLIDE 11 — INSIGHTS E RECOMENDAÇÕES
**⏱ ~50 segundos**

Alguns insights adicionais que emergiram da análise exploratória:

As **meninas têm INDE ligeiramente superior** em todas as coortes analisadas — o que pode indicar oportunidade para programas diferenciados por gênero.

O **tempo no programa correlaciona positivamente com o INDE** — r = 0,42. Isso é um argumento forte para investir em retenção e continuidade dos alunos.

A **queda do IEG de 8,70 para 7,37 em 2024** é um sinal de alerta que merece investigação prioritária — seja por mudança de perfil dos alunos novos, mudança curricular ou outro fator.

E o dado sobre **bolsas**: alunos indicados têm INDE médio 0,8 pontos maior. Expandir o programa de bolsas pode ser uma das alavancas de maior impacto.

---

## 🎬 SLIDE 12 — CONCLUSÕES E PRÓXIMOS PASSOS
**⏱ ~55 segundos**

Três conclusões centrais:

Primeiro: **o programa funciona**. INDE subiu 5%, defasagem caiu 24 pontos percentuais, Topázios quase triplicaram em dois anos. Os dados confirmam o impacto.

Segundo: **engajamento é chave**. A correlação r = 0,54 entre IEG e o Ponto de Virada mostra que alunos engajados chegam mais longe. Estratégias que aumentem o IEG têm retorno direto no INDE.

Terceiro: **o modelo está pronto para produção**. Com AUC de 0,97 e F1 de 0,85, a ferramenta pode ser usada hoje pela equipe pedagógica para identificação precoce de risco.

O alerta real é a queda de IDA e IEG em 2024 — isso precisa ser monitorado com os dados de 2025 quando estiverem disponíveis.

Como próximos passos: deploy do app, capacitação da equipe no uso do modelo, retreinamento semestral com dados novos, e investigação das causas da queda de IDA e IEG.

---

## 🎬 SLIDE 13 — ENCERRAMENTO
**⏱ ~25 segundos**

Bom, é isso!

Foi um projeto muito gratificante — analisar dados de um programa com impacto social real, e contribuir com uma ferramenta que pode de fato apoiar decisões pedagógicas.

Obrigado pela atenção, e fico à disposição para perguntas.

---

## 📋 CHECKLIST ANTES DE GRAVAR

- [ ] PPTX aberto no modo apresentação, tela principal
- [ ] Câmera ou gravação de tela configurada
- [ ] Microfone testado
- [ ] Fone de ouvido para evitar eco (se usar câmera)
- [ ] Anotações desse roteiro abertas em segundo monitor ou impresso
- [ ] Fechar notificações do computador (modo não-perturbe)
- [ ] Testar resolução antes de gravar o final

## 🎙 DICAS DE GRAVAÇÃO

**Ritmo:** fale mais devagar do que parece natural — na reprodução sempre parece mais rápido.

**Pausas:** ao trocar de slide, faça uma pausa curta antes de começar a falar. Facilita a edição.

**Erros:** se errar uma frase, pare, respire e repita o parágrafo inteiro. Na edição é fácil cortar a parte ruim.

**Energia:** mostre entusiasmo pelos resultados — especialmente na seção do modelo e nas conclusões. Você construiu algo que realmente funciona.

**Olhar:** se estiver usando câmera, olhe para a lente ao fazer as afirmações mais importantes, não para a tela.
