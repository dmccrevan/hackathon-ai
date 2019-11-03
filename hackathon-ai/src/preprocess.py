import pickle

data = pickle.load(open("data.pickle", "rb"))

print(len(data))

titles = [element[0] for element in data]
taglines = [element[1] for element in data]

print(len(titles))
print(len(taglines))

pickle.dump(titles, open('titles.pickle', 'wb'))
pickle.dump(taglines, open('taglines.pickle', 'wb'))

