from gensim.models import word2vec

model = word2vec.Word2Vec.load('wiki.model')
results = model.most_similar(positive = ['Swift'])

for result in results:
    print(result)


