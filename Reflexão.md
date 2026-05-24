# Reflexão — EngTutor: Agente Tutor de Inglês

## 1. Decisões de design do prompt

Escolhi o domínio de tutor de inglês porque é uma necessidade real para estudantes brasileiros e o escopo é bem delimitado — o agente tem um papel claro e concreto. Qualquer pessoa consegue testar se a resposta está certa ou não, o que facilita a avaliação iterativa do prompt.

A parte mais difícil do projeto foi entender o código Python, especialmente como o SDK do Google Gemini funciona e como o histórico multi-turn é mantido automaticamente pelo objeto `chat`. No início não estava claro que bastava usar `client.chats.create()` e chamar `chat.send_message()` repetidamente — o próprio SDK cuida do contexto entre os turnos.

O elemento mais trabalhoso do system prompt foi definir **o que o agente não faz** de forma que a recusa soasse natural e não robótica. Testei algumas versões e percebi que incluir um redirecionamento ("mas sobre inglês posso te ajudar muito") deixava a negativa mais amigável do que uma recusa seca. Também adicionei dois exemplos few-shot com situações diferentes — uma tradução simples e uma dúvida conceitual — para mostrar ao modelo o formato de resposta esperado em contextos distintos.

---

## 2. Uma coisa que funcionou e uma que não funcionou

### ✅ O que funcionou — Recusa fora do escopo

**Conversa:**
> Usuário: `loops`
> EngTutor: *explicou loops em Python detalhadamente*

Depois de corrigir o system prompt, testei a mesma pergunta e o agente respondeu corretamente:

> Usuário: `loops`
> EngTutor: "Sou especialista em ensino de inglês. Sobre programação não sou a ferramenta certa — mas posso te ensinar a falar sobre tecnologia em inglês! Quer tentar?"

A instrução explícita de recusa com template de resposta foi determinante para esse resultado.

### ❌ O que não funcionou — Configuração da API

O maior problema técnico foi configurar a API do Google Gemini. As variáveis de ambiente funcionam diferente no Windows — o comando `export` é do Linux/Mac e não existe no PowerShell. Tentei usar `export GEMINI_API_KEY=...` no terminal e recebi o erro:

> *"O termo 'export' não é reconhecido como nome de cmdlet"*

A solução foi usar um arquivo `.env` com a biblioteca `python-dotenv`, chamando `load_dotenv()` no início do código para carregar a chave automaticamente. Além disso, o `system_prompt.txt` inicialmente continha o prompt errado (de tutor de Python), o que fez o agente ignorar completamente o escopo de inglês nas primeiras interações.

---

## 3. O que eu faria com mais tempo

A próxima melhoria seria um **modo de prática estruturada**: o agente detectaria quando o aluno quer praticar (ex: "quero treinar verbos irregulares") e iniciaria uma sequência de exercícios com feedback progressivo — errou, explica e tenta de novo; acertou, aumenta a dificuldade.

Isso transformaria o agente de um "tirador de dúvidas" em um professor de fato. Implementaria com uma variável de estado simples (`modo_pratica = True/False`) que mudaria o comportamento do agente dentro do loop principal, sem precisar de nenhum framework externo.