import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


# Function to perform tokenization, stemming, lemmatization, sentence tokenization, and stop word removal
def process_text(input_text):
    # Sentence Tokenization
    sentences = sent_tokenize(input_text)

    # Tokenization
    tokens = word_tokenize(input_text)

    # Remove Stop Words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    return sentences, tokens, filtered_tokens, stemmed_tokens, lemmatized_tokens

# Function to write tokens to a file
def write_to_file(tokens, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(tokens))

# Function to process input file and generate output files
def process_and_save_files(input_file_path):
    # Read input text from a file
    with open(r"C:\Users\arshb\OneDrive\Desktop\sub\SEM VI\NLP\lab 2\text.txt") as file:
        input_text = file.read()

    # Process the text
    sentences, tokens, filtered_tokens, stemmed_tokens, lemmatized_tokens = process_text(input_text)

    # Write tokens to files
    write_to_file(sentences, 'sentences.txt')
    write_to_file(tokens, 'tokenized.txt')
    write_to_file(filtered_tokens, 'filtered.txt')
    write_to_file(stemmed_tokens, 'stemmed.txt')
    write_to_file(lemmatized_tokens, 'lemmatized.txt')

    print("Files generated successfully: sentences.txt, tokenized.txt, filtered.txt, stemmed.txt, lemmatized.txt")

# Replace 'input.txt' with the path to your input text file
input_file_path = 'input.txt'
process_and_save_files(input_file_path)
