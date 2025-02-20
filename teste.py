import os
import nltk
from textblob import TextBlob
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree

# Baixar os recursos necessários do nltk (executar apenas uma vez)
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def analyze_sentiment_with_explanation(text, language='en'):
    # Criar o objeto TextBlob
    blob = TextBlob(text)
    
    # Obter a polaridade
    sentiment_polarity = blob.sentiment.polarity
    
    # Determinar o sentimento com base na polaridade
    if sentiment_polarity > 0:
        sentiment = "Positivo" if language == 'pt' else "Positive"
        explanation = f"A avaliação é positiva porque a polaridade é {sentiment_polarity:.2f}, indicando um tom positivo na linguagem usada."
    elif sentiment_polarity < 0:
        sentiment = "Negativo" if language == 'pt' else "Negative"
        explanation = f"A avaliação é negativa porque a polaridade é {sentiment_polarity:.2f}, indicando um tom negativo na linguagem usada."
    else:
        sentiment = "Neutro" if language == 'pt' else "Neutral"
        explanation = f"A avaliação é neutra porque a polaridade é {sentiment_polarity:.2f}, sem forte indicação de sentimentos positivos ou negativos."
    
    return sentiment, explanation

def extract_entities(text, language='en'):
    # Tokenizar o texto e realizar a marcação de partes do discurso (POS)
    words = word_tokenize(text, language="portuguese" if language == 'pt' else 'english')
    tagged_words = pos_tag(words)

    # Realizar o reconhecimento de entidades nomeadas
    named_entities = ne_chunk(tagged_words)
    
    # Extrair entidades nomeadas
    entities = []
    for subtree in named_entities:
        if isinstance(subtree, Tree):
            entity = " ".join([word for word, tag in subtree])
            entities.append((entity, subtree.label()))
    
    return entities

def process_reviews(file_path, language='en'):
    # Abrir o arquivo com codificação UTF-8
    with open(file_path, "r", encoding='utf-8') as file:
        reviews = file.readlines()

    analysis_results = []
    for review in reviews:
        sentiment, sentiment_explanation = analyze_sentiment_with_explanation(review, language)
        entities = extract_entities(review, language)
        entities_explanation = "Nenhuma entidade nomeada foi encontrada." if not entities else f"Foram encontradas as seguintes entidades nomeadas: {', '.join([f'{entity[0]} ({entity[1]})' for entity in entities])}."
        
        analysis_results.append({
            "review": review.strip(),
            "sentiment": sentiment,
            "sentiment_explanation": sentiment_explanation,
            "entities": entities,
            "entities_explanation": entities_explanation
        })
    
    return analysis_results

def save_analysis_to_file(analysis_results, save_path, language='en'):
    # Verificar se a pasta results existe, se não, criar
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Salvar o arquivo com codificação UTF-8
    with open(save_path, 'w', encoding='utf-8') as f:
        for result in analysis_results:
            f.write(f"Review: {result['review']}\n")
            f.write(f"Sentimento: {result['sentiment']}\n")
            f.write(f"Explicação do Sentimento: {result['sentiment_explanation']}\n")
            f.write(f"Entidades: {result['entities_explanation']}\n\n")
    print(f"Análise salva em: {save_path}")

def main():
    # Listar os arquivos de review na pasta 'inputs'
    input_folder = 'inputs'
    files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    if not files:
        print("Nenhum arquivo de review encontrado na pasta 'inputs'.")
        return
    
    print("Arquivos de review disponíveis:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")

    # Solicitar ao usuário para escolher um arquivo
    choice = int(input("Escolha o número do arquivo para analisar: "))
    if choice < 1 or choice > len(files):
        print("Escolha inválida!")
        return
    
    selected_file = files[choice - 1]
    file_path = os.path.join(input_folder, selected_file)

    # Perguntar ao usuário para escolher o idioma
    print("\nEscolha o idioma para a análise:")
    print("1. Inglês")
    print("2. Português")
    language_choice = input("Digite o número do idioma (1 para Inglês, 2 para Português): ").strip()

    if language_choice == '1':
        language = 'en'
    elif language_choice == '2':
        language = 'pt'
    else:
        print("Escolha inválida!")
        return

    print(f"\nAnalisando o arquivo: {selected_file} em {'Inglês' if language == 'en' else 'Português'}")

    # Processar as reviews do arquivo escolhido
    analysis_results = process_reviews(file_path, language)

    # Exibir resultados na tela
    for result in analysis_results:
        print(f"\nAnalisando: {result['review']}")
        print(f"Sentimento: {result['sentiment']}")
        print(f"Explicação do Sentimento: {result['sentiment_explanation']}")
        print(f"Entidades: {result['entities_explanation']}")

    # Perguntar se o usuário deseja salvar a análise
    save_choice = input("\nVocê deseja salvar a análise na pasta 'results'? (s/n): ").strip().lower()
    if save_choice == 's':
        # Caminho para salvar os resultados na pasta 'results'
        save_folder = 'results'
        save_file = selected_file.replace(".txt", f"_analise_{language}.txt")
        save_path = os.path.join(save_folder, save_file)
        save_analysis_to_file(analysis_results, save_path, language)

if __name__ == "__main__":
    main()
