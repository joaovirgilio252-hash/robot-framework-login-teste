# robot-framework-login-teste
“Testes de login automatizados com Robot Framework”
# 🔐 Testes de Login com Robot Framework

Este projeto contém cenários automatizados de login utilizando **Robot Framework** e **SeleniumLibrary**.  
O objetivo é validar diferentes combinações de credenciais e mensagens de retorno do sistema.

---

## 📂 Estrutura do Projeto
- `login.robot` → contém os cenários de teste de login.
- `Estrutura.robot` → keywords e variáveis auxiliares.
- `BDD.robot` → exemplos de escrita de cenários em estilo BDD.
- `requirements.txt` → dependências do projeto.
- `.gitignore` → arquivos ignorados pelo Git.
- `README.md` → documentação do projeto.

---

## 🚀 Como executar os testes

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/joaovirgilio252-hash/robot-framework-login-teste.git
   cd robot-framework-login-teste
2. Instale as dependencias:
    pip install -r requirements.txt
3.Execute os testes:
   robot login.robot

   Cenários implementados- Cenário 1: Campos vazios → mensagem de erro “E-mail e senha são obrigatórios”
- Cenário 2: E-mail válido + senha inválida → mensagem de erro “E-mail ou senha inválidos!”
- Cenário 3: E-mail inválido + senha válida → mensagem de erro “E-mail ou senha inválidos!”
- Cenário 4: Ambos inválidos → mensagem de erro “E-mail ou senha inválidos!”
- Cenário 5: Ambos válidos → mensagem de boas-vindas “Bem vindo”

AutorProjeto desenvolvido por João Virgílio como prática de automação de testes.

