# EngTutor — Agente Tutor de Inglês 🇬🇧

Agente conversacional multi-turn que ensina inglês para falantes de português brasileiro. Desenvolvido com Python e Google Gemini como atividade de ingresso no Grupo de Estudos de IA.

## Como rodar

### 1. Clone ou baixe o projeto
Coloque todos os arquivos numa mesma pasta.

### 2. Instale as dependências
```powershell
pip install google-genai python-dotenv
```

### 4. Configure sua chave da API
Crie um arquivo `.env` na pasta do projeto com o seguinte conteúdo:
```
GEMINI_API_KEY=sua-chave-aqui
```
> Obtenha sua chave gratuita em: https://aistudio.google.com/app/apikey

### 5. Execute o agente
```powershell
python agent.py
```

## Estrutura do projeto

```
Projeto_IA/
├── agent.py            # Código do agente (multi-turn com Gemini)
├── system_prompt.txt   # Persona, escopo e exemplos few-shot
├── reflexao.md         # Reflexão escrita sobre as decisões de design
├── README.md           # Este arquivo
└── .env                # Chave da API (NÃO subir para o GitHub)
```

## Segurança

Nunca suba o arquivo `.env` para o GitHub. Adicione ao `.gitignore`:
```
.env
```

## Exemplo de uso

```
🇬🇧 EngTutor iniciado! Let's practice! (Digite 'sair' para encerrar)

Você: como fala "eu estou com fome" em inglês?
EngTutor: Boa pergunta! É "I'm hungry" 🍔 — literalmente "Eu estou faminto"...

Você: qual a diferença entre since e for?
EngTutor: Ótima dúvida! As duas palavras falam sobre tempo, mas de formas diferentes...
```