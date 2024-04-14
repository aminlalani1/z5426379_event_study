def freqword(filepath):
    with open(filepath) as file:
        count = dict()
        for line in file:
            words = line.split()
            for word in words:
                count[word] = count.get(word, 0) + 1
        maxword = None
        maxcount = None
        for word, count in count.items():
            if maxcount is None or count > maxcount:
                maxword = word
                maxcount = count
    return (f"The most common word is {maxword}, and its frequency is {maxcount}.")


result = freqword(r"C:/Users/amin9/toolkit/toolkit/iso.txt")
print(result)
