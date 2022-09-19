'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classes de curvas parametrizadas

'''

class CurvaParametrizada2D:
	''' Classe que define uma curva parametrizada FIXA de duas dimensões '''


	def __init__(self, funcao_x, funcao_y):
		'''
		Inicializa uma nova curva parametrizada 2D.

		Parâmetros:
		- funcao_x: [função (num) -> num] do eixo x
		- funcao_y: [função (num) -> num] do eixo y

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
		x = self.funcao_x(t)
		y = self.funcao_y(t)
		ponto = (x, y)

		return ponto


	def calcular_derivada(self, t, resolucao=1e-6):
		'''
		Calcula numericamente o valor da derivada da posição da curva
		parametrizada em determinado valor do parâmetro.
		
		Parâmetros:
		- t: valor do parâmetro
		- resolucao: variação no parâmetro usada para calcular

		Retorna um vetor (tupla) de duas dimensões (x, y)

		'''

		# valor de retorno
		vetor = tuple()

		# cálculo da derivada de x
		valor_x = self.funcao_x(t)
		valor_xr = self.funcao_x(t + resolucao)
		derivada_x = (valor_xr - valor_x) / resolucao

		# cálculo da derivada de y
		valor_y = self.funcao_y(t)
		valor_yr = self.funcao_y(t + resolucao)
		derivada_y = (valor_yr - valor_y) / resolucao

		# definição do valor de retorno
		vetor = (derivada_x, derivada_y)

		return vetor



class CurvaParametrizada3D:
	''' Classe que define uma curva parametrizada FIXA de três dimensões '''


	def __init__(self, funcao_x, funcao_y, funcao_z):
		'''
		Inicializa uma nova curva parametrizada 3D.

		Parâmetros:
		- funcao_x: [função (num) -> num] do eixo x
		- funcao_y: [função (num) -> num] do eixo y
		- funcao_z: [função (num) -> num] do eixo z

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
		x = self.funcao_x(t)
		y = self.funcao_y(t)
		z = self.funcao_z(t)
		ponto = (x, y, z)

		return ponto


	def calcular_derivada(self, t, resolucao=1e-6):
		'''
		Calcula numericamente o valor da derivada da posição da curva
		parametrizada em determinado valor do parâmetro.
		
		Parâmetros:
		- t: valor do parâmetro
		- resolucao: variação no parâmetro usada para calcular

		Retorna um vetor (tupla) de três dimensões (x, y, z)

		'''

		# valor de retorno
		vetor = tuple()

		# cálculo da derivada de x
		valor_x = self.funcao_x(t)
		valor_xr = self.funcao_x(t + resolucao)
		derivada_x = (valor_xr - valor_x) / resolucao

		# cálculo da derivada de y
		valor_y = self.funcao_y(t)
		valor_yr = self.funcao_y(t + resolucao)
		derivada_y = (valor_yr - valor_y) / resolucao

		# cálculo da derivada de y
		valor_z = self.funcao_z(t)
		valor_zr = self.funcao_z(t + resolucao)
		derivada_z = (valor_zr - valor_z) / resolucao

		# definição do valor de retorno
		vetor = (derivada_x, derivada_y, derivada_z)

		return vetor







