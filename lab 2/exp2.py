import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

def process_text(input_text):
    sentences = sent_tokenize(input_text)
    tokens = word_tokenize(input_text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return sentences, tokens, filtered_tokens, stemmed_tokens, lemmatized_tokens

def write_to_file(tokens, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(tokens))

#input file path address 
def process_files(input_path):
    with open(r"") as file:
        input_text = file.read()

    sentences, tokens, filtered_tokens, stemmed_tokens, lemmatized_tokens = process_text(input_text)

    write_to_file(sentences, 'sentences.txt')
    write_to_file(tokens, 'tokenized.txt')
    write_to_file(filtered_tokens, 'filtered.txt')
    write_to_file(stemmed_tokens, 'stemmed.txt')
    write_to_file(lemmatized_tokens, 'lemmatized.txt')

    print("Files generated successfully: sentences.txt, tokenized.txt, filtered.txt, stemmed.txt, lemmatized.txt")

input_path = 'text.txt'
process_files(input_path)
