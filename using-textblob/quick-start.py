from textblob import TextBlob
from textblob import Word
import nltk
import ssl

# nltk defitions requirement
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
# nltk.download()

# Natural language
wiki = TextBlob(
    "Python is a high-level, general-purpose programming language.")
print(wiki.tags)
print(wiki.noun_phrases)

# Sentiment analysis (positive, negative, neutral)
testimonial = TextBlob("Peace, love, and harmony")
print(testimonial.sentiment)

# Breakdown
zen = TextBlob("Beautiful is better than ugly. "
               "Explicit is better than implicit. "
               "Simple is better than complex.")
print(zen.words)
print(zen.sentences)

# Inflection
sentence = TextBlob('Use 4 spaces per indentation level.')
print(sentence.words.pluralize())

# Lemmatize
w = Word("octopi")
print(w.lemmatize())

# Defintions
print(Word("octopus").definitions)

# Spelling Correction
b = TextBlob("I havv goood speling!")
print(b.correct())

# Translate
en_blob = TextBlob(u'Simple is better than complex.')
print(en_blob.translate(to='es'))

# Language Detect
b = TextBlob(u"بسيط هو أفضل من مجمع")
print(b.detect_language())
