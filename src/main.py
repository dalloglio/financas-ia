import os
import json
import base64
import google.generativeai as genai
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
SERVICE_ACCOUNT_INFO_BASE64 = os.environ.get("SERVICE_ACCOUNT_INFO_BASE64")
SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

try:
    json_string = base64.b64decode(SERVICE_ACCOUNT_INFO_BASE64).decode('utf-8')
    creds_info = json.loads(json_string)
    creds = service_account.Credentials.from_service_account_info(creds_info, scopes=SCOPES)
    sheets_service = build('sheets', 'v4', credentials=creds)
except Exception as e:
    print(f"Erro ao carregar credenciais: {e}")
    exit()

def ler_dados_da_planilha(spreadsheet_id, range_name):
    """
    Lê os dados da planilha do Google Sheets e retorna um DataFrame (ou uma lista de listas).
    """
    try:
        sheet = sheets_service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])

        if not values:
            print('Nenhum dado encontrado.')
            return None
        else:
            headers = values[0]
            data = values[1:]
            df = pd.DataFrame(data, columns=headers)
            return df
    except Exception as e:
        print(f"Erro ao ler a planilha: {e}")
        return None



def analisar_gastos_com_gemini(dados):
    """
    Envia os dados para a API Gemini e retorna os insights.
    """

    prompt = f"""
    Analise os seguintes dados de gastos:

    {dados}

    Com base nesses dados, forneça insights financeiros para um jovem adulto, incluindo:
    - Principais categorias de gasto.
    - Categorias com gastos elevados.
    - Padrões de gasto.
    - Dicas de economia.
    - Resumo dos gastos.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao obter insights da Gemini: {e}"


def main():
    """
    Função principal que coordena o fluxo do programa.
    """
    RANGE_NAME = 'A1:D'

    dados = ler_dados_da_planilha(SPREADSHEET_ID, RANGE_NAME)

    if dados is not None:
        insights = analisar_gastos_com_gemini(dados)
        print("Insights Financeiros:\n\n", insights)


if __name__ == "__main__":
    main()