'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classes de campos vetoriais

'''

class CampoVetorial2D:
	''' Classe que define um campo vetorial FIXO de duas dimensões '''
	

	def __init__(self, funcao_x, funcao_y):
		'''
		Inicializa um novo campo vetorial 2D.

		Parâmetros:
		- funcao_x: [função (num, num) -> num] do eixo x
		- funcao_y: [função (num, num) -> num] do eixo y

		'''

		# amarra os argumentos à insrância da classe
		self.funcao_x = funcao_x
		self.funcao_y = funcao_y


	def calcular(self, x, y):
		'''
		Calcula o vetor do campo vetorial em determinado ponto.

		Parâmetros:
		- x: valor x do ponto em questão
		- y: valor y do ponto em questão

		Retorna um vetor (tupla) de duas dimensões (x, y)

		'''

		# valor de retorno
		vetor = tuple()

		# calcula os valores
		valor_x = self.funcao_x(x, y)
		valor_y = self.funcao_y(x, y)
		vetor = (valor_x, valor_y)

		return vetor


	def calcular_integral_linha(self, curva, resolucao=1e-3):
		'''
		Calcula a integral de linha do campo em uma curva.

		Parâmetros:
		- curva: [função (num) -> (num, num)] curva parametrizada 2D
		- resolucao: variação no parâmetro da curva usado para calcular

		Retorna o valor da integral de linha (num)

		'''

		pass
		



class CampoVetorial3D:
	''' Classe que define um campo vetorial FIXO de três dimensões '''
	

	def __init__(self, funcao_x, funcao_y, funcao_z):
		'''
		Inicializa um novo campo vetorial 3D.

		Parâmetros:
		- funcao_x: [função (num, num, num) -> num] do eixo x
		- funcao_y: [função (num, num, num) -> num] do eixo y
		- funcao_z: [função (num, num, num) -> num] do eixo z

		'''

		# amarra os argumentos à insrância da classe
		self.funcao_x = funcao_x
		self.funcao_y = funcao_y
		self.funcao_z = funcao_z


	def calcular(self, x, y, z):
		'''
		Calcula o vetor do campo vetorial em determinado ponto.

		Parâmetros:
		- x: valor x do ponto em questão
		- y: valor y do ponto em questão
		- z: valor z do ponto em questão

		Retorna um vetor (tupla) de três dimensões (x, y, z)

		'''

		# valor de retorno
		vetor = tuple()

		# calcula os valores
		valor_x = self.funcao_x(x, y, z)
		valor_y = self.funcao_y(x, y, z)
		valor_z = self.funcao_z(x, y, z)
		vetor = (valor_x, valor_y, valor_z)

		return vetor


	def calcular_integral_linha(self, curva, resolucao=1e-3):
		'''
		Calcula a integral de linha do campo em uma curva.

		Parâmetros:
		- curva: [função (num) -> (num, num, num)] curva parametrizada 3D
		- resolucao: variação no parâmetro da curva usado para calcular

		Retorna o valor da integral de linha (num)

		'''

		pass






