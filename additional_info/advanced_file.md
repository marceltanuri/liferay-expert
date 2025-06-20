[Como o AdvancedFileSystemStore monta o caminho de um arquivo]
o AdvancedFileSystemStore é uma versão mais "avançada" do FileSystemStore e organiza os arquivos no sistema de arquivos. A ideia principal é distribuir os arquivos para evitar diretórios gigantes e melhorar a performance.

:one: O Básico: Raiz + Identificadores Tudo começa com um diretório raiz configurado, seguido pelo companyId e repositoryId. Ex: [raiz_do_armazenamento]/[companyId]/[repositoryId]/

:two: Lidando com Nomes e Extensões
A extensão do arquivo é separada (ex: .jpg).
Se não tiver extensão, ele usa uma padrão: _HOOK_EXTENSION (que é .afsh).
O nome do arquivo sem a extensão é o que chamamos de fileNameFragment.

:three: O Truque do "DLFE-" Se o fileNameFragment começar com DLFE- (um prefixo comum para arquivos de Documentos e Mídia):
Esse prefixo é removido do fileNameFragment.
E DLFE/ é adicionado no começo da estrutura de diretórios que vamos montar. Isso agrupa esses arquivos.

:four: buildPath: A Mágica do Aninhamento! O método buildPath pega o fileNameFragment (já sem o "DLFE-") e:
Quebra ele em pedaços de 2 caracteres.
Cada pedaço vira um subdiretório.
Ex: Se o fragmento for documentoimportante, ele pode gerar algo como do/cu/me/.
Isso tem um limite de profundidade (atualmente 3 níveis criados pelo buildPath, mais o DLFE/ se aplicável).

:five: Juntando Tudo: O Diretório do Arquivo (getFileNameDir) Para um arquivo chamado DLFE-documentoimportante.txt:
fileNameFragment (sem "DLFE-") = documentoimportante
buildPath gera: do/cu/me/ (simplificando)
O diretório que conterá as versões desse arquivo será: [raiz]/[coId]/[repoId]/DLFE/do/cu/me/documentoimportante.txt/ (Note que o nome original com extensão vira o nome do diretório final que agrupa as versões)

:six: Finalmente, o Arquivo Versionado! (getFileNameVersionFile) Dentro do diretório que acabamos de ver, cada versão do arquivo é nomeada assim: fileNameFragment_versao.extensao.
Para a versão "1.0" do nosso DLFE-documentoimportante.txt: [raiz]/[coId]/[repoId]/DLFE/do/cu/me/documentoimportante.txt/documentoimportante_1.0.txt

Essa estrutura de "sharding" (fragmentação) ajuda a:
Evitar que um único diretório tenha milhares de arquivos (o que pode deixar o sistema de arquivos lento).
Manter uma organização lógica, mesmo que um pouco mais complexa à primeira vista.