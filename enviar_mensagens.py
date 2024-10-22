import pandas as pd #biblioteca que permite ler arquivos excel xlsx, ods
import requests


# URL da API
url = "https://telcosms.co.ao/send_message"

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json"
}

#lendo o arquivo excel
documento_excel="cimi_final.csv"
#ler_arquivo= pd.read_excel(documento_excel)
ler_arquivo= pd.read_csv(documento_excel)
numeros_processados = set()
#a primerira coluna do excel deve ter uma descrição e a seguir numeros
#percorrer o documento excel e enviar mensagem a cada numero.
for i , j in ler_arquivo.iterrows():
    telefone = j['Telefone']


    # Verificar se a célula está vazia ou se o número contém caracteres não numéricos
    if pd.isna(telefone) or not str(telefone).isdigit() or len(
            str(telefone)) < 9:
        print(f"Número inválido ou célula vazia: {telefone}, ignorando...")
        continue  # Pula para a próxima iteração do loop

    #verificar numeros duplicados
    if telefone in numeros_processados:
        print(f"Número duplicado encontrado: {telefone}, ignorando...")
        continue  # Pula para a próxima iteração do loop

    numeros_processados.add(telefone)

    mensagem =( "Amado(a), confirmamos a sua inscricao na Conferencia Internacional de Missoes, dia 26.2"
                "As contrib. de 1.000kzs podem ser enviadas para o IBAN A006 0040 0000 4387 5824 1066 2"
                "CBA e o comprovativo para WhatsApp 923386289")

    data = {
        "message": {
            "api_key_app": "prdc4b5a87b97d15edf8aa0cb5929",
            "phone_number": str(telefone),
            "message_body": mensagem
        }
    }

    # Fazendo a requisição POST
    response = requests.post(url, json=data, headers=headers)

    # Exibindo o status da resposta e o corpo da resposta
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
