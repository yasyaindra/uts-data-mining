# Nyari persentasi sentimen negatif dan positif
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def open_txt(txt):
    data = open(txt, 'r')
    return data.read()

def turn_to_array(text):
    tokenized = []
    
    if '\n' in text:
        for word in text.split('\n'):
            tokenized.append(word)
    else:     
        for word in text.split(' '):
            tokenized.append(word)

    return tokenized

def parsing_both_words(text, neg, pos):
    sentiment = {"negative": 0, "positive": 0}    
    for i in text:
        for j in neg:
            if i == j:
                sentiment["negative"] += 1
        for k in pos:
            if i == k:
                sentiment["positive"] += 1
                
    return sentiment

tweets = open_txt('tweets.txt')
neg_word = open_txt('wordlist/negative.txt')
pos_word = open_txt('wordlist/positive.txt')

# Stemming
stemmed_tweets   = stemmer.stem(tweets)

# Tokenization
tokenized_tweets = turn_to_array(stemmed_tweets)
tokenized_neg_words = turn_to_array(neg_word)
tokenized_pos_words = turn_to_array(pos_word)

# Parsing
counted_words = parsing_both_words(tokenized_tweets, tokenized_neg_words, tokenized_pos_words)

def please_percentage(count, neg, pos):
    total = round(count/count * 100)
    positive = round(pos/count * 100)
    negative = round(neg/count * 100)
    
    return {"total": f"{total}%","positive":f"{positive}%","negative":f"{negative}%"}
    
percentage = please_percentage(len(tokenized_tweets), counted_words['negative'], counted_words['positive'])

print("Tweet Pak Ridwan memiliki sentimen buruk" if percentage['negative'] > percentage['positive'] else "Tweet Pak Ridwan memiliki sentimen baik")