import pandas as pd #biblioteca que permite ler arquivos excel xlsx, ods
import requests


# URL da API
url = "https://telcosms.co.ao/send_message"

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json"
}

#lendo o arquivo excel
documento_excel="numeros_de_telefone_teste.ods"
ler_arquivo= pd.read_excel(documento_excel)
#ler_arquivo= pd.read_csv(documento_excel)

#a primerira coluna do excel deve ter uma descrição e a seguir numeros
#percorrer o documento excel e enviar mensagem a cada numero.
for i , j in ler_arquivo.iterrows():
    telefone = j['numero_telefone']

    # Verificar se a célula está vazia ou se o número contém caracteres não numéricos
    if pd.isna(telefone) or not str(telefone).isdigit() or len(
            str(telefone)) < 9:
        print(f"Número inválido ou célula vazia: {telefone}, ignorando...")
        continue  # Pula para a próxima iteração do loop

    data = {
        "message": {
            "api_key_app": "prdc4b5a87b97d15edf8aa0cb5929",
            "phone_number": str(telefone),
            "message_body": "Mensagem de teste CBA"
        }
    }

    # Fazendo a requisição POST
    response = requests.post(url, json=data, headers=headers)

    # Exibindo o status da resposta e o corpo da resposta
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
