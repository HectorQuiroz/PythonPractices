from urllib.request import urlopen as urequest
story=urequest("http://sixty-north.com/c/t.txt")
story_words=[]
for line in story:
    line_word=line.decode("utf8").split()
    for word in line_word:
        story_words.append(word)

story.close()
print(story_words)