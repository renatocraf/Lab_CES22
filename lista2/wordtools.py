import string

def cleanword(palavra):
    palavra2 = ""

    for letra in palavra:
        if letra in string.ascii_letters:
            palavra2 = palavra2 + letra
    return palavra2


def has_dashdash(palavra):
    dashdash = "--"
    return (dashdash in palavra)


def extract_words(frase):
    frase = frase.lower()+ " "
    palavras = []
    palavra = ''
    for letra in frase:
        if letra in string.ascii_letters:
            palavra = palavra+letra
        elif letra in string.whitespace and palavra != "":
            palavras.append(palavra)
            palavra = ''
    # ate aqui ele adicionou todas a palavras, menos a ultima, ja que
    # nao aparece espaço em branco no fim da frase. com isso temos q dar
    # mais um append ###### outra alternativa foi adicionar um " " no final da frase!

    #palavras.append(palavra)

    return palavras

#print(extract_words("Eu sou Renato."))
#print(extract_words("Eu sou Renato.") ==
#      ['eu','sou','renato'])

#print(extract_words("Now is the time!  'Now', is the time? Yes, now."))
#print(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
#     ['now','is','the','time','now','is','the','time','yes','now'])

def wordcount(palavra, palavras):
    cont = 0
    for palavra2 in palavras:
        if palavra == palavra2:
            cont +=1
    return cont

#print(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)

def wordset(palavras):
    palavras2 = []
    for palavra in palavras:
        if not(palavra in palavras2):
            palavras2.append(palavra)
    palavras2.sort()
    return palavras2 

#print(wordset(["now", "is", "time", "is", "now", "is", "is"]))  

def longestword(palavras):
    tam = 0
    for palavra in palavras:
        if len(palavra)> tam:
            tam = len(palavra)
    return tam


