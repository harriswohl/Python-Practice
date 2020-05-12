
noun = input("Proper Noun: ")
verb = input("Verb (past tense): ")
instrument = input("Musical Instrument: ")

sentence = "What a jam. {} played a 20 minute solo on the {}. I almost {}!".format(noun.capitalize(), instrument.lower(), verb.lower())
print(sentence)
