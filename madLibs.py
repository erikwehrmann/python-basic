madLib = """Today I went to the zoo. I saw a(n)
___________(adjective1) ___________(noun1) jumping up and down in its tree.
He ___________(verb1) ___________(adverb1)
through the large tunnel that led to its ___________(adjective2)
___________(noun2). I got some peanuts and passed
them through the cage to a gigantic gray ___________(noun3)
towering above my head. Feeding that animal made
me hungry. I went to get a ___________(adjective3) scoop
of ice cream. It filled my stomach. Afterwards I had to
___________(verb2) ___________(adverb2) to catch our bus.
When I got home I ___________(verb3) my
mom for a ___________(adjective4) day at the zoo."""
adjective1 = input("Tell me an adjective \n")
madLib = madLib.replace("___________(adjective1)", adjective1)
noun1 = input("Tell me a noun \n")
madLib = madLib.replace("___________(noun1)", noun1)
verb1 = input("Tell me a verb in the past tense \n")
madLib = madLib.replace("___________(verb1)", verb1)
adverb1 = input("Tell me an adverb \n")
madLib = madLib.replace("___________(adverb1)", adverb1)
adjective2 = input("Tell me an adjective \n")
madLib = madLib.replace("___________(adjective2)", adjective2)
noun2 = input("Tell me a noun \n")
madLib = madLib.replace("___________(noun2)", noun2)
noun3 = input("Tell me a noun \n")
madLib = madLib.replace("___________(noun3)", noun3)
adjective3 = input("Tell me an adjective \n")
madLib = madLib.replace("___________(adjective3)", adjective3)
verb2 = input("Tell me a verb \n")
madLib = madLib.replace("___________(verb2)", verb2)
adverb2 = input("Tell me an adverb \n")
madLib = madLib.replace("___________(adverb2)", adverb2)
verb3 = input("Tell me a verb in the past tense \n")
madLib = madLib.replace("___________(verb3)", verb3)
adjective4 = input("Tell me an adjective \n")
madLib = madLib.replace("___________(adjective4)", adjective4)
print(madLib)
