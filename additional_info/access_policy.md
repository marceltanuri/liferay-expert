[Dica rápida sobre Service Access Policy no Liferay]

Quando você acessar o API Explorer (ex: /o/api?endpoint=...), tem agora um botão de copiar ao lado de cada método (GET, POST etc). Ele copia automaticamente a assinatura exata que precisa ser usada na configuração da política de acesso, como:
com.liferay.portal.search.rest.internal.resource.v1_0.SearchResultResourceImpl#getSearchPage

É só colar isso na aba "Advanced Mode" da Service Access Policy. Bem mais fácil agora.
