foosballers = [
    "Mia", "Retta", "Augustine", "Jin", "Waylon", "Alphonso", "Sage", "Hubert",
    "Raymon", "Rebecca", "Monty", "Glen", "Christi", "Patrice", "Craig",
    "Dexter", "Wally", "Ian", "Pat"
]

midIndex = int(len(foosballers) / 2)
print(foosballers[midIndex])
print(foosballers[midIndex - 2:midIndex + 3])
foosballers.insert(midIndex, "Average Player")
foosballers[midIndex] = "AVERAGE PLAYER"
foosballers.append("Durk")
foosballers.append("Lump")
foosballers.append("Cap'n")
foosballers.append("Damian")
foosballers.append("Barnett")
del foosballers[midIndex]
midIndex = int(len(foosballers) / 2)
foosballers.insert(midIndex, "AVERAGE PLAYER")
hubertIndex = foosballers.index("Hubert")
foosballers.insert(hubertIndex, "Lucy")
rebeccaIndex = foosballers.index("Rebecca")
foosballers.insert(rebeccaIndex + 1, "Omar")
foosballers.insert(7, "Otto")
foosballers.insert(-9, "Chauncey")
print(foosballers)
del foosballers[foosballers.index("AVERAGE PLAYER")]
midIndex = int(len(foosballers) / 2)
foosballers.insert(midIndex, "AVERAGE PLAYER")
print(foosballers)
