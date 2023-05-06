f = open("C:\\Users\\bouta\\OneDrive\\Bureau\\hackathons\\Think AI\\src\\util\\data.txt", "r")
lines = f.read()
texts = []
for line in lines:
    texts.push({
        "recipe": line.strip(),
    })
