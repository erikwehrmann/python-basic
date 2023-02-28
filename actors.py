import time

actors = [
    "Nathan Fillion",
    "Gina Torres",
    "Alan Tudyk",
    "Morena Baccarin",
    "Adam Baldwin",
    "Jewel Staite",
    "Sean Maher",
    "Summer Glau",
    "Ron Glass"
]

roles = [
    "Captain Malcolm Reynolds",
    "Zoe Washburn",
    "Hoban Washburn",
    "Inara Serra",
    "Jayne Cobb",
    "Kaylee Frye",
    "Dr. Simon Tam",
    "River Tam",
    "Derrial Book"
]

print("Featuring:")
print("=-=-=-=-=-=-=-=-=-=-=")
for char in actors:
    i = actors.index(char)
    print(actors[i], " as ", roles[i])
    time.sleep(0.5)
