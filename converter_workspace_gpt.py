import os
from pathlib import Path

# -----------------------------
# Configurações
# -----------------------------
LIMIT_INSTRUCTIONS = 8000          # Máx. caracteres em instructions.txt
LIMIT_FILE_CHARS   = 100000        # Máx. caracteres por uploadX.txt
MAX_UPLOAD_FILES   = 20            # Máx. quantidade de uploads gerados
EXTENSOES_SUPORTADAS = ('.txt', '.md', '.json', '.properties', '.yaml', '.yml', '.rst')

# Pastas padrão dentro da workspace de origem
INSTRUCTIONS_DIR_NAME = 'instructions'      # Arquivos aqui vão para instructions.txt
UPLOAD_DIR_NAME       = 'additional_info'   # Arquivos aqui vão para uploadX.txt

# -----------------------------
# Funções utilitárias
# -----------------------------

def coletar_arquivos_texto(diretorio_base: Path):
    """Retorna lista de tuplas (nome_relativo, conteudo) para arquivos suportados."""
    arquivos = []
    if not diretorio_base.exists():
        return arquivos

    for root, _, files in os.walk(diretorio_base):
        for nome in sorted(files):
            if nome.lower().endswith(EXTENSOES_SUPORTADAS):
                caminho = Path(root) / nome
                try:
                    with open(caminho, 'r', encoding='utf-8') as f:
                        conteudo = f.read()
                        nome_relativo = caminho.relative_to(diretorio_base).as_posix()
                        arquivos.append((nome_relativo, conteudo))
                except Exception as e:
                    print(f"[WARN] Erro ao ler {caminho}: {e}")
    return arquivos


def salvar(destino: Path, nome: str, conteudo: str):
    destino.mkdir(parents=True, exist_ok=True)
    caminho = destino / nome
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo.strip())

# -----------------------------
# Processo principal
# -----------------------------

def gerar_instrucao_e_uploads(workspace: str, destino: str):
    workspace_path = Path(workspace).resolve()
    destino_path   = Path(destino).resolve()

    # 1️⃣ Arquivos para instructions.txt
    pasta_instructions = workspace_path / INSTRUCTIONS_DIR_NAME
    arquivos_instr = coletar_arquivos_texto(pasta_instructions)

    # 2️⃣ Arquivos para uploads
    pasta_uploads = workspace_path / UPLOAD_DIR_NAME
    arquivos_upload = coletar_arquivos_texto(pasta_uploads)

    # ----------------- Monta instructions.txt -----------------
    instructions = ""
    for nome, conteudo in arquivos_instr:
        bloco = f"\n\n### {nome}\n\n{conteudo.strip()}"
        if len(instructions) + len(bloco) <= LIMIT_INSTRUCTIONS:
            instructions += bloco
        else:
            print(f"[INFO] Limite de {LIMIT_INSTRUCTIONS} caracteres em instructions atingido. Restante ignorado.")
            break

    # ----------------- Monta uploads -----------------
    uploads = []
    atual = ""
    for nome, conteudo in arquivos_upload:
        bloco = f"\n\n### {nome}\n\n{conteudo.strip()}"
        if len(atual) + len(bloco) > LIMIT_FILE_CHARS:
            uploads.append(atual)
            atual = ""
            if len(uploads) >= MAX_UPLOAD_FILES:
                print(f"[INFO] Limite de {MAX_UPLOAD_FILES} arquivos de upload atingido. Restante ignorado.")
                break
        atual += bloco
    if atual and len(uploads) < MAX_UPLOAD_FILES:
        uploads.append(atual)

    # ----------------- Salva saídas -----------------
    salvar(destino_path, 'instructions.txt', instructions)
    for idx, conteudo in enumerate(uploads, 1):
        salvar(destino_path, f'upload{idx}.txt', conteudo)

    # ----------------- Resumo -----------------
    print("================ RESUMO ================")
    print(f"Instructions.txt: {len(instructions)} caracteres")
    print(f"Uploads gerados: {len(uploads)}")
    for i, u in enumerate(uploads, 1):
        print(f"  - upload{i}.txt: {len(u)} caracteres")
    print("========================================")

# -----------------------------
# CLI
# -----------------------------
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Converter workspace de conhecimento em instructions + uploads para GPT customizado.")
    parser.add_argument("--origem", required=True, help="Pasta raiz da workspace.")
    parser.add_argument("--destino", required=True, help="Pasta onde serão salvos instructions.txt e uploadX.txt.")

    args = parser.parse_args()

    gerar_instrucao_e_uploads(args.origem, args.destino)
