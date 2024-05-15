

sentence = "this problem is an easy problem" 
searchWord = "pro"

wordsList = sentence.split()
dummy = 0

for word in wordsList:
    dummy += 1
    if searchWord in word:
        print("Prefix found at index: ", dummy)
        break