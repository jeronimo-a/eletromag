'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classes de campos vetoriais

Jerônimo de Abreu Afrange

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


	def calcular_integral_linha(self, curva, t_inicial, t_final, resolucao=1e3, variacao=1e-3):
		'''
		Calcula a integral de linha do campo em uma curva.

		Parâmetros:
		- curva: instância de CurvaParametrizada2D
		- t_inicial: valor inicial de t
		- t_final: valor final de t
		- resolucao: número de subdivisões de integração
		- variacao: variação no parâmetro usada para calcular a derivada da curva 

		Retorna o valor da integral de linha (num)

		'''

		# força int em resolução
		resolucao = int(resolucao)

		# valor de retorno
		integral = float()

		# pré-cálculos
		delta_t = t_final - t_inicial
		dt = delta_t / resolucao

		# loop de cálculo
		for i in range(resolucao):

			# calcula o valor de t atual
			t = t_inicial + dt * i

			# calcula os vetores relativos à curva
			vetor_curva = curva.calcular(t)
			derivada_vetor_curva = curva.calcular_derivada(t, variacao)

			# calcula o vetor do campo no ponto atual da curva
			vetor_campo = self.calcular(vetor_curva[0], vetor_curva[1])
			
			# calcula o produto escalar do vetor_campo e derivada_vetor_curva
			# divide por dt e soma ao acumulador da integral
			valor = derivada_vetor_curva[0] * vetor_campo[0]
			valor += derivada_vetor_curva[1] * vetor_campo[1]
			integral += valor * dt

		return integral



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


	def calcular_integral_linha(self, curva, t_inicial, t_final, resolucao=1e3, variacao=1e-3):
		'''
		Calcula a integral de linha do campo em uma curva.

		Parâmetros:
		- curva: instância de CurvaParametrizada3D
		- t_inicial: valor inicial de t
		- t_final: valor final de t
		- resolucao: número de subdivisões de integração
		- variacao: variação no parâmetro usada para calcular a derivada da curva 

		Retorna o valor da integral de linha (num)

		'''

		# força int em resolução
		resolucao = int(resolucao)

		# valor de retorno
		integral = float()

		# pré-cálculos
		delta_t = t_final - t_inicial
		dt = delta_t / resolucao

		# loop de cálculo
		for i in range(resolucao):

			# calcula o valor de t atual
			t = t_inicial + dt * i

			# calcula os vetores relativos à curva
			vetor_curva = curva.calcular(t)
			derivada_vetor_curva = curva.calcular_derivada(t, variacao)

			# calcula o vetor do campo no ponto atual da curva
			vetor_campo = self.calcular(vetor_curva[0], vetor_curva[1], vetor_curva[2])
			
			# calcula o produto escalar do vetor_campo e derivada_vetor_curva
			# divide por dt e soma ao acumulador da integral
			valor = derivada_vetor_curva[0] * vetor_campo[0]
			valor += derivada_vetor_curva[1] * vetor_campo[1]
			valor += derivada_vetor_curva[2] * vetor_campo[2]
			integral += valor * dt

		return integral






