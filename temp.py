import pickle
numbers = [1, 2, 3, 4, 5]
with open("numbers.pkl", "wb") as f:
 pickle.dump(numbers, f)