import nltk.tree
import nltk.chunk

sentence = "Good diagrams are an importat tool"

words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words, lang='eng')

# Diccionario con las etiquetas POS  y sus significados
tag_names = {
    "CC": "Coordinating conjunction",
    "CD": "Cardinal number",
    "DT": "Determiner",
    "EX": "Existential there",
    "FW": "Foreign word",
    "IN": "Preposition or subordinating conjunction",
    "JJ": "Adjective",
    "JJR": "Adjective, comparative",
    "JJS": "Adjective, superlative",
    "LS": "List item marker",
    "MD": "Modal",
    "NN": "Noun, singular or mass",
    "NNS": "Noun, plural",
    "NNP": "Proper noun, singular",
    "NNPS": "Proper noun, plural",
    "PDT": "Predeterminer",
    "POS": "Possessive ending",
    "PRP": "Personal pronoun",
    "PRP$": "Possessive pronoun",
    "RB": "Adverb",
    "RBR": "Adverb, comparative",
    "RBS": "Adverb, superlative",
    "RP": "Particle",
    "SYM": "Symbol",
    "TO": "to",
    "UH": "Interjection",
    "VB": "Verb, base form",
    "VBD": "Verb, past tense",
    "VBG": "Verb, gerund or present participle",
    "VBN": "Verb, past participle",
    "VBP": "Verb, non-3rd person singular present",
    "VBZ": "Verb, 3rd person singular present",
    "WDT": "Wh-determiner",
    "WP": "Wh-pronoun",
    "WP$": "Possessive wh-pronoun",
    "WRB": "Wh-adverb"
}

grammar = nltk.RegexpParser('''
    NP: {<DT>?<JJ>*<NN>+} # un grupo nominal
    PP: {<IN><NP>} # un grupo preposicional
    VP: {<VB.*><NP|PP>*} # un grupo verbal
    ''')

full_tags = []
for word, tag in tags:
    full_tag = tag_names.get(tag, "Unknown")  #obtiene el nombre completo del metodo POS, o "Unknown" si no está en el diccionario
    full_tags.append((word, full_tag))
    print(word, full_tag)

print()
tree = grammar.parse(tags)
print(tree)
# (S
#   (NP El/DT niño/NN)
#   (VP juega/VB (PP con/IN (NP su/DT perro/NN)) (PP en/IN (NP el/DT parque/NN))))

tree.draw()


subtrees = list(tree.subtrees())
for subtree in subtrees:
    label = subtree.label()
    if label == 'NP':
        print('Sujeto:', subtree)
    # Sujeto: (NP El/DT niño/NN)
    # Sujeto: (NP su/DT perro/NN)
    # Sujeto: (NP el/DT parque/NN)
    elif label == 'VP':
        print('Predicado:', subtree)
    # Predicado: (VP juega/VB (PP con/IN (NP su/DT perro/NN)) (PP en/IN (NP el/DT parque/NN)))
    elif label == 'VB':
        print('Verbo:', subtree)
    # Verbo: (VB juega)

