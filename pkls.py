import pickle


with open('data.pkl', 'rb') as f:
    data = pickle.load(f)


print(data[:10])
# lens = [(len(x), x) for x in data]
# print(max(lens))
# for i in range(20):
#     lens.remove(max(lens))
#     print(max(lens))
