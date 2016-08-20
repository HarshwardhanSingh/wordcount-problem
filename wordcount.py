from re import findall
from collections import Counter


filename = "input2.txt"
content = open(filename, 'r').read()
wordcount = len(content.split())
print "Total word count\n====================\n%d words\n" % wordcount

def percentage(score, total):
    score = float(score)
    return round((score/total)*100,3)

def most_common_words():
    words = findall(r'\w+', content.lower())
    most_common = Counter(words).most_common(10)
    n = 1
    print "Top ten frequent words\n===================="
    for x,y in most_common:
        print "%d: %s => %d (%.2f %%)\n" % (n,x,y,percentage(y,wordcount))
        n += 1

def most_common_word_of_quarter():
    n = 1
    slice_at = wordcount/4
    print "Most common successor of \"the\"\n===================="
    for i in xrange(0, len(content.split()), slice_at):
        a = " ".join(content.split()[i:i+slice_at]) 
        words = findall(r'the\s(\w+)',str(a.split("\n")))
        most_common = Counter(words).most_common(1)
        for a,b in most_common:
            print "Quarter %d => %s\n" % (n,a)
            n += 1
            
most_common_words()
most_common_word_of_quarter()