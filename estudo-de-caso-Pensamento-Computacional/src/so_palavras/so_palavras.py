"""
@Author: Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por separar as palavras em lista.
"""

import string

def separar_palavras(texto):

    # Remover a pontuação do texto
    texto_sem_pontuacao = texto.translate(str.maketrans('','', string.punctuation))

    # Converter o texto em minúsculas
    texto_sem_pontuacao = texto_sem_pontuacao.lower()

    # Separar o texto em palavras
    lista_palavras = texto_sem_pontuacao.split()

    return lista_palavras
