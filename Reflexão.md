# Reflexão — EngTutor: Agente Tutor de Inglês

## 1. Decisões de design do prompt

Escolhi tutor de inglês porque é algo que faz sentido no meu dia a dia — é uma dificuldade real, minha e de muita gente ao redor. Isso ajudou bastante na hora de testar, porque eu mesmo conseguia julgar se a resposta estava boa ou não, sem precisar de nenhum critério técnico complicado.

A parte mais difícil foi entender o código Python. Nunca tinha mexido com SDK de IA antes, e no começo não fazia ideia de como o histórico da conversa era mantido. Fui lendo aos poucos e descobri que o próprio objeto `chat` já cuida disso — cada vez que você chama `chat.send_message()`, ele lembra tudo que foi dito antes automaticamente. Parece simples depois que entende, mas levou um tempo até clicar.

No prompt, o que mais me deu trabalho foi escrever a parte de recusa — quando o agente precisa dizer que não vai responder algo fora do escopo. As primeiras versões soavam muito robotizadas, tipo um atendente de banco. Fui ajustando até chegar num tom mais natural, onde a recusa vem acompanhada de um redirecionamento ("mas sobre inglês posso te ajudar muito"). Também coloquei dois exemplos diferentes no prompt — uma tradução simples e uma dúvida de gramática — pra mostrar ao modelo como eu queria que ele respondesse em cada tipo de situação.

---

## 2. Uma coisa que funcionou e uma que não funcionou

### ✅ O que funcionou — Recusa fora do escopo

Após corrigir o system prompt, testei perguntas fora do escopo e o agente respondeu corretamente:

> Usuário: `qual a capital da França?`
> EngTutor: "Sou especialista em ensino de inglês. Sobre geografia não sou a ferramenta certa — mas posso te ensinar a falar sobre viagens em inglês! Quer tentar?"

A instrução explícita de recusa com template de resposta foi determinante para esse resultado.

### ❌ O que não funcionou — Configuração da API

O maior problema técnico foi configurar a API do Google Gemini. As variáveis de ambiente funcionam diferente no Windows — o comando `export` é do Linux/Mac e não existe no PowerShell. Tentei usar `export GEMINI_API_KEY=...` no terminal e recebi o erro:

> *"O termo 'export' não é reconhecido como nome de cmdlet"*

A solução foi usar um arquivo `.env` com a biblioteca `python-dotenv`, chamando `load_dotenv()` no início do código para carregar a chave automaticamente. Além disso, o `system_prompt.txt` inicialmente continha o prompt errado, o que fez o agente ignorar completamente o escopo de inglês nas primeiras interações.

---

## 3. O que eu faria com mais tempo

A próxima melhoria seria um **modo de prática estruturada**: o agente detectaria quando o aluno quer praticar (ex: "quero treinar verbos irregulares") e iniciaria uma sequência de exercícios com feedback progressivo — errou, explica e tenta de novo; acertou, aumenta a dificuldade.

Isso transformaria o agente de um "tirador de dúvidas" em um professor de fato. Implementaria com uma variável de estado simples (`modo_pratica = True/False`) que mudaria o comportamento do agente dentro do loop principal, sem precisar de nenhum framework externo.