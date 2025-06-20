[CI/CD PaaS - falha no build: No artifacts found that match the file pattern "build/**". - Resolvido] 

Oi time,
Recentemente enfrentamos um problema com o pipeline do Jenkins, onde o build falhava com a mensagem:
ERROR: No artifacts found that match the file pattern "build/**". Configuration error?
Contexto do Problema:
O pipeline estava falhando porque o token de SCM usado para autenticação no Azure DevOps estava com permissões insuficientes ou expirado.
Esse problema foi descrito na documentação da Liferay em um artigo do Fast Track:
 Liferay Support - Jenkins Build Failed - No Artifacts Found
Como Resolvemos:
Verificamos o token atual do SCM e identificamos que ele retornava 403 Forbidden, indicando problema de permissões.
Geramos um novo token temporário com Code: Read e testamos diretamente com o comando:
curl -s -o /dev/null -w "OLD_TOKEN: %{http_code}\n" -H "Authorization: Bearer $OLD_TOKEN" \
     "https://dev.azure.com/Accelerate-25/DXP-Liferay/_apis/git/repositories?api-version=6.0"

curl -s -o /dev/null -w "NEW_TOKEN: %{http_code}\n" -H "Authorization: Bearer $NEW_TOKEN" \
     "https://dev.azure.com/Accelerate-25/DXP-Liferay/_apis/git/repositories?api-version=6.0"
O resultado mostrou claramente o problema:
OLD_TOKEN: 403 (Forbidden)
NEW_TOKEN: 200 (Success)
Com o novo token, o pipeline voltou a funcionar normalmente.
Recomendação:
Se encontrarem esse problema novamente:
Verifiquem o token do SCM e testem diretamente com o comando acima.
Garanta que o token tenha o escopo mínimo de Code: Read.
Se o problema persistir, revisem as variáveis de ambiente do Jenkins e a configuração do SCM.
