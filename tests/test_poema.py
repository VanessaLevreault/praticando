# def main():

# poem = (" De tudo, ao meu amor serei atento, Antes, e com tal zelo, e sempre, e tanto, Que mesmo em face do maior encanto, Dele se encante mais meu pensamento., Quero vivê-lo em cada vao momento, E em seu louvor hei de espalhar meu canto, E rir meu riso e derramar meu pranto, Ao seu pesar ou seu contentamento., E assim, quando mais tarde me procure, Quem sabe a morte, angustia de quem vive, Quem sabe a solidao, fim de quem ama, Eu possa me dizer do amorque tive: , Que nao seja imortal, posto que e chama, Mas que seja infinito enquanto dure.")

# poem.split()


def test_separar_palavras():
    poem = (" De tudo, ao meu amor serei atento, Antes, e com tal zelo, e sempre, e tanto, Que mesmo em face do maior encanto, Dele se encante mais meu pensamento., Quero vive-lo em cada vao momento, E em seu louvor hei de espalhar meu canto, E rir meu riso e derramar meu pranto, Ao seu pesar ou seu contentamento., E assim, quando mais tarde me procure, Quem sabe a morte, angustia de quem vive, Quem sabe a solidao, fim de quem ama, Eu possa me dizer do amor que tive: , Que nao seja imortal, posto que e chama, Mas que seja infinito enquanto dure.")

    test_ = poem.split()
    print(test_)


test_separar_palavras()

test_poem_lista = ['De', 'tudo,', 'ao', 'meu', 'amor', 'serei', 'atento,',
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

print(len(test_poem_lista))
