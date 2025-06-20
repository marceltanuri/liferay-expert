# Conversor de Workspace para GPT Customizado

Este script converte uma workspace local de conhecimento técnico em dois formatos adequados para criação de um GPT customizado no ChatGPT:

* Um arquivo `instructions.txt` contendo até 8.000 caracteres para o campo de instruções.
* Até 20 arquivos `uploadX.txt` com conteúdos adicionais para upload como base de conhecimento.

---

## 📁 Estrutura esperada da workspace

A pasta de origem deve conter duas subpastas principais:

```
meu_conhecimento/
├── instructions/        # Conteúdo principal, vai para instructions.txt
│   ├── resumo.md
│   └── boas_praticas.txt
└── additional_info/     # Conteúdo complementar, vai para uploadX.txt
    ├── casos_de_uso/
    │   └── exemplo1.md
    └── docs.json
```

Arquivos aceitos: `.txt`, `.md`, `.json`, `.properties`, `.yaml`, `.yml`, `.rst`

---

## ▶️ Como usar

Execute o script passando a pasta de origem e o destino de saída:

```bash
python converter_workspace_gpt.py \
  --origem ./meu_conhecimento \
  --destino ./saida
```

Após a execução, serão criados:

* `instructions.txt` (até 8.000 caracteres)
* `upload1.txt`, `upload2.txt`, ... (cada um com até 100.000 caracteres, no máximo 20 arquivos)

---

## 📦 Exemplo de uso prático

Esse conteúdo pode ser utilizado para criar um GPT personalizado via ChatGPT (Plus):

1. Vá para "Explore GPTs" → "Create"
2. Em **Instructions**, cole o conteúdo de `instructions.txt`
3. Em **Knowledge**, envie os arquivos `uploadX.txt`

---

## 🔒 Observações

* O script evita duplicidade: o que está em `instructions.txt` não será incluído nos uploads.
* Se `instructions/` exceder 8.000 caracteres, o restante será ignorado.
* Se `additional_info/` gerar mais de 20 uploads ou arquivos muito grandes, o excesso será ignorado.

---

## 🛠️ Dependências

Nenhuma. O script usa apenas bibliotecas padrão do Python 3.

---

## 🧠 Autor

Criado por \[Marcel Tanuri], com suporte de ChatGPT para automação de tarefas repetitivas em projetos com Liferay, AI e documentação técnica.
