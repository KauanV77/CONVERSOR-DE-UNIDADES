import customtkinter

# JANELa
janela = customtkinter.CTk()
janela.title("Conversor UNIFG")
janela.geometry("500x600")

# Cor do fundo
cor_fundo_atual = "#8EA6F3"
janela.configure(fg_color=cor_fundo_atual)

categoria_atual = "Comprimento"

# Faz a cor do fundo mudar devagar
def mudar_cor_suave(cor_destino, passo=0):
    global cor_fundo_atual

    # Cores usadas no programa
    cores_rgb = {
        "#8EA6F3": (224, 231, 255),
        "#91EAB0": (220, 252, 231),
        "#F0C48A": (255, 237, 213)
    }

    if passo <= 10:

        # Cor atual e cor que queremos chegar
        r1, g1, b1 = cores_rgb[cor_fundo_atual]
        r2, g2, b2 = cores_rgb[cor_destino]

        # Calcula as cores do meio da animação
        r = int(r1 + (r2 - r1) * (passo / 10))
        g = int(g1 + (g2 - g1) * (passo / 10))
        b = int(b1 + (b2 - b1) * (passo / 10))

        nova_cor = f"#{r:02x}{g:02x}{b:02x}"
        janela.configure(fg_color=nova_cor)

        # Continua a animação da cor do fundo
        janela.after(20, mudar_cor_suave, cor_destino, passo + 1)

    else:
        cor_fundo_atual = cor_destino


# Quando clicar em Comprimento
def clica_comprimento():
    global categoria_atual

    categoria_atual = "Comprimento"
    mudar_cor_suave("#8EA6F3")

    # Unidades 
    opcoes = ["Metro", "Centimetro", "Quilometro"]

    caixa_de.configure(values=opcoes)
    caixa_para.configure(values=opcoes)

    caixa_de.set("Metro")
    caixa_para.set("Centimetro")

    # Limpa os campos
    entrada_valor.delete(0, 'end')
    entrada_resultado.delete(0, 'end')


# Quando clicar em Peso
def clica_peso():
    global categoria_atual

    categoria_atual = "Peso"
    mudar_cor_suave("#91EAB0")

    opcoes = ["Grama", "Quilograma"]

    caixa_de.configure(values=opcoes)
    caixa_para.configure(values=opcoes)

    caixa_de.set("Quilograma")
    caixa_para.set("Grama")

    # Limpa os campos
    entrada_valor.delete(0, 'end')
    entrada_resultado.delete(0, 'end')


# Quando clicar em Temperatura
def clica_temperatura():
    global categoria_atual

    categoria_atual = "Temperatura"
    mudar_cor_suave("#F0C48A")

    opcoes = ["Celsius", "Fahrenheit"]

    caixa_de.configure(values=opcoes)
    caixa_para.configure(values=opcoes)

    caixa_de.set("Celsius")
    caixa_para.set("Fahrenheit")

    # Limpa os campos
    entrada_valor.delete(0, 'end')
    entrada_resultado.delete(0, 'end')


# Faz as conversões
def calcular_tudo():
    try:

        # Pega o valor digitado
        texto_digitado = entrada_valor.get()
        valor = float(texto_digitado)

        de = caixa_de.get()
        para = caixa_para.get()

        resultado = 0

        # Conversões de comprimento
        if categoria_atual == "Comprimento":

            if de == "Metro" and para == "Centimetro":
                resultado = valor * 100

            elif de == "Metro" and para == "Quilometro":
                resultado = valor / 1000

            elif de == "Centimetro" and para == "Metro":
                resultado = valor / 100

            elif de == "Centimetro" and para == "Quilometro":
                resultado = valor / 100000

            elif de == "Quilometro" and para == "Metro":
                resultado = valor * 1000

            elif de == "Quilometro" and para == "Centimetro":
                resultado = valor * 100000

            else:
                resultado = valor

        # Conversões de peso
        elif categoria_atual == "Peso":

            if de == "Quilograma" and para == "Grama":
                resultado = valor * 1000

            elif de == "Grama" and para == "Quilograma":
                resultado = valor / 1000

            else:
                resultado = valor

        # Conversões de temperatura
        elif categoria_atual == "Temperatura":

            if de == "Celsius" and para == "Fahrenheit":
                resultado = (valor * 1.8) + 32

            elif de == "Fahrenheit" and para == "Celsius":
                resultado = (valor - 32) / 1.8

            else:
                resultado = valor

        # Mostra o resultado
        entrada_resultado.delete(0, 'end')
        entrada_resultado.insert(0, str(resultado))

    except:

        # Se der erro mostra aviso
        entrada_resultado.delete(0, 'end')
        entrada_resultado.insert(0, "Erro!")


# titulo do conversor
titulo = customtkinter.CTkLabel(
    janela,
    text="Conversor de Unidades",
    font=("Arial", 30)
)
titulo.pack(pady=20)

# Botoes
frame_botoes = customtkinter.CTkFrame(
    janela,
    fg_color="transparent"
)
frame_botoes.pack(pady=10)

btn_comp = customtkinter.CTkButton(
    frame_botoes,
    text="Comprimento",
    command=clica_comprimento
)
btn_comp.pack(side="left", padx=5)

btn_peso = customtkinter.CTkButton(
    frame_botoes,
    text="Peso",
    command=clica_peso
)
btn_peso.pack(side="left", padx=5)

btn_temp = customtkinter.CTkButton(
    frame_botoes,
    text="Temperatura",
    command=clica_temperatura
)
btn_temp.pack(side="left", padx=5)

# Espaço visual
espaco = customtkinter.CTkLabel(janela, text="")
espaco.pack()

# --- NOVO FRAME ---
frame_opcoes = customtkinter.CTkFrame(janela, fg_color="#BBBBBB", corner_radius=12)
frame_opcoes.pack(pady=10, padx=20, fill="both", expand=True)

# Escolha da unidade quando inicia o programa
label_de = customtkinter.CTkLabel(frame_opcoes, text="Converter de:")
label_de.pack(pady=(10, 0))

caixa_de = customtkinter.CTkOptionMenu(
    frame_opcoes,
    values=["Metro", "Centimetro", "Quilometro"]
)
caixa_de.pack(pady=5)

# Campo para digitar o valor
entrada_valor = customtkinter.CTkEntry(
    frame_opcoes,
    placeholder_text="Digite o número aqui"
)
entrada_valor.pack(pady=10)

# Botão da conversao
btn_calcular = customtkinter.CTkButton(
    frame_opcoes,
    text="CALCULAR AGORA",
    command=calcular_tudo,
    fg_color="black"
)
btn_calcular.pack(pady=20)

# Escolha da unidade final
label_para = customtkinter.CTkLabel(frame_opcoes, text="Para:")
label_para.pack()

caixa_para = customtkinter.CTkOptionMenu(
    frame_opcoes,
    values=["Centimetro", "Metro", "Quilometro"]
)
caixa_para.pack(pady=5)

# Campo do Resultado
entrada_resultado = customtkinter.CTkEntry(
    frame_opcoes,
    placeholder_text="O resultado vai aparecer aqui"
)
entrada_resultado.pack(pady=(10, 20))

janela.mainloop()