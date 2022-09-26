'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classe de monômios matemáticos

Jerônimo de Abreu Afrange

https://www.cuemath.com/algebra/monomial/

'''

class Monomio:
	'''
	Representa um monômio matemático.
	
	Exemplos: 2x, 3xy, 4x^2, 7xyz, -3x^2yz

	'''


	def __init__(self, expoentes, coeficiente=1):
		'''
		Instancializa a classe Monomio.

		Parâmetros:
		- expoentes: dict[str(var) -> int(exp)], associa cada variável a um expoente;
		- coeficiente: valor numérico que multiplica a coisa toda.

		'''		

		# amarra os argumentos à instância de Monomio
		self.expoentes = expoentes
		self.coeficiente = coeficiente

		# propriedades auxiliares
		self.variaveis = set(expoentes.keys())
		self.identidade = Monomio.extrair_identidade(expoentes)


	def calcular(self, valores):
		'''
		Calcula o valor numérico do monômio para valores específicos das variáveis.

		Parâmetros:
		- valores: dict[str(var) -> num(valor)], determina o valor de cada variável

		Retorna o valor numérico do monômio para os valores das variáveis dados.

		'''

		# variável de retorno
		resultado = self.coeficiente

		# multiplica cada valor elevado à respectiva potência
		for variavel in self.variaveis:
			expoente = self.expoentes[variavel]
			valor = valores[variavel]
			resultado *= valor ** expoente

		return resultado


	@staticmethod
	def extrair_identidade(expoentes):
		'''
		Extrai a identidade do monômio a partir do dicinário dos expoentes.

		A utilidade disso é facilitar o agrupamento de monômios que podem ser
		combinados em um só, apenas somando os coeficientes.

		Parâmetros:
		- expoentes: dict[str(var) -> int(exp)], associa cada variável a um expoente

		Retorna uma string na forma "V1E1V2E2V3E3V4E4..."

		'''

		# valor de retorno
		identidade = str()

		# faz uma lista ordenada das variáveis, para consistência
		variaveis = list(expoentes.keys())
		variaveis.sort()

		# define a identidade do monômio, para facilitar combinar monômios
		for variavel in variaveis:
			identidade += variavel
			identidade += str(expoentes[variavel])

		return identidade


	def __str__(self):
		''' Overload da função de cast de string '''
		return str(self.coeficiente) + self.identidade









