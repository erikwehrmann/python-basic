journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

journey = journey.replace("tone", "town")
journey = journey.replace("Leaving", "Living")
journey = journey.replace("whirl", "world")
journey = journey.replace("tray", "train")
journey = journey.replace("seedy", "city")
journey = journey.replace("Bored", "Born")
journey = journey.replace(" or something", "")

print(journey)
