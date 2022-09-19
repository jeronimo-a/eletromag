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


	def calcular_derivada(self, var_independente, variacao=1e-6):
		'''
		Calcula numericamente o valor da derivada da função
		
		Parâmetros:
		- var_independente: valor da variável independente
		- variacao: variação no parâmetro usada para calcular

		Retorna um float do valor da derivada

		'''

		# valor de retorno
		derivada = float()

		# cálculo da derivada
		valor = self.funcao(var_independente)
		valor_res = self.funcao_x(var_independente + variacao)
		derivada = (valor_res - valor) / variacao

		return derivada





