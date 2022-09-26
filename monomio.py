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

		#--	--- VERIFICA A VALIDADE DOS ARGUMENTOS	---	---	---	---	---	---	---	---	---	---	---

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

		#--	---	---	---	---	---	---	--- ---	---	---	---	---	---	---	---	---	---	---	---	---	---

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
		identidade = str()
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
		self.coeficiente = coeficiente
		self.numero_variaveis = numero_variaveis


	def calcular(self, valores):
		'''
		Calcula o valor do monômio para determinados valores das variáveis.

		Parâmetros:
		- valores: dicionário [variável(str) -> valor(num)]

		Retorna o valor numérico.

		'''

		#--	--- VERIFICA A VALIDADE DOS ARGUMENTOS	---	---	---	---	---	---	---	---	---	---	---

		if not isinstance(valores, dict):
			raise TypeError('O argumento "valores" tem que ser um dicionário.')

		if len(valores) != self.numero_variaveis:
			raise ValueError('Número incorreto de variáveis recebido em "valores".')

		for variavel in valores.keys():
			if not isinstance(variavel, str):
				raise TypeError('As chaves do dicionário "valores" têm que ser strings.')
			if not (isinstance(valores[variavel], int) or isinstance(valores[variavel], float)):
				raise TypeError('Os valores do dicionário "valores" têm que ser numéricos.')
			if variavel not in self.variaveis:
				raise ValueError('Uma das variáveis não existe no monômio.')
		
		#--	---	---	---	---	---	---	--- ---	---	---	---	---	---	---	---	---	---	---	---	---	---

		# variável de retorno
		resultado = self.coeficiente

		# loop de variáveis
		for variavel in self.variaveis:
			expoente = self.expoentes[variavel]
			valor = valores[variavel]
			resultado *= valor ** expoente

		return resultado


	def combinar(self, other):
		''' Combina dois monômios de identidades iguais '''

		#--	--- VERIFICA A VALIDADE DOS ARGUMENTOS	---	---	---	---	---	---	---	---	---	---	---

		if not isinstance(other, Monomio):
			raise TypeError('O argumento "other" tem que ser uma instância de Monomio.')

		if self.identidade != other.identidade:
			raise ValueError('Os dois monômios têm identidades diferentes.')

		#--	---	---	---	---	---	---	--- ---	---	---	---	---	---	---	---	---	---	---	---	---	---

		# calcula o coeficiente do novo monômio
		coeficiente = self.coeficiente + other.coeficiente

		# formata as variáveis e expoentes
		variaveis = list()
		potencias = list()
		for variavel in self.expoentes.keys():
			potencia = self.expoentes[variavel]
			variaveis.append(variavel)
			potencias.append(potencia)

		# cria a nova instância de Monomio
		monomio_combinado = Monomio(variaveis, potencias, coeficiente)

		return monomio_combinado


	def __str__(self):
		''' Overload do cast de string '''
		return str(self.coeficiente) + self.identidade














