import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import uniform

number_of_cities=int(input("enter the number of cities - "))
cities=[]
pheromoneij=[]
pheromone_quantity=0.2
inv_distance_matrix=[]
pheromone_quantity_new=[]
path_by_cities=[]
distance_matrix=[]
a=[]
b=[]
for i in range(number_of_cities):
    cities.append(i+1)
for i in range(number_of_cities):
    temp_distance_store=[]
    temp_pheromoneij_store=[]
    temp_inv_distance_store=[]
    for j in range(number_of_cities):
        if(i!=j):
            temp_pheromoneij_store.append(pheromone_quantity)
            dist=float(input("enter the distance from city "+(str)(i+1)+" to "+str(j+1)+" - "))
            temp_distance_store.append(dist)
            temp_inv_distance_store.append(round(1/dist,3))
            b.append(0.0)
        else:
            temp_pheromoneij_store.append(0.0)
            temp_distance_store.append(0.0)
            temp_inv_distance_store.append(0.0)
            b.append(0.0)
    
    distance_matrix.append(temp_distance_store)
    inv_distance_matrix.append(temp_inv_distance_store)
    pheromoneij.append(temp_pheromoneij_store)
    a.append(b)
print(distance_matrix,pheromoneij,inv_distance_matrix)
for t in range(number_of_cities):
    for city in range(number_of_cities):
        path=[]
        visited_node=[]
        path.append(city+1)
        i=city
        for count in range(number_of_cities-1): 
            visited_node.append(i)
            product_of_phero_invdist=[]
            track_city={}
            track_probability={}
            sum_of_product=0.0
            probability=[]
            for j in range(number_of_cities): 
                temp_track_city=[]
                if(j not in visited_node):
                    t=pheromoneij[i][j]*(inv_distance_matrix[i][j]**2)
                    product_of_phero_invdist.append(t)
                    track_city[t]=j+1
                    sum_of_product=sum_of_product+t
            for j in range(len(product_of_phero_invdist)):
                    probability.append(product_of_phero_invdist[j]/sum_of_product)
                    track_probability[product_of_phero_invdist[j]/sum_of_product]=product_of_phero_invdist[j]
            probability.sort()
            i=track_city[track_probability[probability[len(probability)-1]]]-1
            path.append(i+1)
        path.append(city+1)
        path_by_cities.append(path)
        print(path)
        sum_path_dist=0.0
        for j in range(len(path)-1):
            sum_path_dist=sum_path_dist+distance_matrix[path[j]-1][path[j+1]-1]
        pheromone_quantity_new.append(1/sum_path_dist)
        print(sum_path_dist)
    for i in range(len(path_by_cities)):
        for j in range(number_of_cities):
            for k in range(number_of_cities):
                if j==path_by_cities[i][j]-1 and k==path_by_cities[i][j+1]-1:
                    a[j][k]=a[j][k]+pheromone_quantity_new[i]
                else:
                    a[j][k]=a[j][k]+0.0
                    #pheromoneij[j][k]=((1-0.5)*pheromoneij[j][k])
    for j in range(number_of_cities):
        for k in range(number_of_cities):
            if(j!=k):
                pheromoneij[j][k]=((1-0.5)*pheromoneij[j][k])+a[j][k]
        #pheromoneij[path_by_cities[i][j]-1][path_by_cities[i][j+1]-1]=((1-0.5)*pheromoneij[path_by_cities[i][j]-1][path_by_cities[i][j+1]-1])+pheromone_quantity_new[i]      
            
            



