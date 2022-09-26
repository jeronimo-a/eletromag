'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classe de polinômios matemáticos

Jerônimo de Abreu Afrange

https://www.cuemath.com/algebra/polynomials/

'''

from monomio import Monomio


class Polinomio:
	'''
	Representa um polinômio matemático.
	
	Exemplos: 2x + 2, 3xy + y, 4x^2 - 2x, 7xyz + xw, -3x^2yz + 2

	'''


	def __init__(self, monomios, constante=0):
		'''
		Instancializa a classe Polinomio.

		Parâmetros:
		- monomios: list[Monomio], monômios que compõem o polinômio;
		- constante: valor numérico independente.

		'''		

		# amarra os argumentos à instância de Monomio
		self.monomios = Polinomio.combinar_monomios(monomios)
		self.constante = float(constante)

		# propriedades auxiliares
		self.variaveis = Polinomio.combinar_variaveis(monomios)


	def calcular(self, valores):
		'''
		Calcula o valor numérico do polinômio para valores específicos das variáveis.

		Parâmetros:
		- valores: dict[str(var) -> num(valor)], determina o valor de cada variável

		Retorna o valor numérico do polinômio para os valores das variáveis dados.

		'''

		# variável de retorno
		resultado = self.constante

		# loop de adição ao resultado
		for monomio in self.monomios:
			resultado += monomio.calcular(valores)

		return resultado


	@staticmethod
	def combinar_monomios(monomios):
		'''
		Combina todos os monômios compatíveis dentro de uma lista.

		Parâmetros:
		- monomios: list[Monomio]

		Retorna uma lista de monômios.

		'''

		# valor de retorno
		monomios_combinados = list()

		# loop de identificação dos pares
		por_identidade = dict()
		for monomio in monomios:
			identidade = monomio.identidade
			try: por_identidade[identidade].append(monomio)
			except KeyError: por_identidade[identidade] = [monomio]

		# loop de combinação
		for identidade in por_identidade.keys():
			monomios_compativeis = por_identidade[identidade]
			expoentes = monomios_compativeis[0].expoentes
			monomio_acumulado = Monomio(expoentes, 0)
			for monomio in monomios_compativeis:
				monomio_acumulado = Monomio.combinar(monomio_acumulado, monomio)
			monomios_combinados.append(monomio_acumulado)

		return monomios_combinados


	@staticmethod
	def combinar_variaveis(monomios):
		'''
		Lista todas as variáveis presentes numa lista de monômios.

		Parâmetros:
		- monomios: list[Monomio]

		Retorna um set de strings.

		'''

		# valor de retorno
		variaveis = set()

		# loop de união
		for monomio in monomios:
			variaveis = variaveis.union(monomio.variaveis)

		return variaveis


	def __str__(self):
		''' Overload da função de cast de string '''
		string = str()
		for monomio in self.monomios:
			string += str(monomio)
			string += ' + '
		string += str(self.constante)
		return string








