import math

class CalculadoraCientifica:
    # Classe responsável por todas as operações matemáticas (Back-End).
    
    def calcular_simples(self, expressao):
        try:
            # Substitui 'x' por '*' para multiplicação 
            expressao = expressao.replace('x', '*')
            
            # Trata porcentagem: 50% de 200 => (200 / 100) * 50
            if '%' in expressao:
                pass 

            # Usa a função eval() para processar a string da expressão
            resultado = eval(expressao)
            return resultado

        except ZeroDivisionError:
            return "Erro: Divisão por zero"
        except Exception:
            return "Erro: Expressão Inválida"

    def raiz_quadrada(self, numero):
        try:
            numero = float(numero)
            if numero < 0:
                return "Erro: Raiz de número negativo"
            return math.sqrt(numero)
        except ValueError:
            return "Erro: Entrada inválida"

    def calcular_trigonometrica(self, funcao, numero_graus):
        #Calcula seno, cosseno ou tangente.
        #Recebe o ângulo em graus e converte para radianos.

        try:
            numero = float(numero_graus)
            # Converte graus para radianos, pois as funções math.sin/cos/tan usam radianos
            radianos = math.radians(numero)
            
            if funcao == 'sen':
                return math.sin(radianos)
            elif funcao == 'cos':
                return math.cos(radianos)
            elif funcao == 'tan':
                # Garante que não haja divisão por zero (tan(90°), tan(270°), etc.)
                if abs(math.cos(radianos)) < 1e-9: # Verifica se o cosseno é muito próximo de zero
                    return "Erro: Tangente indefinida"
                return math.tan(radianos)
            else:
                return "Erro"

        except ValueError:
            return "Erro: Entrada inválida"
            
    def porcentagem_de(self, valor, percentual):
        #Calcula a porcentagem de um valor. Ex: 50% de 200.
        try:
            v = float(valor)
            p = float(percentual)
            return (v * p) / 100
        except ValueError:
            return "Erro: Entrada inválida"
