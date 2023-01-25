# def main():

# poem = (" De tudo, ao meu amor serei atento, Antes, e com tal zelo, e sempre, e tanto, Que mesmo em face do maior encanto, Dele se encante mais meu pensamento., Quero vivê-lo em cada vao momento, E em seu louvor hei de espalhar meu canto, E rir meu riso e derramar meu pranto, Ao seu pesar ou seu contentamento., E assim, quando mais tarde me procure, Quem sabe a morte, angustia de quem vive, Quem sabe a solidao, fim de quem ama, Eu possa me dizer do amorque tive: , Que nao seja imortal, posto que e chama, Mas que seja infinito enquanto dure.")

# poem.split()

import pytest


def test_separar_palavras():
    poem = (" De tudo, ao meu amor serei atento, Antes, e com tal zelo, e sempre, e tanto, Que mesmo em face do maior encanto, Dele se encante mais meu pensamento., Quero vive-lo em cada vao momento, E em seu louvor hei de espalhar meu canto, E rir meu riso e derramar meu pranto, Ao seu pesar ou seu contentamento., E assim, quando mais tarde me procure, Quem sabe a morte, angustia de quem vive, Quem sabe a solidao, fim de quem ama, Eu possa me dizer do amor que tive: , Que nao seja imortal, posto que e chama, Mas que seja infinito enquanto dure.")

    test_ = poem.split()
    print(test_)


def test_primeira():
    nome = "vanessa"
    resultado = list(nome)[0]
    assert resultado == "v"


# def test_palavras():
poem_lista = ['De', 'tudo,', 'ao', 'meu', 'amor', 'serei', 'atento,',
              'Antes,', 'e', 'com', 'tal', 'zelo,', 'e', 'sempre,',
              'e', 'tanto,', 'Que', 'mesmo', 'em', 'face', 'do',
              'maior', 'encanto,', 'Dele', 'se', 'encante', 'mais',
              'meu', 'pensamento.,', 'Quero', 'vive-lo', 'em', 'cada',
              'vao', 'momento,', 'E', 'em', 'seu', 'louvor', 'hei', 'de',
              'espalhar', 'meu', 'canto,', 'E', 'rir', 'meu', 'riso',
              'e', 'derramar', 'meu', 'pranto,', 'Ao', 'seu', 'pesar',
              'ou', 'seu', 'contentamento.,', 'E', 'assim,', 'quando',
              'mais', 'tarde', 'me', 'procure,', 'Quem', 'sabe', 'a',
              'morte,', 'angustia', 'de', 'quem', 'vive,', 'Quem',
              'sabe', 'a', 'solidao,', 'fim', 'de', 'quem', 'ama,',
              'Eu', 'possa', 'me', 'dizer', 'do', 'amor', 'que',
              'tive:', ',', 'Que', 'nao', 'seja', 'imortal,', 'posto',
              'que', 'e', 'chama,', 'Mas', 'que', 'seja', 'infinito', 'enquanto', 'dure.']
poema = poem_lista.sort()


for k in range(0, len(poem_list)):
    if (poema[k] == poema[k+1]):

        # numero_letras = poem_lista[1]
        # assert numero_letras == 2

        # print(len(test_poem_lista))
