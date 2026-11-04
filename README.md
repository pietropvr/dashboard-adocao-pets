# Projeto: Dinâmica de Adoção de Animais de Estimação

## 1. Problema, Objetivo e Importância
**Pergunta:** Quais características dos animais (faixa etária, espécie, raça e sexo) mais influenciam a probabilidade de adoção num abrigo?   
**Objetivo:** Analisar o perfil dos animais adotados para identificar padrões que ajudam ou dificultam a adoção.
**Importância:**Abrigos e ONGs operam com recursos limitados. Entender estes dados ajuda a criar campanhas de adoção direcionadas para os animais que estatisticamente possuem menores taxas de adoção.

## 2. Escopo e Resultados Esperados
* **O que foi analisado:** Espécie, idade na adoção, raça e sexo.
* **O que está fora do escopo:** Dados médicos complexos ou identificação de adotantes (respeitando as diretrizes de privacidade).
* **Resultados esperados:** Gráficos que demonstram a taxa de adoção por espécie/idade e um painel interativo.

## 3. Fonte de Dados e Captura
* **Fonte:** Austin Animal Center Outcomes (via Kaggle / Dados Abertos).
* **Método de Captura:** Download de ficheiro público `.csv`.
* **Licença:** Domínio Público / Dados Abertos Governamentais.

## 4. Pipeline e Metodologia
* **Extração:** Leitura dos dados em formato CSV.
* **Transformação (ETL):** Limpeza de nulos, tradução de colunas e dados para português, conversão de datas e cálculo matemático da idade exata em dias e faixas etárias.
* **Análise (EDA):** Cálculo das taxas de adoção e distribuição dos desfechos.

## 5. Bibliotecas e Tecnologias
* **Pandas:** Para manipulação, limpeza e cálculo dos dados estruturados.
* **Matplotlib:** Para geração de gráficos estáticos durante a fase de análise exploratória.
* **Streamlit:** Para a criação do painel interativo de Business Intelligence (BI).

## 6. Resultados Encontrados e Conclusão
A análise demonstra que a espécie e a faixa etária são determinantes no desfecho. Cães e gatos lideram o volume de adoções, enquanto animais seniores ou com necessidades específicas apresentam menores taxas de adoção. A filtragem por sexo e raça no painel permite identificar nichos específicos (ex: filhotes de raças menores) que são adotados quase imediatamente.

## 7. Aplicação Profissional
Este pipeline pode ser implementado no sistema de gestão de uma ONG ou centro de zoonoses real. O painel interativo permite que os gestores aloquem recursos de marketing (ex: publicações em redes sociais) de forma estratégica, focando nos perfis de animais com menor saída histórica, otimizando o fluxo de adoções e reduzindo a sobrelotação.

## 8. Como Executar o Projeto
1. Clone este repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o script de ETL para processar os dados: `python src/transform.py`
4. Inicie o painel interativo: `streamlit run app.py`

*Nota: O ficheiro bruto `animais.csv` deve ser colocado na pasta `data/raw/` (não versionado no GitHub por segurança).*

## 9. Links de Entrega
* **Repositório Pessoal:** [https://github.com/pietropvr/dashboard-adocao-pets](https://github.com/pietropvr/dashboard-adocao-pets)
* **Aplicação Streamlit (Deploy):** [https://dashboard-adocao-pet.streamlit.app/](https://dashboard-adocao-pet.streamlit.app/)
