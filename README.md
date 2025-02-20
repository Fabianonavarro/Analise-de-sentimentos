# Análise de Sentimentos de Avaliações de Hotéis - Projeto Python

Este projeto tem como objetivo realizar a análise de sentimentos em avaliações de hotéis utilizando Python. A análise de sentimentos permite determinar se uma avaliação é positiva, negativa ou neutra. Para isso, utilizamos a biblioteca TextBlob, que é simples e eficiente para o processamento de linguagem natural (PLN).

# Objetivo do Projeto
O projeto visa analisar o sentimento de avaliações de hotéis de forma automatizada, destacando se os textos possuem um tom positivo, negativo ou neutro. Ele é projetado para ser executado localmente com Python, sem a necessidade de utilizar serviços de nuvem, como o Azure.

# Comparação com o Azure Language Studio
Embora o Azure Language Studio ofereça uma plataforma robusta com mais funcionalidades, como a extração de frases-chave e a análise de entidades, este projeto foca em uma abordagem simples e local usando Python. Ambos os projetos têm o mesmo objetivo: analisar o sentimento de avaliações de hotéis.

# Funcionalidades
Leitura de arquivos de texto: O script lê avaliações de hotéis a partir de arquivos de texto.
Análise de Sentimentos: O script analisa cada sentença de cada avaliação, retornando a polaridade e o sentimento (positivo, negativo ou neutro).
Armazenamento de Resultados: O script salva a análise em um arquivo de texto na pasta results.
Lógica de Substituição ou Acrescentamento: Se o arquivo de resultados já existir, o usuário pode optar por substituir ou acrescentar um número sequencial no nome do arquivo.

# Estrutura do Projeto
├── inputs/                     # Pasta para armazenar as avaliações de hotéis (arquivos .txt)

│   ├── example_reviews.txt     # Exemplo de avaliações de hotéis

├── results/                    # Pasta onde as análises serão salvas

│   ├── reviews_analise_en.txt  # Resultado da análise

├── analyze_sentiments.py       # Script principal de análise de sentimentos

├── requirements.txt            # Configurarção das bibliotecas usada

├── readme.md                   # Este arquivo README


# Pré-requisitos

Para rodar este projeto, você precisará ter o Python 3.x instalado em seu sistema. Além disso, você deve instalar as dependências abaixo:

pip install -r requirements.txt

Ou manualmente, utilizando os seguintes pacotes:

textblob==0.17.1
nltk==3.7

# Como Usar

# 1. Estrutura de Pastas

Crie duas pastas principais:

inputs/: Onde você colocará os arquivos de avaliação de hotéis (um arquivo .txt com as avaliações).
results/: Onde a análise será salva.
Exemplo de avaliação em inputs/example_reviews.txt:

This is an old hotel and the room furnishings are average.
The internet didn't work and had to come to one of their office rooms to check in for my flight home.
The website says it's close to the British Museum, but it's too far to walk.

# 2. Executando o Script

Para rodar o script de análise de sentimentos, execute o seguinte comando no terminal:

python analyze_sentiments.py

Ler o arquivo de avaliação da pasta inputs/.
Analisar o sentimento de cada sentença.
Salvar o resultado na pasta results/.
Se um arquivo já existir na pasta results/, o script perguntará se você deseja substituir ou acrescentar um número sequencial ao nome do arquivo.

# 3. Exemplo de Saída

O arquivo de saída gerado será um arquivo .txt na pasta results/, com o seguinte formato:

makefile
Copiar
Análise de Sentimentos:

Sentença: Tired hotel with poor service.
Sentimento: Negativo

Sentença: The Royal Hotel, London, United Kingdom 5/6/2018
Sentimento: Neutro

Sentença: This is an old hotel and the room furnishings are average.
Sentimento: Neutro

...

# Conclusão
Este projeto é uma introdução à análise de sentimentos e ao uso de Python para Processamento de Linguagem Natural (PLN). A partir dele, você pode explorar mais ferramentas e técnicas de PLN, como a extração de entidades e a análise de frases-chave, ou integrar o código com soluções baseadas em nuvem para maior escalabilidade.

# ''Sobre o Azure AI Language Studio''
Embora este projeto seja implementado em Python localmente, o Azure AI Language Studio oferece funcionalidades semelhantes, como a análise de sentimentos e a extração de frases-chave, mas com a vantagem de uma plataforma pronta para uso, escalável e integrada com outros serviços da Microsoft.

Para saber mais sobre o Azure AI Language Studio, acesse Azure Language Studio.

# Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

---
MIT License

Copyright (c) [2025] [Fabiano Navarro]

Aqui está o texto completo da licença MIT:

Permite-se que qualquer pessoa obtenha uma cópia deste software e de seus arquivos de documentação associados (o "Software"), para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e para permitir que outras pessoas o façam, desde que a seguinte condição seja atendida:

O aviso de copyright e este aviso de permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "NO ESTADO EM QUE SE ENCONTRA", SEM GARANTIAS DE QUALQUER TIPO, EXPRESSAS OU IMPLÍCITAS, INCLUINDO, MAS NÃO SE LIMITANDO A, GARANTIAS DE COMERCIABILIDADE, ADEQUAÇÃO A UM FIM ESPECÍFICO E NÃO INFRAÇÃO. EM NENHUM CASO OS AUTORES OU DETENTORES DO DIREITO AUTORAL SERÃO RESPONSÁVEIS POR QUALQUER REIVINDICAÇÃO, DANO OU OUTRO RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, DANO OU OUTRO, DECORRENTE DE, FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO SOFTWARE.
