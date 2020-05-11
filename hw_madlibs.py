
person = input("Person: ")
verb = input("Verb (past tense): ")
instrument = input("Musical Instrument: ")

sentance = "What a jam. {} played a 20 minute solo on the {}. I almost {}!".format(person.capitalize(), instrument.lower(), verb.lower())
print(sentance)
