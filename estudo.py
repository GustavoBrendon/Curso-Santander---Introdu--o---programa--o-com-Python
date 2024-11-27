""" Conceitos básicos da sintaxe em Python """

# No Python, a indentação (espaços ou tabulações no início de uma linha) é utilizada para delimitar blocos de código. 
# Diferente de outras linguagens que utilizam chaves ou palavras-chave, o Python utiliza a indentação para determinar o escopo das declarações. 
# Por exemplo: 

a=10
b=5

if a==b:
    # Bloco de código se a condição for verdadeira
    print("São iguais")
else:
    # Bloco de código se a condição for falsa
    print("São diferentes")
    
     
""" Comentários """

# Os comentários são linhas de texto no código que são ignoradas pelo interpretador do Python.
# Eles são utilizados para explicar ou documentar o código. 
# No Python, os comentários de uma única linha começam com o símbolo #, enquanto os comentários de várias linhas são delimitados por três aspas """ . 
# Por exemplo:

# Este é um comentário de uma única linha

"""
Este é um comentário
de várias linhas
"""


""" Sensibilidade a maiúsculas e minúsculas """

# Python distingue entre maiúsculas e minúsculas. Portanto, variável, Variável e VARIÁVEL são consideradas variáveis diferentes.

""" Ponto e vírgula """

# Diferente de outras linguagens, o Python não requer o uso de ponto e vírgula (;) ao final de cada instrução. 
# No entanto, se você desejar escrever várias instruções em uma única linha, pode separá-las com um ponto e vírgula. Por exemplo:
# instrucao1; instrucao2; instrucao3;

""" Uso de parênteses """

# Os parênteses são utilizados para agrupar expressões, definir funções e realizar chamadas a funções. Por exemplo:

a=1
b=2
c=3
resultado = (a + b) * c;


""" Inteiros (int) """

# Os números inteiros são aqueles que não têm parte decimal. Em Python, são representados simplesmente escrevendo o número sem aspas nem pontos decimais. Por exemplo:

idade = 25
quantidade = 100

""" Inteiros (int) """

# Os números flutuantes, também conhecidos como números de ponto flutuante, são aqueles que têm uma parte decimal. Em Python, são representados utilizando um ponto para separar a parte inteira da parte decimal. Por exemplo:

preço = 9.99
altura = 1.75

""" Cadeias de texto (strings) """

# As cadeias de texto, ou simplesmente cadeias, são sequências de caracteres encerradas entre aspas simples ('...') ou duplas ("..."). São utilizadas para representar texto em Python. Por exemplo:

nome = "Gustavo"
mensagem = 'Olá, Mundo!' 

# Você pode incluir caracteres especiais nas cadeias utilizando o caractere de escape \. 
# Por exemplo, para incluir aspas dentro de uma cadeia, você pode usar \' ou \". 
# Também pode utilizar a notação de tripla aspa ('''...''' ou """...""") para criar cadeias de várias linhas.

""" Booleanos """

# Os valores booleanos representam os valores de verdade: True (verdadeiro) e False (falso). 
# São comumente utilizados em expressões condicionais e operações lógicas. Por exemplo:

é_maior_de_idade = True; """ Os valores booleanos em Python começam com uma letra maiúscula: True e False. """
tem_desconto = False


""" Declaração e atribuição de variáveis """

# As variáveis são contêineres que nos permitem armazenar e manipular dados em nossos programas. 
# Para declarar e atribuir um valor a uma variável em Python, utilizamos o operador de atribuição =
# O nome da variável vai à esquerda do operador, e o valor que você deseja atribuir vai à direita. Por exemplo:

nome = "Gustavo"
idade = 25
altura = 1.75
é_estudante = True

# No exemplo, declaramos e atribuímos valores às variáveis nome, idade, altura e é_estudante.
#  O Python infere automaticamente o tipo de dados de cada variável com base no valor atribuído.
# Você também pode atribuir o mesmo valor a várias variáveis em uma única linha usando o operador de atribuição múltipla:

a = b = c = 10

# Escolher nomes descritivos para suas variáveis facilita a leitura e compreensão do código, 
# tanto para você quanto para outros desenvolvedores que possam trabalhar no mesmo projeto.

"""  Operadores """
""" Aritméticos """

# Os operadores aritméticos são utilizados para realizar operações matemáticas básicas. Os principais operadores aritméticos em Python são:

