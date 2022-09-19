'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classes de curvas parametrizadas

Jerônimo de Abreu Afrange

'''

class CurvaParametrizada2D:
	''' Classe que define uma curva parametrizada FIXA de duas dimensões '''


	def __init__(self, funcao_x, funcao_y):
		'''
		Inicializa uma nova curva parametrizada 2D.

		Parâmetros:
		- funcao_x: instância de Funcao1D do eixo x
		- funcao_y: instância de Funcao1D do eixo y

		'''

		# amarra os argumentos à instância da classe
		self.funcao_x = funcao_x
		self.funcao_y = funcao_y


	def calcular(self, t):
		'''
		Calcula a posição da curva parametrizada em determinado valor do parâmetro.

		Parâmetros:
		- t: valor do parâmetro

		Retorna um ponto (tupla) de duas dimensões (x, y)

		'''

		# valor de retorno
		ponto = tuple()

		# calcula os valores
		x = self.funcao_x.calcular(t)
		y = self.funcao_y.calcular(t)
		ponto = (x, y)

		return ponto


	def calcular_derivada(self, t, variacao=1e-6):
		'''
		Calcula numericamente o valor da derivada da posição da curva
		parametrizada em determinado valor do parâmetro.
		
		Parâmetros:
		- t: valor do parâmetro
		- variacao: variação no parâmetro usada para calcular

		Retorna um vetor (tupla) de duas dimensões (x, y)

		'''

		# valor de retorno
		vetor = tuple()

		# cálculo das derivadas
		derivada_x = self.funcao_x.calcular_derivada(t, variacao)
		derivada_y = self.funcao_y.calcular_derivada(t, variacao)

		# definição do valor de retorno
		vetor = (derivada_x, derivada_y)

		return vetor



class CurvaParametrizada3D:
	''' Classe que define uma curva parametrizada FIXA de três dimensões '''


	def __init__(self, funcao_x, funcao_y, funcao_z):
		'''
		Inicializa uma nova curva parametrizada 3D.

		Parâmetros:
		- funcao_x: instância de Funcao1D do eixo x
		- funcao_y: instância de Funcao1D do eixo y
		- funcao_z: instância de Funcao1D do eixo z

		'''

		# amarra os argumentos à instância da classe
		self.funcao_x = funcao_x
		self.funcao_y = funcao_y
		self.funcao_z = funcao_z


	def calcular(self, t):
		'''
		Calcula a posição da curva parametrizada em determinado valor do parâmetro.

		Parâmetros:
		- t: valor do parâmetro

		Retorna um ponto (tupla) de três dimensões (x, y, z)

		'''

		# valor de retorno
		ponto = tuple()

		# calcula os valores
		x = self.funcao_x.calcular(t)
		y = self.funcao_y.calcular(t)
		z = self.funcao_z.calcular(t)
		ponto = (x, y, z)

		return ponto


	def calcular_derivada(self, t, variacao=1e-6):
		'''
		Calcula numericamente o valor da derivada da posição da curva
		parametrizada em determinado valor do parâmetro.
		
		Parâmetros:
		- t: valor do parâmetro
		- variacao: variação no parâmetro usada para calcular

		Retorna um vetor (tupla) de três dimensões (x, y, z)

		'''

		# valor de retorno
		vetor = tuple()

		# cálculo das derivadas
		derivada_x = self.funcao_x.calcular_derivada(t, variacao)
		derivada_y = self.funcao_y.calcular_derivada(t, variacao)
		derivada_z = self.funcao_z.calcular_derivada(t, variacao)

		# definição do valor de retorno
		vetor = (derivada_x, derivada_y, derivada_z)

		return vetor







