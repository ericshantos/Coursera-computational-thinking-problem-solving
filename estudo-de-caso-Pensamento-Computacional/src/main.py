"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Módulo principal, repoonsável por execultar a aplicação.
"""

from so_palavras.so_palavras import separar_palavras
from constante.contantes import corpus, palavra_chave

def main():

  # Dicionário para armazenar as contagens
  contagens = {}

  for indice, item in enumerate(corpus):

    # Separa as palavras do texto em lista
    lista_palavras = separar_palavras(item)

    for chave, valores in palavra_chave.items():

      # Inicializa a contagem para a palavra-chave
      contagem_palavra_chave = lista_palavras.count(chave)

      # Inicializa a contagem total com a contagem da palavra-chave
      contagem_total = contagem_palavra_chave

      # Conta a quantidade de vezes que cada sinônimo aparece no texto
      for sinonimo in valores:

        contagem_sinonimo = lista_palavras.count(sinonimo.lower())

        contagem_total += contagem_sinonimo

      # Armazena a contagem total no dicionário de contagens
      contagens[chave] = contagem_total

    # Exibe as contagens
    print(f"No {indice + 1}° corpus, a palavras-chaves e seus sinônimos aparecem:\n")
          
    
    for chave, contagem in contagens.items():
        
      print(f'- {chave}: {contagem}')
    
    print("\n")


if __name__ == '__main__':
  main()