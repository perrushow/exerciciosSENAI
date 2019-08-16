dict = {
    "purple": 0,
    "rain": 0,
    "you": 0,
    "laughing": 0,
}

music = open("purplerain.txt","r")

for linha in music:
    words = linha.split(" ")
    for word in words:
        word.strip()
        print (word)
        if word == "purple" or word == "Purple":
            dict["purple"] += 1
            continue
        if word == "rain" or word == "rain," or word == "rain\n":
            dict["rain"] += 1
            continue
        if word == "you" or word == "You" or word == "you\n":
            dict["you"] += 1
            continue
        if word.capitalize() == "laughing".capitalize() or word == "laughing\n":
            dict["laughing"] += 1
            continue
print(dict)




