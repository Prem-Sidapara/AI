

import numpy as np

py_list = [1,2,3,4,5]

np_array = np.array([1,2,3,4,5])


print(type(py_list))
print(type(np_array))


print(np_array * 2 )
print(np_array + 10 )
print(np_array ** 2 )

result = [x * 2 for x in py_list]
print(result)




import time

big_list = list(range(1_000_000))
big_array = np.array(big_list)

start = time.time()
result = [ x*2 for x in big_list]
print(f"List time: {time.time() - start:.4f} seconds")

start = time.time()
result = big_array * 2
print(f"Numpy Array time: {time.time() - start:.4f} seconds")




# Embeddings 

word_cat  = np.array([0.9, 0.1, 0.8])   # "cat" ka vector
word_dog  = np.array([0.8, 0.2, 0.7])   # "dog" ka vector  
word_car  = np.array([0.1, 0.9, 0.1])   # "car" ka vector

# Dot product similarity 

cat_dog_similarity = np.dot(word_cat, word_dog)
cat_car_similarity = np.dot(word_cat, word_car)

print(f" Cat - dog: {cat_dog_similarity:.2f}")
print(f" Cat - Car: {cat_car_similarity:.2f}")

def cosine_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(f"Cosine cat-dog: {cosine_similarity(word_cat, word_dog)}")
print(f"Cosine cat-car: {cosine_similarity(word_cat, word_car)}")








# find most similar word

vocabulary = {
    "cat": np.array([0.9, 0.1, 0.8]),
    "dog":   np.array([0.8, 0.2, 0.7]),
    "car":   np.array([0.1, 0.9, 0.1]),
    "truck": np.array([0.2, 0.8, 0.15]),
    "fish":  np.array([0.7, 0.1, 0.6]),
}

def find_most_similar(query_vector, vocab):
    scores = {}
    for word , vector in vocab.items():
        scores[word] = cosine_similarity(query_vector,vector)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

kitten = np.array([0.85, 0.1, 0.75])
results = find_most_similar(kitten, vocabulary)

print("\nMost similar to 'kitten':")
for word , score in results:
    print(f" {word}: {score:.3f}")

# i wrote embeddings by myself so obv cat and fish comed closer to kitten and dog is in the third place 
