# Projeto de Contagem de Ocorrências de Palavras e Sinônimos

Neste projeto de curso, estou aplicando o pensamento computacional para resolver o problema de contar o 
número de ocorrências de uma palavra e seus sinônimos em um corpus de documentos de texto. A solução desse 
problema é uma parte fundamental de muitas tarefas de análise de texto, como avaliar o sentimento ou o humor 
do conteúdo de mídia social de uma pessoa ou resumir uma coleção de e-mails ou análises de produtos.

Na Parte 1, aplicamos os pilares do pensamento computacional para decompor esse problema em dois problemas 
menores e, em seguida, usamos o reconhecimento de padrões para encontrar pontos em comum entre os problemas, 
usamos a representação e a abstração de dados para identificar os dados necessários e desenvolvemos um algoritmo simples.

Nesta parte do projeto, você deve criar o fluxograma para esse algoritmo, aprofundando-o e detalhando-o 
mais do que na Parte 1, agora que exploramos uma variedade de algoritmos comuns.

> ℹ️ **NOTE:** O arquivo PDF do fluxograma está incluído neste repositório. Verifique o arquivo [fluxograma.pdf](output/fluxograma.pdf) para visualizar o fluxograma detalhado.

## Termos Utilizados:

- **Palavra-chave:** a palavra a ser pesquisada.
- **Thesaurus:** uma coleção de entradas, cada uma das quais consiste em uma palavra e uma coleção 
correspondente chamada Sinônimos, que é uma coleção de uma ou mais palavras.
- **Corpus:** uma coleção de documentos, cada um dos quais é uma coleção de palavras.

## Estrutura do Fluxograma:

1. **Encontrar os sinônimos no dicionário de sinônimos**
2. **Contar o número de ocorrências da palavra-chave e seus sinônimos no corpus**

### Parte 1: Encontrar os Sinônimos

1. **Iniciar:** Comecei com uma coleção de termos de pesquisa que inclui apenas a palavra-chave.
2. **Examinar o Thesaurus:** Para cada entrada no Thesaurus:
   - Se a palavra na entrada for igual à palavra-chave:
     - Adicione os sinônimos dessa entrada à coleção de termos de pesquisa.

### Parte 2: Contar as Ocorrências

1. **Inicializar Contadores:** Para cada termo na coleção de termos de pesquisa, criar um contador e começar em 0.
2. **Examinar o Corpus:**
   - Para cada documento no Corpus:
     - Para cada palavra no documento:
       - Se a palavra for igual a algum termo na coleção de termos de pesquisa:
         - Aumentar o contador desse termo em 1.
3. **Emitir Resultados:** Mostrar quantas vezes cada termo apareceu no Corpus.

### Passo a Passo

#### Parte 1: Encontrar os Sinônimos

1. **Iniciar:**
   - Comecei com uma coleção de termos de pesquisa que inclui apenas a palavra-chave.

2. **Examinar o Thesaurus:**
   - Para cada entrada no Thesaurus:
     - Se a palavra na entrada for igual à palavra-chave:
       - Adicione os sinônimos dessa entrada à coleção de termos de pesquisa.

#### Parte 2: Contar as Ocorrências

1. **Inicializar Contadores:**
   - Para cada termo na coleção de termos de pesquisa, criar um contador e começar em 0.

2. **Examinar o Corpus:**
   - Para cada documento no Corpus:
     - Para cada palavra no documento:
       - Se a palavra for igual a algum termo na coleção de termos de pesquisa:
         - Aumentar o contador desse termo em 1.

3. **Emitir Resultados:**
   - Mostrar quantas vezes cada termo apareceu no Corpus.

### Desenhando o Fluxograma

#### Estrutura do Fluxograma

1. **Início:** Representado por um oval.
2. **Passos de Processo:** Representados por retângulos.
   - **Iniciar coleção de termos de pesquisa:** Coloque a palavra-chave.
   - **Inicializar contadores:** Para cada termo.
3. **Decisões:** Representadas por losangos.
   - **Se a palavra no Thesaurus for igual à palavra-chave:** Adicionar sinônimos.
   - **Se a palavra no documento for igual ao termo de pesquisa:** Aumentar contador.
4. **Setas:** Conectar os passos, mostrando o fluxo do processo.
5. **Finais:** Representados por um oval.

