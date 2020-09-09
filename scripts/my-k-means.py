import random

distence = [
[0.0, 13.95, 12.46, 25.03, 17.01, 31.43, 17.23, 25.33, 26.32, 36.44, 33.84, 31.88, 36.97, 29.32, 30.37, 36.61, 38.29, 31.69], 
[13.95, 0.0, 13.04, 32.34, 24.48, 34.38, 24.15, 32.26, 15.78, 23.07, 20.48, 23.16, 23.95, 24.31, 24.25, 34.56, 29.85, 25.98], 
[12.46, 13.04, 0.0, 37.19, 27.31, 42.24, 28.91, 37.71, 26.29, 35.92, 32.75, 31.21, 35.36, 25.77, 20.06, 31.03, 30.74, 20.72], 
[25.03, 32.34, 37.19, 0.0, 15.2, 6.59, 8.75, 0.46, 17.04, 12.29, 18.3, 13.15, 12.12, 13.2, 18.93, 13.86, 9.17, 17.86], 
[17.01, 24.48, 27.31, 15.2, 0.0, 21.7, 7.58, 15.6, 9.2, 22.52, 13.41, 17.43, 18.13, 13.65, 21.64, 21.08, 33.17, 19.79], 
[31.43, 34.38, 42.24, 6.59, 21.7, 0.0, 14.8, 6.49, 17.82, 13.55, 9.59, 23.75, 9.4, 11.73, 21.56, 7.47, 17.98, 21.94], 
[17.23, 24.15, 28.91, 8.75, 7.58, 14.8, 0.0, 8.49, 13.29, 19.4, 11.51, 16.15, 19.18, 18.86, 13.73, 18.88, 19.19, 15.2], 
[25.33, 32.26, 37.71, 0.46, 15.6, 6.49, 8.49, 0.0, 17.46, 12.4, 13.84, 14.32, 10.42, 19.9, 17.36, 14.36, 15.42, 18.05], 
[26.32, 15.78, 26.29, 17.04, 9.2, 17.82, 13.29, 17.46, 0.0, 10.5, 6.5, 8.64, 11.76, 12.96, 12.92, 18.45, 22.76, 10.21], 
[36.44, 23.07, 35.92, 12.29, 22.52, 13.55, 19.4, 12.4, 10.5, 0.0, 8.09, 8.23, 2.67, 10.06, 15.45, 14.13, 5.77, 16.27], 
[33.84, 20.48, 32.75, 18.3, 13.41, 9.59, 11.51, 13.84, 6.5, 8.09, 0.0, 3.11, 7.49, 2.62, 9.87, 12.52, 18.71, 13.26],
[31.88, 23.16, 31.21, 13.15, 17.43, 23.75, 16.15, 14.32, 8.64, 8.23, 3.11, 0.0, 7.71, 6.0, 15.58, 22.72, 7.58, 8.86], 
[36.97, 23.95, 35.36, 12.12, 18.13, 9.4, 19.18, 10.42, 11.76, 2.67, 7.49, 7.71, 0.0, 20.25, 18.81, 8.98, 10.61, 15.15], 
[29.32, 24.31, 25.77, 13.2, 13.65, 11.73, 18.86, 19.9, 12.96, 10.06, 2.62, 6.0, 20.25, 0.0, 6.47, 12.9, 11.83, 5.18], 
[30.37, 24.25, 20.06, 18.93, 21.64, 21.56, 13.73, 17.36, 12.92, 15.45, 9.87, 15.58, 18.81, 6.47, 0.0, 11.04, 12.26, 1.98],
[36.61, 34.56, 31.03, 13.86, 21.08, 7.47, 18.88, 14.36, 18.45, 14.13, 12.52, 22.72, 8.98, 12.9, 11.04, 0.0, 3.25, 11.26], 
[38.29, 29.85, 30.74, 9.17, 33.17, 17.98, 19.19, 15.42, 22.76, 5.77, 18.71, 7.58, 10.61, 11.83, 12.26, 3.25, 0.0, 10.56], 
[31.69, 25.98, 20.72, 17.86, 19.79, 21.94, 15.2, 18.05, 10.21, 16.27, 13.26, 8.86, 15.15, 5.18, 1.98, 11.26, 10.56, 0.0]]

nodes_num = 18

# get 3 random
#centers = [random.randint(0,nodes_num-1) for _ in range(3)]
centers = random.sample(range(0,nodes_num), 3)
print "initial centers = ", centers

# clusters
clusters = [[], [], []]

def get_cluster(node):
    distence0 = distence[centers[0]][node]
    distence1 = distence[centers[1]][node]
    distence2 = distence[centers[2]][node]
    if distence0 < distence1 and distence0 < distence2:
        return 0
    elif distence1 < distence0 and distence1 < distence2:
        return 1
    else:
        return 2

def get_center(cluster):
    min_distences = float('inf')
    ret = cluster[0]

    for i in cluster:
        temp = 0
        # get all distence
        for j in cluster:
            temp += distence[i][j]
        if temp < min_distences:
            ret = i
            min_distences = temp

    return ret

def check_same(new_center0, new_center1, new_center2):
    if new_center0 in centers and new_center1 in centers and new_center2 in centers:
        return True


while True:
    for i in range(nodes_num):
        print "node ", i,
        cluster_id = get_cluster(i)
        print cluster_id
        clusters[cluster_id].append(i)

    print "clusters = ", clusters

    new_center0 = get_center(clusters[0])
    new_center1 = get_center(clusters[1])
    new_center2 = get_center(clusters[2])
    print "new centers = ", new_center0, new_center1, new_center2
    
    if check_same(new_center0, new_center1, new_center2):
        break
    else:
        clusters = [[], [], []]
        centers = [new_center0, new_center1, new_center2]
        
