import re #Regular Expressions

#"""encontrar as posições de padroes dentro de uma #string, se estes estiverem presentes( metodo SEARCH )
#
#Encontrar se o começo de uma string é igual a um determinado padrãpo ( metodo MATCH )

#Encontrar todas as substrings em uma string que correspondam a um padrão ( metodo FINDALL )


#. - Qualquer caractere (exceto linha nova )
#\w - qualquer caractere alfanumerico
#\W - qualquer caractere nao-alfanumerico
#\d - qualquer caractere que seja um digito
#\D - qualquer caractere que nao seja um digito
#\s - espa;o em branco
#^ - começa com x
#$ - termina com x
#"\" - usado antes de metacaracteres para especificar seu significado literal



#quantificadores

#[] - opcional entre os que estao dentro dos colchetes
#() - captura grupo de caracteres
#* - de zero a mais vezes
#? - zero ou uma vez
#+ - uma ou main vezes
#{m , n } - de m a n vezes
#| - ou 

#EXEMPLO:
#    joaovitorsilva@gmail.com
#
#    \w+@\w+\.\w+
#
#    \w+ = joaovitorsilva
#    @ = @
#    \w+ = gmail
#    \. = .
#    \w+ = com"""


#usando o re.search para ver se esta dentro da frase
print("=-" * 10)\

frase = "Ola! , meu numero e (81)90000-0000"
regex = r'\(\d{2}\)\d{4,5}-\d{4}' 

resultado = re.search(regex , frase)
print(resultado)

frase = "A placa  do carro que eu anotei  foi FTR-9238"
regex = r'[A-Z]{3}-\d{4}'
resultado = re.search(regex , frase)
print(resultado)

print("=-" * 10)

#utilizando o re.match para ver se esta no comeco da frase
frase = "A placa  do carro que eu anotei  foi FTR-9238"
regex = r'[A-Z]{3}-\d{4}'
resultado = re.match(regex , frase)
print(resultado)

print("=-" * 10)

#utilizando o re.findall para colocar em uma lista em qualquer posicao da frase
frase = "A placa  do carro que eu anotei  foi FTR-9238 a antiga era HFG-7162"
regex = r'[A-Z]{3}-\d{4}'
resultado = re.findall(regex , frase)
print(resultado)