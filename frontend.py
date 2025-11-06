import tkinter as tk
from tkinter import font
from backend import CalculadoraCientifica 

class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica Python")
        master.resizable(False, False)

        # 1. Instância do Back-End
        self.calculadora = CalculadoraCientifica()
        
        # Variável para armazenar a expressão atual
        self.expressao_atual = ""
        
        # Variável de controle 
        self.ultimo_resultado = None

        # Configurações de estilo
        self.font_display = font.Font(family="Helvetica", size=20)
        self.font_botoes = font.Font(family="Helvetica", size=14, weight="bold")
        
        # 2. Criação do Display (Visor)
        self.display = tk.Entry(
            master, 
            width=20, 
            borderwidth=5, 
            relief=tk.FLAT, 
            justify='right', 
            font=self.font_display
        )
        # O display ocupa todas as 4 colunas
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        #  Definição e Layout dos Botões
        self.criar_botoes()
        
    def criar_botoes(self):
        # Definição dos botões: (texto, linha, coluna, cor_fundo)
        botoes = [
            ('C', 1, 0, '#E57373'), ('%', 1, 1, '#FFB74D'), ('√', 1, 2, '#FFB74D'), ('/', 1, 3, '#FFA000'),
            ('sen', 2, 0, '#ADD8E6'), ('cos', 2, 1, '#ADD8E6'), ('tan', 2, 2, '#ADD8E6'), ('x', 2, 3, '#FFA000'),
            ('7', 3, 0, '#FFFFFF'), ('8', 3, 1, '#FFFFFF'), ('9', 3, 2, '#FFFFFF'), ('-', 3, 3, '#FFA000'),
            ('4', 4, 0, '#FFFFFF'), ('5', 4, 1, '#FFFFFF'), ('6', 4, 2, '#FFFFFF'), ('+', 4, 3, '#FFA000'),
            ('1', 5, 0, '#FFFFFF'), ('2', 5, 1, '#FFFFFF'), ('3', 5, 2, '#FFFFFF'), ('=', 5, 3, '#4CAF50'),
            ('0', 6, 0, '#FFFFFF'), ('.', 6, 1, '#FFFFFF'), ('+/-', 6, 2, '#9E9E9E'), ('<-', 6, 3, '#9E9E9E') 
        ]
        
        # Mapeamento de texto para as funções de clique
        for (texto, linha, coluna, cor) in botoes:
            if texto == 'C':
                comando = self.limpar_display
            elif texto == '=':
                comando = self.calcular_expressao
            elif texto == '√':
                comando = self.calcular_raiz
            elif texto in ('sen', 'cos', 'tan'):
                comando = lambda t=texto: self.calcular_trigonometria(t)
            elif texto == '%':
                comando = self.calcular_porcentagem
            elif texto == '<-':
                comando = self.apagar_ultimo
            elif texto == '+/-':
                comando = self.inverter_sinal
            else:
                comando = lambda t=texto: self.clicar_botao(t)

            # --- AQUI É O AJUSTE PARA O TAMANHO IGUAL ---
            b = tk.Button(self.master, text=texto, padx=10, pady=10, bg=cor, font=self.font_botoes, command=comando)
            
            b.grid(row=linha, column=coluna, sticky="nsew", padx=3, pady=3)
                
            self.master.grid_columnconfigure(coluna, weight=1)
            self.master.grid_rowconfigure(linha, weight=1)

    # (Adicionei a função inverter_sinal para o novo botão)

    def limpar_display(self):
        """Limpa a expressão e o display."""
        self.expressao_atual = ""
        self.ultimo_resultado = None
        self.display.delete(0, tk.END)

    def apagar_ultimo(self):
        """Apaga o último caractere digitado."""
        self.expressao_atual = self.expressao_atual[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expressao_atual)

    def clicar_botao(self, valor):
        """Adiciona o número ou operador à expressão atual."""
        self.expressao_atual += str(valor)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expressao_atual)

    def calcular_expressao(self):
        """Chama a função de cálculo simples do Back-End."""
        resultado = self.calculadora.calcular_simples(self.expressao_atual)
        
        self.expressao_atual = str(resultado) if not isinstance(resultado, str) else ""
        self.display.delete(0, tk.END)
        self.display.insert(0, str(resultado))
        self.ultimo_resultado = resultado

    def calcular_raiz(self):
        """Chama a função de raiz quadrada do Back-End."""
        valor = self.display.get()
        if not valor: return
        resultado = self.calculadora.raiz_quadrada(valor)
        self.expressao_atual = str(resultado) if not isinstance(resultado, str) else ""
        self.display.delete(0, tk.END)
        self.display.insert(0, str(resultado))
        self.ultimo_resultado = resultado

    def calcular_trigonometria(self, funcao):
        """Chama a função trigonométrica (seno, cosseno, tangente) do Back-End."""
        valor = self.display.get()
        if not valor: return
        resultado = self.calculadora.calcular_trigonometrica(funcao, valor)
        self.expressao_atual = str(resultado) if not isinstance(resultado, str) else ""
        self.display.delete(0, tk.END)
        self.display.insert(0, str(resultado))
        self.ultimo_resultado = resultado
        
    def calcular_porcentagem(self):
        """Calcula o valor percentual de um número digitado."""
        expressao = self.display.get()
        try:
            num = float(expressao)
            resultado = num / 100
            self.expressao_atual = str(resultado)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expressao_atual)
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Erro")
            
    def inverter_sinal(self):
        """Inverte o sinal do número atual no display."""
        try:
            num = float(self.display.get())
            resultado = num * -1
            self.expressao_atual = str(resultado)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expressao_atual)
        except ValueError:
            pass

# --- Execução da Aplicação ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()