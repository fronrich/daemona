# modules for learning
from bs4 import BeautifulSoup
import requests
from src.utils.DirUtils import DirUtils
import nltk
from nltk.corpus import wordnet

du = DirUtils()
global NEG_WORDS, POS_WORDS

# get the synonyms of a word
def get_synonyms(word):

    synonyms = []

    for syn in wordnet.synsets(word.lower()):
        for lm in syn.lemmas():
            synonyms.append(lm.name())

    return list(set(synonyms))

# use wordnet to expand list, map, array, or set to include synonyms
def get_expanded_set(old_list):
    exp_set = set()
    old_set = set(old_list)
    for word in old_set:
        exp_set = exp_set.union(set(get_synonyms(word)))
    return exp_set if len(exp_set) > len(old_set) else set(old_list)

# read into ram as dp to save computation time
NEG_WORDS = get_expanded_set(du.read_csv_as_array(du.get_schema_dir(), 'neg_words.csv'))
POS_WORDS = get_expanded_set(du.read_csv_as_array(du.get_schema_dir(), 'pos_words.csv'))

# learn the sentiment of a word 
def learn_word_sentiment(word):
    # print(list(NEG_WORDS))
    # print(list(POS_WORDS))

    # generate a list of synonyms, including the word
    # score word based on -1 for each negative synonym and vice versa
    score = 0

    synonyms = get_synonyms(word)
    synonyms.append(word)

    for curr_word in set(synonyms):
        if curr_word in NEG_WORDS:
            score -= 1
        elif curr_word in POS_WORDS:
            score += 1
    return score

# learn how a statement makes daemona feel
def learn_statement_sentiment(statement):
    # identity adjectives
    text = nltk.word_tokenize(statement)
    result = nltk.pos_tag(text)
    # only include nouns, verbs, and adjectives
    def is_important(component_type, whitelist):
        return component_type in whitelist
    whitelist = ['NN', 'VV', 'JJ', 'VBG', 'NNS', 'NNPS', 'NNP']

    non_infinitive = [i for i in result if is_important(i[1], whitelist)]

    net_score = 0

    for pair in non_infinitive:
        word = pair[0]
        net_score += learn_word_sentiment(word)

    return net_score

# learn about the world by parsing actual real-world events for sentiment analysis
# returns current events, their link, and sentiment
def learn_social_context():
    # print('Getting Relevant Current Events')

    TOPIC_URL = 'https://womennewsnetwork.net/'
    response = requests.get(TOPIC_URL)


    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('article')
    headline_analysis = []
    for x in headlines:
        headline = x.text.strip().replace("\n", "").replace("\t", "")
        link = x.find_all('a', href=True)[0]['href']
        senitment = learn_statement_sentiment(headline)
        headline_analysis.append({"headline": headline, "url": link, "senitment": senitment})
    
    return headline_analysis


