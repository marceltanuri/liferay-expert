[Curiosidade – CMS 2.0 local com build a partir da master]


Pessoal, deixo aqui registrado um experimento técnico que fiz por curiosidade: subir o Liferay localmente a partir da branch master para testar o CMS 2.0, que está em desenvolvimento.

O CMS 2.0 será um novo produto SaaS da Liferay, inspirado em plataformas como Contentful e Acquia. Ele já vem sendo divulgado publicamente como uma das promessas para o próximo ano — inclusive foi mencionado no último Customer Summit em São Paulo.
Quanto ao build direto da master, foi necessário porque essa feature ainda não está disponível nos releases oficiais. Achei interessante compartilhar porque o processo não é tão moroso quanto parece — o build completo levou cerca de 25 minutos com ANT_OPTS=-Xmx6g.

Passos que segui para rodar localmente:

1. Clonar o repositório (nesse caso do CMS 2.0 pode ser o público CE mesmo):
git clone https://github.com/liferay/liferay-portal.git && cd liferay-portal
2. Instalar o Ant (necessário para orquestrar o build, mesmo que os módulos usem Gradle).
3. Configurar memória para o Ant:
export ANT_OPTS="-Xmx6g"
4. Rodar o build completo:
ant all
5. Criar o arquivo portal-ext.properties dentro da pasta bundles/, com as seguintes flags:
setup.wizard.enabled=false
default.admin.email.address=admin@liferay.com
...
feature.flag.LPD-17564=true    # CMS 2.0
feature.flag.LPD-11232=true    # Search API
feature.flag.LPD-34594=true    # Views: All, Content, Files, Structures
6. Após o portal iniciar, ir até Control Panel > Sites > Site Initializers e criar um site com o template “New CMS”.
7. Acessar o CMS 2.0 em:
http://localhost:8080/web/cms/
