# Assistente de Voz via API - OPENAI

Grava áudio, transcreve utilizando o Whisper, transfere o texto para o GPT-4 e converte a resposta em áudio.

## Setup

1. Criar arquivo `.env` com a variável:

```bash
OPENAI_API_KEY=your_api_key_here
```
2. Instalar dependências:

```bash
pip install -r requirements.txt
```
3. Rodar:

```bash
python assistente.py
```
