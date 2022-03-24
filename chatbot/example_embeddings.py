import numpy as np

list1 =np.array([[ 4, 45,  8,  4],
       [ 2, 23,  6,  4]])

list2=np.array([ 2, 54, 13, 15])

similarity_scores = list1.dot(list2)/ (np.linalg.norm(list1, axis=1) * np.linalg.norm(list2))

print(similarity_scores)
