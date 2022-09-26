'''
Estudos de Eletromagnetismo e Ondulatória
Insper, Engenharia da Computação 2022.2

Classe que representa monômios matemáticos

Jerônimo de Abreu Afrange

https://www.cuemath.com/algebra/polynomials/

'''

from monomio import Monomio


class Polinomio:
	''' Representa um polinômio matemático '''


	def __init__(self, monomios, constante=0):
		'''
		Cria uma nova instância de Polinomio.

		Parâmetros:
		- monomios: lista de instâncias de Monomio;
		- constante: valor numérico, constance do polinômio

		'''

		#--	--- VERIFICA A VALIDADE DOS ARGUMENTOS	---	---	---	---	---	---	---	---	---	---	---	---	---	---

		if not isinstance(monomios, list):
			raise TypeError('O argumento "monomios" tem que ser uma lista.')

		if not (isinstance(constante, int) or isinstance(coeficiente, float)):
			raise TypeError('O argumento "constante" tem que ser um valor numérico.')

		for monomio in monomios:
			if not isinstance(monomio, Monomio):
				raise TypeError('Os itens do argumento "monomios" devem ser instâncias de Monomio.')

		#--	---	---	---	---	---	---	--- ---	---	---	---	---	---	---	---	---	---	---	---	---	---	---	---	---

		# valores a serem extraídos da lista de monômios
		monomios_por_identidade = dict()
		monomios_combinados = list()
		numero_variaveis = 0
		variaveis = set()
		grau = 0

		# para cada monômio na lista
		for monomio in monomios:

			# verifica se há monômios de mesma identtidade para combiná-los depois
			identidade = monomio.identidade
			try: monomios_por_identidade[identidade].append(monomio)
			except KeyError: monomios_por_identidade[identidade] = [monomio]

			# adiciona às variáveis do monômio ao set de contagem e verifica o grau
			for variavel in monomio.variaveis: variaveis.add(variavel)
			if monomio.grau > grau: grau = monomio.grau

		# combina os monômios de identidades iguais
		for identidade in monomios_por_identidade.keys():
			monomios_dessa_identidade = monomios_por_identidade[identidade]
			monomio_base = Monomio(monomios_dessa_identidade[0].expoentes, 0)
			for monomio in monomios_dessa_identidade:
				monomio_base = monomio_base.combinar(monomio)
			monomios_combinados.append(monomio_base)

		# extrai demais informações e formata
		numero_variaveis = len(variaveis)
		variaveis = list(variaveis)
		variaveis.sort()

		# propriedades
		self.grau = grau
		self.monomios = monomios_combinados
		self.variaveis = variaveis
		self.numero_monomios = len(monomios_combinados)
		self.numero_variaveis = numero_variaveis












