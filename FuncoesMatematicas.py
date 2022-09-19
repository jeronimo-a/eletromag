'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classes de funções matemáticas simples

Jerônimo de Abreu Afrange

'''

class Funcao1D:
	''' Classe que define uma função FIXA de uma variável '''
	

	def __init__(self, funcao):
		'''
		Inicializa uma nova função matemática de uma variável.

		Parâmetros:
		- funcao: função python [num -> num]

		'''
		
		# define o método de cálculo
		self.calcular = funcao


	def calcular_derivada(self, x, variacao=1e-6):
		'''
		Calcula numericamente o valor da derivada da função
		
		Parâmetros:
		- x: valor da variável independente
		- variacao: variação na variável em questão usada para calcular

		Retorna um float do valor da derivada

		'''

		# valor de retorno
		derivada = float()

		# cálculo da derivada
		valor = self.calcular(x)
		valor_res = self.calcular(x + variacao)
		derivada = (valor_res - valor) / variacao

		return derivada



class Funcao2D:
	''' Classe que define uma função FIXA de duas variáveis '''
	

	def __init__(self, funcao):
		'''
		Inicializa uma nova função matemática de duas variáveis.

		Parâmetros:
		- funcao: função python [(num, num) -> num]

		'''
		
		# define o método de cálculo
		self.calcular = funcao


	def calcular_derivada_parcial_x(self, x, y, variacao=1e-6):
		'''
		Calcula numericamente o valor da derivada parcial da função em x
		
		Parâmetros:
		- x: valor da variável independente x
		- y: valor da variável independente y
		- variacao: variação na variável em questão usada para calcular

		Retorna um float do valor da derivada

		'''

		# valor de retorno
		derivada = float()

		# cálculo da derivada
		valor = self.calcular(x, y)
		valor_res = self.calcular(x + variacao, y)
		derivada = (valor_res - valor) / variacao

		return derivada


	def calcular_derivada_parcial_y(self, x, y, variacao=1e-6):
		'''
		Calcula numericamente o valor da derivada parcial da função em y
		
		Parâmetros:
		- x: valor da variável independente x
		- y: valor da variável independente y
		- variacao: variação na variável em questão usada para calcular

		Retorna um float do valor da derivada

		'''

		# valor de retorno
		derivada = float()

		# cálculo da derivada
		valor = self.calcular(x, y)
		valor_res = self.calcular(x, y + variacao)
		derivada = (valor_res - valor) / variacao

		return derivada



class Funcao3D:
	''' Classe que define uma função FIXA de três variáveis '''


	def __init__(self, funcao):
		'''
		Inicializa uma nova função matemática de três variáveis.

		Parâmetros:
		- funcao: função python [(num, num, num) -> num]

		'''
		
		# define o método de cálculo
		self.calcular = funcao


	def calcular_derivada_parcial_x(self, x, y, z, variacao=1e-6):
		'''
		Calcula numericamente o valor da derivada parcial da função em x
		
		Parâmetros:
		- x: valor da variável independente x
		- y: valor da variável independente y
		- z: valor da variável independente z
		- variacao: variação na variável em questão usada para calcular

		Retorna um float do valor da derivada

		'''

		# valor de retorno
		derivada = float()

		# cálculo da derivada
		valor = self.calcular(x, y, z)
		valor_res = self.calcular(x + variacao, y, z)
		derivada = (valor_res - valor) / variacao

		return derivada


	def calcular_derivada_parcial_y(self, x, y, z, variacao=1e-6):
		'''
		Calcula numericamente o valor da derivada parcial da função em y
		
		Parâmetros:
		- x: valor da variável independente x
		- y: valor da variável independente y
		- z: valor da variável independente z
		- variacao: variação na variável em questão usada para calcular

		Retorna um float do valor da derivada

		'''

		# valor de retorno
		derivada = float()

		# cálculo da derivada
		valor = self.calcular(x, y, z)
		valor_res = self.calcular(x, y + variacao, z)
		derivada = (valor_res - valor) / variacao

		return derivada


	def calcular_derivada_parcial_z(self, x, y, z, variacao=1e-6):
		'''
		Calcula numericamente o valor da derivada parcial da função em z
		
		Parâmetros:
		- x: valor da variável independente x
		- y: valor da variável independente y
		- z: valor da variável independente z
		- variacao: variação na variável em questão usada para calcular

		Retorna um float do valor da derivada

		'''

		# valor de retorno
		derivada = float()

		# cálculo da derivada
		valor = self.calcular(x, y, z)
		valor_res = self.calcular(x, y, z + variacao)
		derivada = (valor_res - valor) / variacao

		return derivada






