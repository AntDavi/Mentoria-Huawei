import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SAMPLE_SPREADSHEET_ID = "175YaMK3bZ3y_V3Bnuo24v6KapYOrTB7pimx7ou16h3c"
SAMPLE_RANGE_NAME = "Página1!A2:B"

def main():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credencialHUAWEI.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Ler informações da tabela
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        valores = result.get('values', [])  # Obtém os valores da resposta ou uma lista vazia se não houver valores
        print(valores)

        # Calcula o total de itens na coluna B, ignorando a linha de títulos e a célula "Total de itens" na coluna A
        total_itens = sum(int(item[1]) for item in valores if len(item) >= 2 and item[0] != 'Total de itens')

        # Adicionar ['Total de itens', totalDeItemsTabela] na primeira linha livre da coluna A
        valores_adicionar = [
            ['Total de itens', total_itens],
        ]

        result = (
            sheet.values()
            .append(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range='Página1!A:B',
                valueInputOption="USER_ENTERED",
                body={'values': valores_adicionar},
                insertDataOption="INSERT_ROWS",
            )
            .execute()
        )

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
