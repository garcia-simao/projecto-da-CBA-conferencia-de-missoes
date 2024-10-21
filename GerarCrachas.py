from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os




def centralizar_texto(desenhar, texto, fonte, largura_total):
    largura_texto = desenhar.textsize(texto, font=fonte)[0]
    posicao_x = (largura_total - largura_texto) // 2
    return posicao_x

def gerar_cracha(nome, sobrenome ,funcao, caminho_da_foto, caminho_pasta_para_salvar):

    #tamanho do cracha
    largura, altura= 400, 600

    texto1="Convenção Baptista de Angola"
    texto2="Departamento de envagelismo e Missões"

    #criar uma imagem com fundo branco
    imagem = Image.new('RGB', (largura,altura), 'white')
    desenhar=ImageDraw.Draw(imagem)

    # Fonte com melhor qualidade
    fonte_nome = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 45)
    fonte_funcao = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
    fonte_sobrenome = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 45)
    fonte_texto = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)

    # Etiquetas antes do nome e cargo
    #desenhar.text((50, 400), "Nome:", font=fonte_nome, fill="black")
    #desenhar.text((50, 450), "Função:", font=fonte_nome, fill="black")

    #inserir nome e funcao no cracha
    posicao_nome = centralizar_texto(desenhar, nome, fonte_nome, largura)
    desenhar.text((posicao_nome,300), nome, font=fonte_nome, fill="black")

    posicao_sobrenome = centralizar_texto(desenhar, sobrenome, fonte_sobrenome, largura)
    desenhar.text((posicao_sobrenome, 380), sobrenome, font=fonte_sobrenome, fill="black")

    posicao_funcao = centralizar_texto(desenhar, funcao, fonte_funcao, largura)
    desenhar.text((posicao_funcao, 550), funcao, font=fonte_funcao, fill="black")

    posicao_texto1 = centralizar_texto(desenhar, texto1, fonte_texto, largura)
    desenhar.text((posicao_texto1, 150), texto1, font=fonte_texto, fill="black")

    posicao_texto2 = centralizar_texto(desenhar, texto2, fonte_texto, largura)
    desenhar.text((posicao_texto2, 170), texto2, font=fonte_texto, fill="black")

    foto = Image.open(caminho_da_foto)
    foto = foto.resize((310,100))
    imagem.paste(foto, (50, 50))

    caminho_completo = os.path.join(caminho_pasta_para_salvar, f"{nome} {sobrenome}.pdf")

    imagem.save(caminho_completo)
    print(f"Cracha salvo em {caminho_pasta_para_salvar}")


# Função para gerar crachás em massa a partir de um arquivo CSV
def gerar_crachas_em_massa(caminho_do_documento, caminho_da_foto, caminho_pasta_para_salvar):
    # Ler o arquivo CSV
    #documento = pd.read_csv(csv_path)
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