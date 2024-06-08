<h1 align="center">Aplicando os pilares do pensamento computacional</h1>

## Problema:

Com o aumento exponencial da quantidade de dados disponíveis na World Wide Web, extrair conhecimento útil 
desses dados tornou-se um desafio significativo. Esse desafio pode ser abordado utilizando o pensamento 
computacional. O problema específico é identificar a frequência de uma palavra-chave e seus sinônimos em 
um corpus de documentos.

### Os principais componentes deste problema são:

- **Palavra-chave**: A palavra específica para a qual a pesquisa será realizada.
- **Thesaurus**: Um conjunto de palavras, cada uma associada a seus sinônimos.
- **Corpus**: Um conjunto de documentos, cada um contendo várias palavras.

## Objetivo:

Determinar o número de ocorrências da palavra-chave e seus sinônimos em todos os 
documentos do corpus.

### Simplificações e Considerações:

Ignorar capitalização, pontuação e correspondência parcial de palavras.
Não considerar variações ou grafias alternativas das palavras.

### Cenários de Aplicação:

- Análise de publicações em mídias sociais para avaliar bem-estar e saúde mental.
- Análise de e-mails para identificar tópicos frequentemente discutidos.
- Avaliação de feedback de clientes para determinar sentimentos positivos ou negativos.
- Análise de palavras usadas em mídias sociais para entender a disseminação de doenças.
- Estudo da evolução do uso de palavras ou frases ao longo do tempo por pesquisadores em linguística.

## Indagações:

***Usando a decomposição, quais são os principais subproblemas que precisam ser resolvidos para solucionar o problema geral?***

 - Identificação e definição dos componentes: definir a palavra-chave, construir ou obter o thesaurus com a 
   palavra-chave e seus sinônimos, coletar e organizar o corpus de documentos.

 - Preparação e limpeza dos dados: normalizar os textos (remoção de pontuação, converter para minúsculas), estruturar 
   os dados para fácil acesso e manipulação, e desenvolvimento de um algoritmo de busca, criar uma função para contar 
   ocorrências da palavra-chave e seus sinônimos em cada documento, iterar por todos os documentos no corpus aplicando a 
   função de contagem.

 - Agregação dos resultados: somar as contagens individuais de cada documento para obter o total de ocorrências.

**Usando o reconhecimento de padrões, que padrões o senhor vê na solução, ou seja, que processos precisam ser repetidos?**

 - Identificação de sinônimos: Usar o thesaurus para mapear a palavra-chave aos seus sinônimos,

 - Estrutura dos documentos: aproveitar a estrutura repetitiva dos documentos (e-mails, postagens,etc.) para otimizar a busca.

**Usando a abstração e a representação de dados, como o senhor representaria o tesauro, o corpus e cada um dos documentos do corpus?**

 - thesaurus: seria representado por um dicionário, cuja chave seria a palavra-chave e o valor agregado, os sinônimos.
 - corpus: seriam agrupados em uma lista, de forma a serem alocados para serem processados.

**Usando os resultados dos três primeiros pilares, qual é o algoritmo que o senhor usaria para resolver esse problema? Descreva-o com o máximo de detalhes possível.**

 1. Salva o corpus em um objeto;
 2. Estruturar os dados para facilitar o acesso e manipulação (separar o texto em palavras e remover a pontuação);
 3. Acessar o corpus;
 4. Ler o conteúdo do corpus;
 5. Se indentificada a palavra-chave ou um de seus sinônimos no conteúdo, interar sobre a variável contador. Caso não, continue a ler o conteúdo;
 6. Exibe o resultado do ocorrência da palavra-chave no corpus.