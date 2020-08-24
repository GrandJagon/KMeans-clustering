import numpy as np
import math
import matplotlib.pyplot as plt

np.random.seed(8)

colors = ['green', 'orange', 'yellow', 'blue', 'violet', 'gold', 'chartreuse', 'plum', 'aqua', 'lavender']

class KMeans():
    
    # Constructor taking the dataset, the number of iterations and the number of clusters 
    def __init__(self, data, iterations=10, k=3):
       self.data = data
       self.n = len(data)
       self.k = k
       self.iterations = iterations
    
    # Initializing values and random centroids
    def fit(self):
       self.outputs = {}
       self.temp = {}
       self.centroids = []
       for i in range(self.k):
          rand = np.random.randint(0, len(self.data))
          self.centroids.append(self.data[rand])
          self.temp[i] = []
          self.outputs[i] = []   
          
    
    def iterate(self):
        #  For each data point finds the nearest centroid and stores it in the corresponding entry of the temp dict
        for i in range(self.iterations):
            for n in self.data:
                dist = [math.sqrt((n[0] - centroid[0])**2 + (n[1] - centroid[1])**2) for centroid in self.centroids]
                self.temp[dist.index(min(dist))].append(n)  
                                        
            for index in self.temp.keys():
                mean_dist = np.mean(self.temp[index], axis=0)
                self.centroids[index] = mean_dist
                self.temp[index] = []  
                
        # Once all iterations done stores the data points in the corresponding centroid entry in the final dict
        for n in self.data:
            dist = [math.sqrt((n[0] - centroid[0])**2 + (n[1] - centroid[1])**2) for centroid in self.centroids]
            self.outputs[dist.index(min(dist))].append(n)
 
    
    # Plot the datapoints according to the nearest centroids
    def plot(self):        
        plt.figure(figsize=(8,6))
        plt.title("DATA AFTER CLUSTERING")
        plt.xlabel("Income")
        plt.ylabel("Age")
        
        for i in range(self.k):
            self.outputs[i] = np.array(self.outputs[i])
            plt.scatter(self.outputs[i][:,0], self.outputs[i][:,1], c=colors[i])
            plt.scatter(self.centroids[i][0], self.centroids[i][1], c='red')
            
        plt.show()
        
        
        
        

                

            
        
                

         
        
                
                
                
           
        
        
            
            
    
    
        
                
        
            
            
        
        
    
       
       
        
         
    
    
        
   
    



