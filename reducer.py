import sys

word2count={}

for line in sys.stdin:
    line=line.strip()
    word , count=line.split('\t',1)
    try:
        count=int(count)
    except ValueError:
        continue;
    try:
        word2count[word]=word2count[word]+count
    except:
        word2count[word]=count


for word in word2count.keys():
    print(f'{word}\t{word2count[word]}')
    