""" 
Soma (+): soma dois valores.
Subtração (-): subtrai o segundo valor do primeiro.
Multiplicação (*): multiplica dois valores.
Divisão (/): divide o primeiro valor pelo segundo e devolve um resultado de tipo flutuante.
Divisão inteira (//): divide o primeiro valor pelo segundo e devolve um resultado de tipo inteiro (a parte decimal é descartada).
Módulo (%): devolve o resto da divisão entre o primeiro valor e o segundo.
Exponenciação (**): eleva o primeiro valor à potência do segundo. """

a = 10
b = 3


soma = a + b   # 13
subtracao = a - b    # 7
multiplicacao = a * b    # 30
divisao = a / b   # 3.333333333
divisao_inteira = a // b   # 3
modulo = a % b   # 1
exponenciacao = a ** b   # 1000

""" De comparação """

# Os operadores de comparação são utilizados para comparar dois valores e devolvem um valor booleano (True ou False) segundo o resultado da comparação. 
# Os operadores de comparação em Python são:

""" 
Igual a (==): devolve True se ambos os valores são iguais.
Diferente de (!=): devolve True se os valores são diferentes.
Maior que (>): devolve True se o primeiro valor é maior que o segundo.
Menor que (<): devolve True se o primeiro valor é menor que o segundo.
Maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo.
Menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo. """

a = 10
b = 3

igual = a == b   # False
diferente = a != b   # True
maior_que = a > b   # True
menor_que = a < b   # False
maior_ou_igual = a >= b   # True
menor_ou_igual = a <= b   # False

""" Lógicos """

# Os operadores lógicos são utilizados para combinar expressões condicionais e avaliar múltiplas condições. Os operadores lógicos em Python são:

""" AND (and): devolve True se ambas as condições são verdadeiras.
OR (or): devolve True se ao menos uma das condições é verdadeira.
NOT (not): inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira. """

a = 10
b = 3

resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False 

# Python segue as regras de precedência de operadores, onde certos operadores têm prioridade sobre outros.
# Em geral, a precedência segue a ordem: parênteses, exponenciação, multiplicação/divisão, soma/subtração, operadores de comparação e operadores lógicos. 

"""  Estruturas de controle """
""" Estruturas condicionais """

# IF

# A estrutura if é utilizada para executar um bloco de código se uma condição for verdadeira. A sintaxe básica é a seguinte:

""" if condicao:
   # Bloco de código a executar se a condição for verdadeira
   instruções"""

# Exemplo: 
idade = 18
if idade >= 18:
   print ("Você é maior de idade.")

# Neste exemplo, se a variável idade for maior ou igual a 18, será executado o bloco de código dentro do if e será impressa a mensagem "Você é maior de idade."

# IF-ELSE
# A estrutura if-else nos permite especificar um bloco de código alternativo que será executado se a condição do if for falsa. A sintaxe básica é a seguinte:

idade = 15
if idade >= 18:
   print ("Você é maior de idade.")
else:
   print ("Você é menor de idade.")

# Neste exemplo, se a variável idade for maior ou igual a 18, será executado o bloco de código dentro do if e será impressa a mensagem "Você é maior de idade." 
# Caso contrário, será executado o bloco de código dentro do else e será impressa a mensagem "Você é menor de idade."

# IF-ELIF-ELSE
# A estrutura if-elif-else nos permite especificar múltiplas condições e blocos de código alternativos. 
# A sintaxe básica é a seguinte:
""" 
if condicao1:
   # Bloco de código a executar se a condicao1 for verdadeira
   instruções
elif condicao2:
   # Bloco de código a executar se a condicao2 for verdadeira
   instruções
else:
   # Bloco de código a executar se nenhuma condição anterior for verdadeira
   instruções """

# Exemplo:

nota = 85
if nota >= 90:
   print ("Excelente")
elif nota >= 80:
   print ("Muito bom")
elif nota >= 70:
   print ("Bom")
else:
   print ("Precisa melhorar")

# Neste exemplo, são avaliadas múltiplas condições em ordem. Se a variável nota for maior ou igual a 90, será impresso "Excelente".
#  Se não se cumprir a primeira condição, mas nota for maior ou igual a 80, será impresso "Muito bom". 
# Se não se cumprirem as condições anteriores, mas nota for maior ou igual a 70, será impresso "Bom". 
# Se nenhuma das condições anteriores for verdadeira, será executado o bloco else e será impresso "Precisa melhorar".
