from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os




def centralizar_texto(desenhar, texto, fonte, largura_total):
    largura_texto = desenhar.textsize(texto, font=fonte)[0]
    posicao_x = (largura_total - largura_texto) // 2
    return posicao_x

def gerar_cracha(nome, sobrenome ,funcao, caminho_da_foto, caminho_pasta_para_salvar):
    resolucao = 300

    #tamanho do cracha
    largura, altura= int(50 * resolucao // 25.4), int(70 * resolucao // 25.4)  # mm para pixels

    texto1="Convenção Baptista de Angola"
    texto2="Departamento de envagelismo e Missões"
    texto3 = "PARTICIPANTE"
    texto4 = "CONFERÊNCIA INTERNACIONAL DE MISSÕES"
    texto5 = "LUANDA, 26 DE OUTUBRO DE 2024"

    #criar uma imagem com fundo branco
    imagem = Image.new('RGB', (largura,altura), 'white')
    desenhar=ImageDraw.Draw(imagem)

    # Fonte com melhor qualidade
    fonte_nome = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
    fonte_funcao = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
    fonte_sobrenome = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
    fonte_texto = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf", 15)

    #inserir nome , funcao no cracha e os textos
    posicao_nome = centralizar_texto(desenhar, nome, fonte_nome, largura)
    desenhar.text((posicao_nome,300), nome, font=fonte_nome, fill="black")

    posicao_sobrenome = centralizar_texto(desenhar, sobrenome, fonte_sobrenome, largura)
    desenhar.text((posicao_sobrenome, 380), sobrenome, font=fonte_sobrenome, fill="black")

    posicao_funcao = centralizar_texto(desenhar, funcao, fonte_funcao, largura)
    desenhar.text((posicao_funcao, 450), funcao, font=fonte_funcao, fill="black")

    posicao_texto1 = centralizar_texto(desenhar, texto1, fonte_texto, largura)
    desenhar.text((posicao_texto1, 190), texto1, font=fonte_texto, fill="black")

    posicao_texto2 = centralizar_texto(desenhar, texto2, fonte_texto, largura)
    desenhar.text((posicao_texto2, 210), texto2, font=fonte_texto, fill="black")

    posicao_texto3 = centralizar_texto(desenhar, texto3, fonte_texto, largura)
    desenhar.text((posicao_texto3, 550), texto3, font=fonte_texto, fill="black")

    # Desenhar um retângulo verde ao redor do texto3
    largura_texto3, altura_texto3 = desenhar.textsize(texto3, font=fonte_texto)
    posicao_texto3 = centralizar_texto(desenhar, texto3, fonte_texto, largura)

    padding = 10  # margem extra ao redor do texto
    desenhar.rectangle(
        [posicao_texto3 - padding, 540, posicao_texto3 + largura_texto3 + padding, 550 + altura_texto3 + padding],
        fill="green"
    )

    # Desenhar o texto3 dentro do retângulo verde
    desenhar.text((posicao_texto3, 550), texto3, font=fonte_texto, fill="white")

    posicao_texto4 = centralizar_texto(desenhar, texto4, fonte_texto, largura)
    desenhar.text((posicao_texto2, 230), texto4, font=fonte_texto, fill="black")

    posicao_texto5 = centralizar_texto(desenhar, texto5, fonte_texto, largura)
    desenhar.text((posicao_texto5, 250), texto5, font=fonte_texto, fill="black")

    foto = Image.open(caminho_da_foto)
    foto = foto.resize((200,140), Image.LANCZOS)
    imagem.paste(foto, (200, 50))

    caminho_completo = os.path.join(caminho_pasta_para_salvar, f"{nome} {sobrenome}.png")

    imagem.save(caminho_completo, "PNG", optimize=True, quality=95)
    print(f"Cracha salvo em {caminho_pasta_para_salvar}")


# Função para gerar crachás em massa a partir de um arquivo CSV
def gerar_crachas_em_massa(caminho_do_documento, caminho_da_foto, caminho_pasta_para_salvar):
    # Ler o arquivo CSV
    #documento = pd.read_csv(caminho_do_documento)
    documento = pd.read_excel(caminho_do_documento)

    print("Colunas disponíveis:", documento.columns.tolist())
    # Para cada linha no CSV, gerar um crachá
    for i, j in documento.iterrows():
        nome = j['nome']
        funcao = j['funcao']
        sobrenome=j['sobrenome']

        # Gerar o crachá
        gerar_cracha(nome, sobrenome,funcao, caminho_da_foto ,caminho_pasta_para_salvar)


nome="Júlio"
sobrenome="Chilela"
funcao="Coordenador da área de IT"
caminho_da_foto="CBA.jpeg"
caminho_do_documento="numeros_de_telefone_teste.ods"
caminho_da_pasta="/home/garcia_simao/Documentos/Projecto actividade da CBA/crachas"

#gerar_cracha(nome, sobrenome, funcao, caminho_da_foto, caminho_da_pasta)
gerar_crachas_em_massa(caminho_do_documento, caminho_da_foto,caminho_da_pasta)