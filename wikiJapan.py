from gensim.models import word2vec
import sys


model = word2vec.Word2Vec.load('wiki.model')
sys.stdout.write("> ")
sys.stdout.flush()
sentence = sys.stdin.readline()
for sp in sentence.split('\n'):
    res = model.most_similar(positive = sp)
    for result in res:
        print(result)
    break
