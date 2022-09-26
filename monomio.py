'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classe que representa monômios matemáticos

Jerônimo de Abreu Afrange

https://www.cuemath.com/algebra/monomial/

'''

class Monomio:
	''' Representa um monômio matemático '''


	def __init__(self, expoentes, coeficiente=1):
		'''
		Cria uma nova instância de Monomio.

		Parâmetros:
		- expoentes: dicionário [variável(str) -> expoente(int > 0)];
		- coeficiente: valor numérico, coeficiente do monômio

		'''

		#--	--- VERIFICA A VALIDADE DOS ARGUMENTOS	---	---	---	---	---	---	---	---	---	---	---

		if not isinstance(expoentes, dict):
			raise TypeError('O argumento "expoentes" tem que ser um dicionário.')

		if not (isinstance(coeficiente, int) or isinstance(coeficiente, float)):
			raise TypeError('O argumento "coeficiente" tem que ser um valor numérico.')

		for variavel in expoentes.keys():
			if not isinstance(variavel, str):
				raise TypeError('As chaves do dicionário "expoentes" têm que ser strings.')
			if not isinstance(expoentes[variavel], int):
				raise TypeError('Os valores do dicionário "expoentes" têm que ser inteiros.')
			if expoentes[variavel] < 1:
				raise ValueError('Os valores do dicionário "expoentes" têm que ser maiores que zero.')

		#--	---	---	---	---	---	---	--- ---	---	---	---	---	---	---	---	---	---	---	---	---	---

		# cria a lista de variáveis e ordena para criação da identidade
		variaveis = list(expoentes.keys())
		variaveis.sort()

		# monta a identidade do monômio
		identidade = str()
		for variavel in variaveis:
			expoente = expoentes[variavel]
			identidade += variavel
			identidade += str(expoente)

		# determina o grau e o número de variáveis do monômio
		grau = sum(expoentes.values())
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
		- valores: dicionário [variável(str) -> valor(num)];

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

		# cria a nova instância de Monomio
		monomio_combinado = Monomio(self.expoentes, coeficiente)

		return monomio_combinado


	def __str__(self):
		''' Overload do cast de string '''
		return str(self.coeficiente) + self.identidade














