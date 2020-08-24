import numpy as np
import matplotlib.pyplot as plt


# Function responsible for creating N fake data points (income/age) within k clusters
def create_cluster_data(N, k):
    np.random.seed(10)
    
    points_per_cluster = N / k
    X = []
    
    for i in range(k):
        income_centroid = np.random.uniform(20000, 500000)
        age_centroid = np.random.uniform(20, 80)
        
        for j in range(int(points_per_cluster)):
            X.append([np.random.normal(income_centroid, 50000), np.random.normal(age_centroid, 7)])
        
    X = np.array(X)
    
    plt.figure(figsize=(8,6))
    plt.title("DATA BEFORE CLUSTERING")
    plt.xlabel('Income')
    plt.ylabel('Age')
    plt.scatter(X[:,0], X[:,1])
    plt.show()
        
    return X
    
    
    
    
    




        