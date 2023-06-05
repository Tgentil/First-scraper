# Web Scraper

Este é um script de web scraping desenvolvido como um teste inicial para aprender sobre o tema. O objetivo deste script é extrair informações relacionadas a uma palavra de um site específico. Neste caso, utilizei-o para selecionar notícias do Avaí.

**Instalação de Dependências**: Certifique-se de ter as bibliotecas necessárias instaladas em seu ambiente Python. Nesse caso, você precisará do `requests` e do `beautifulsoup4`. Você pode instalá-los usando o gerenciador de pacotes pip:
   ```
   pip install requests beautifulsoup4
   ```
## Funcionalidade

O script utiliza a biblioteca `requests` para fazer uma requisição HTTP para a URL do site desejado. Em seguida, utiliza a biblioteca `BeautifulSoup` para analisar o HTML da página e encontrar os elementos que contêm as notícias.

O script itera sobre as notícias encontradas e verifica se contêm o termo "Avaí" no título ou no conteúdo. Caso o termo seja encontrado, o script exibe o título, o link e, se disponível, um trecho do conteúdo da notícia.


## Exemplo de Saída

```
Família de Roberto, do Avaí, acompanha jogo no dia do aniversário do zagueiro em Caxias
https://ge.globo.com/sc/futebol/times/avai/noticia/2023/06/05/familia-de-roberto-do-avai-acompanha-jogo-no-dia-do-aniversario-do-zagueiro-em-caxias.ghtml

Avaí leva vantagem sobre o Juventude no histórico do confronto; confira os números
https://ge.globo.com/sc/futebol/times/avai/noticia/2023/06/02/avai-leva-vantagem-sobre-o-juventude-no-historico-do-confronto-confira-os-numeros.ghtml

Avaí negocia com o executivo Eduardo Freeland, ex-Botafogo e Bahia
https://ge.globo.com/sc/futebol/times/avai/noticia/2023/06/02/avai-negocia-com-o-executivo-eduardo-freeland-ex-botafogo-e-bahia.ghtml

Com novidades, Avaí embarca para enfrentar o Juventude; confira os relacionados
https://ge.globo.com/sc/futebol/times/avai/noticia/2023/06/01/com-novidades-avai-embarca-para-enfrentar-o-juventude.ghtml

Ex-Avaí, Arthur Chaves completa primeira temporada na Europa
https://ge.globo.com/sc/futebol/times/avai/noticia/2023/06/01/ex-avai-arthur-chaves-completa-primeira-temporada-na-europa.ghtml

Com dengue, Ricardo Bueno vira desfalque no Avaí
https://ge.globo.com/sc/futebol/times/avai/noticia/2023/05/31/com-dengue-ricardo-bueno-vira-desfalque-no-avai.ghtml

```

## Considerações

Este script é um exemplo básico de web scraping e pode ser aprimorado de várias maneiras, como tratamento de erros, extração de mais informações relevantes ou integração com outras ferramentas e APIs.

# Autor
* Thiago Da Silveira Gentil