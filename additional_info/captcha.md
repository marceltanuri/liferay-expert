Sobre desativação do captcha para operações administrativas siga essas instruções: Usar em local env somente

1. Adicionar ao portal-ext.properties
captcha.enforce.disabled=true

Ou via variavel de ambiente, se preferir
LIFERAY_CAPTCHA_PERIOD_ENFORCE_PERIOD_DISABLED=true

Feito isso, seja por variavel de ambiente, ou por arquivo de propriedades, deve agora adicionar a pasta osgi/configs o arquivo com.liferay.captcha.configuration.CaptchaConfiguration.config com o seguinte conteúdo
maxChallenges=I"-1"