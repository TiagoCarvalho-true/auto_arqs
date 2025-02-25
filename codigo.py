import os
import mimetypes
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# Escopo de permissão (altere para drive se precisar de acesso completo)
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def autenticar():
    creds = None
    # Verifica se já existe um token de acesso válido
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Se não houver credenciais válidas, faz login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Salva as credenciais para a próxima vez
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def upload_para_drive(caminho_arquivo):
    creds = autenticar()
    
    try:
        service = build('drive', 'v3', credentials=creds)
        
        # Configuração do arquivo
        nome_arquivo = os.path.basename(caminho_arquivo)
        mime_type, _ = mimetypes.guess_type(caminho_arquivo)
        if mime_type is None:
            mime_type = 'application/octet-stream'
        
        # Cria metadados e mídia para upload
        file_metadata = {'name': nome_arquivo}
        media = MediaFileUpload(caminho_arquivo,
                                mimetype=mime_type,
                                resumable=True)
        
        # Executa o upload
        arquivo = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        print(f'Arquivo "{nome_arquivo}" enviado com sucesso! ID: {arquivo.get("id")}')
    
    except HttpError as error:
        print(f'Ocorreu um erro: {error}')

if __name__ == '__main__':
    # Configuração do arquivo a ser enviado
    caminho_arquivo = r'C:\caminho\para\seu\arquivo.extensao'  # Altere este caminho
    
    if os.path.exists(caminho_arquivo):
        upload_para_drive(caminho_arquivo)
    else:
        print('Arquivo não encontrado! Verifique o caminho especificado.')