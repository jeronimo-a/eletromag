'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classe que representa monômios matemáticos

Jerônimo de Abreu Afrange

https://www.cuemath.com/algebra/monomial/

'''

class Monomio:
	''' Representa um monômio matemático '''


	def __init__(self, variaveis, potencias, coeficiente=1):
		'''
		Cria uma nova instância de Monomio.

		Parâmetros:
		- variaveis: lista de strings com os nomes das variáveis;
		- potencias: lista de ints maiores que zero com os expoentes das variáveis;
		- coeficiente: valor numérico, coeficiente do monômio

		'''

		#--	--- VERIFICA A VALIDADE DOS ARGUMENTOS	---	---	---	---	---	---	---	---	---	---	---	---	---	---	---	---

		if not (isinstance(variaveis, list) or isinstance(variaveis, tuple)):
			raise TypeError('O argumento "variaveis" tem que ser uma lista ou tupla.')

		if not (isinstance(potencias, list) or isinstance(potencias, tuple)):
			raise TypeError('O argumento "potencias" tem que ser uma lista ou tupla.')

		if not (isinstance(coeficiente, int) or isinstance(coeficiente, float)):
			raise TypeError('O argumento "coeficiente" tem que ser um valor numérico.')

		if len(set(variaveis)) != len(variaveis):
			raise ValueError('Existem variáveis repetidas em "variaveis".')

		for variavel in variaveis:
			if not isinstance(variavel, str):
				raise TypeError('As variáveis em "variaveis" devem ser strings.')

		if len(variaveis) != len(potencias):
			raise ValueError('As quantidades de variáveis e potências são diferentes.')

		for potencia in potencias:
			if not isinstance(potencia, int):
				raise TypeError('Os potências em "potencias" devem ser inteiros.')
			if potencia < 1:
				raise ValueError('Os potências em "potencias" têm que ser maior que zero.')

		#--	---	---	---	---	---	---	--- ---	---	---	---	---	---	---	---	---	---	---	---	---	---	---	---	---	---	---


		# converte os argumentos
		variaveis = list(variaveis)
		potencias = list(potencias)

		# cria o dicionário de cruzamento das variáveis com as potencias
		expoentes = dict()
		for i in range(len(variaveis)):
			expoentes[variaveis[i]] = potencias[i]

		# organiza as variáveis em ordem alfabética para facilitar a comparação de monômios
		variaveis.sort()

		# monta a identidade do monômio
		identidade = ''
		for variavel in variaveis:
			expoente = expoentes[variavel]
			identidade += variavel
			identidade += str(expoente)

		# determina o grau e o número de variáveis do monômio
		grau = sum(potencias)
		numero_variaveis = len(variaveis)

		# define as propriedades
		self.grau = grau
		self.variaveis = variaveis
		self.expoentes = expoentes
		self.identidade = identidade
		self.numero_variaveis = numero_variaveis














