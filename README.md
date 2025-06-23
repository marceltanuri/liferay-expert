# Conversor de Workspace para GPT Customizado

Este projeto converte uma workspace local de conhecimento técnico em arquivos prontos para serem usados na criação de um **ChatGPT customizado**:

- `instructions.txt` com até 8.000 caracteres.
- Até 20 arquivos `uploadX.txt` com conteúdos complementares (100.000 caracteres cada).

Agora essa funcionalidade está desacoplada e reutilizável por meio da biblioteca **[chatgpt-builder](https://github.com/seunome/chatgpt-builder)**.

---

## 📦 Como instalar a biblioteca

```bash
pip install git+https://github.com/seunome/chatgpt-builder.git
# ou, se estiver local:
pip install -e ./chatgpt-builder
```

---

## ▶️ Como usar via terminal

```bash
cd ./meu_conhecimento

chatgpt-builder --origem . --destino ../saida

```

---

## 📁 Estrutura esperada da workspace

```
meu_conhecimento/
├── instructions/        # Conteúdo principal → instructions.txt
│   ├── resumo.md
│   └── boas_praticas.txt
└── additional_info/     # Conteúdo complementar → uploadX.txt
    ├── casos_de_uso/
    │   └── exemplo1.md
    └── docs.json
```

Arquivos suportados: `.txt`, `.md`, `.json`, `.properties`, `.yaml`, `.yml`, `.rst`

---

## 📦 Uso prático com ChatGPT

1. Vá para **Explore GPTs** → **Create**
2. Em **Instructions**, cole o conteúdo de `instructions.txt`
3. Em **Knowledge**, envie os arquivos `upload1.txt`, `upload2.txt`, etc.

---

## 🔒 Regras e limites

- `instructions.txt`: máximo de 8.000 caracteres
- Uploads: até 100.000 caracteres cada, no máximo 20 arquivos
- Conteúdo duplicado entre instructions e uploads é evitado
- Arquivos que excederem os limites são ignorados

---

## 🧠 Autor

Criado por [Marcel Tanuri], com suporte do ChatGPT para automação de tarefas repetitivas em projetos com Liferay, AI e documentação técnica.