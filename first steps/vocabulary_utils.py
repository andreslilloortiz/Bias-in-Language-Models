import pandas as pd # type: ignore
import unicodedata

def normalize_token(token):
    token = token.strip().lower()
    token = unicodedata.normalize('NFD', token)
    token = "".join(c for c in token if not unicodedata.combining(c))
    return token

def load_token_vocabularies(male_tokens, female_tokens, proper_nouns_csv):

    proper_nouns = pd.read_csv(proper_nouns_csv)
    proper_nouns = proper_nouns.dropna(subset = ['Name'])
    proper_nouns_male = [normalize_token(token) for token in proper_nouns[proper_nouns['Gender'] == 'male']['Name']]
    proper_nouns_female = [normalize_token(token) for token in proper_nouns[proper_nouns['Gender'] == 'female']['Name']]

    male_set = set(proper_nouns_male + [normalize_token(token) for token in male_tokens])
    female_set = set(proper_nouns_female + [normalize_token(token) for token in female_tokens])

    return male_set - female_set, female_set - male_set