# Uploader de Arquivos para Google Drive

Este projeto consiste em um script Python que automatiza o upload de arquivos para o Google Drive através da API do Google.

## 📋 Funcionalidades
- Autenticação automática com o Google Drive
- Upload de arquivos de qualquer tipo
- Detecção automática do tipo MIME do arquivo
- Gerenciamento de tokens de acesso
- Suporte a renovação automática de credenciais

## 🔧 Requisitos
- `google-api-python-client`
- `google-auth-httplib2`
- `google-auth-oauthlib`

## ⚙️ Como usar
### Configure suas credenciais:
1. Obtenha o arquivo `credentials.json` do Google Cloud Console
2. Coloque o arquivo na mesma pasta do script
3. Modifique o caminho do arquivo:
   ```python
   caminho_arquivo = r'C:\caminho\para\seu\arquivo.extensao'  # Altere este caminho



O script gerencia automaticamente:
- Verificação de credenciais existentes
- Renovação de tokens expirados
- Processo de autorização inicial
- Armazenamento seguro do token de acesso

## 📝 Observações
- O escopo atual está configurado para `drive.file`, permitindo acesso apenas aos arquivos criados pelo aplicativo
- O token de acesso é salvo localmente em `token.json`
- Suporta upload de qualquer tipo de arquivo com detecção automática do formato

