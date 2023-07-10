# author derrick shibero

from textblob import Word, TextBlob

def hello(word):
    print("hello ",word)

def get_definitions(words):
    for word in words:
        print(word,":")
        for sentence in Word(word).definitions:
            print("\t",sentence)

def get_singular(words):
    for word in words:
        print(word," => ",TextBlob(word).words.singularize()[0])

def get_plural(words):
    for word in words:
        print(word," => ",TextBlob(word).words.pluralize()[0])

def get_spell(words):
    for word in words:
        print(word," => ",TextBlob(word).correct())

def get_spellcheck(words):
    for word in words:
        print(word," => ",Word(word).spellcheck()[0][1])

def get_help():
    print("the dictionary app")
    print("\ts or singular [WORD..] => to check the singular of words")
    print("\tm or meaning [WORD..] => to check the meanings of words")
    print("\tc or correct [WORD..] => to check the correct spelling of words")
    print("\tp or plural [WORD..] => to check the plurals of words")
    print("\tsp or spellcheck [WORD..] => to check the level of spellings of a word")
    print("\th or help => display this help message")

