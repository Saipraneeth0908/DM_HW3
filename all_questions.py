# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since agglomerative hierarchical clustering creates clusters based on distance and local structure metrics, which can naturally segregate outliers, it is more resilient to outliers than k-means. On the other hand, because outliers have the ability to dramatically affect centroids' positions, k-means is susceptible to them."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Agglomerative hierarchical clustering methods follow a deterministic process of merging clusters based on a distance requirement, therefore they will always provide the same clustering for a given dataset. On the other hand, because centroids are randomly initialized, k-means clustering may result in distinct clusterings on various runs."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Because of its more straightforward iterative refinement approach, k-means clustering is typically faster and consumes less memory than agglomerative hierarchical clustering; yet, it is not the most efficient clustering algorithm available. The dataset and environment can affect efficiency, and different clustering techniques may perform better in particular situations."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Because splitting results in two centroids for a given set of points, the distance between the points and the closest centroid is shortened, lowering the SSE."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "A decrease in the sum of squared distances (SSE) between a point and its centroid in k-means clustering implies that points are closer to their centroids, which increases cohesion within clusters."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "In k-means clustering, a rise in the between sum of squares (SSB) denotes a greater separation between the clusters as they get farther away from one another."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "For K-Means, separation and cohesion are independent; that is, increasing separation (greater between sum of squares (SSB)) does not always equate to increasing cohesion (smaller SSE)."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "The total sum of squares (TSS) for K-means is equal to the sum of the between sum of squares (SSB) and the within cluster sum of squares (SSE). TSS remains constant during the K-means clustering procedure."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "The total sum of squares (TSS) for K-means is equal to the sum of the between sum of squares (SSB) and the within cluster sum of squares (SSE).Whereas SSB is a direct indicator of cluster separation, SSE is an inverse indicator of cluster cohesion. Because TSS = SSE + SSB is a constant, when cohesiveness rises, SSE falls and SSB (separation) rises. BSS reaches a local maxima when SSE reaches a local minima."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "As the clusters are very far from each other htey cant alter and will remain in the same respective clusters but will be reasigned to the mean of their respective cluster."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Since the two darkened sections are not circular in shape and are instead near to one another, the final clusters will contain points from each of them."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid at 12.5 will eventually become empty because it is the furthest from all points compared to any other cluster."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R^2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*(a^2+b^2+R^2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10*R^2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "As the density of c is more with 100000 points in it the cluster C will be grouped with a centroid in it and clusters A and B with same density will have one centroind in each of them."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The centroid located in circle A will receive the points from both circles A and B because they are relatively close to one other and far from circle C. The two centroids in C will split the points in C, with 50,000 points each centroid.  Due to the fact that A and B have equal amounts of points, the centroid in A will shift between the two. Each of the centroids in C will retain half of the points in C despite their modest separation."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "since the distance between B and C is more the 2 centroids in C will remain in C saperating the cluster into two parts and the one centroid in A will move towards the cluster B and ends up exaxtly between A and B as the density of A and B are same with 100 points each."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}


    # type: set
    answers["(a)"] = {'Group A','Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B will be merged since they have the smallest single link distance (betweenright-most point of A and left-most point of B), as compared to Groups A and C, and Groups Band C."

    # type: set
    answers["(b)"] = {'Group A','Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ": Groups A and C will be merged since they have the smallest complete link distance (between aboundary point of A and the farthest point in C), as compared to the complete link distance of Groups A and B (between the left-most point in A and right-most point in B), and Groups B and C (between right-most-point in B and the farthest point in C)."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B','C','E','F','I','J','L','M'}

    # type: set
    answers["(a) boundary"] = {'D','G'}

    # type: set
    answers["(a) noise"] = {'A','H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','D','E','F','G'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B','C','E','F','I','J','L','M','D','G'}

    # type: set
    answers["(c)-a boundary"] = {'A','H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'G', 'I', 'H', 'A', 'J', 'E', 'M', 'B', 'D', 'F', 'L', 'C'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "after caluculating the entropies for all the cluster we can see that entropy for the cluster 4 is highest with value of 2.2615165224362351 and also it is considered to me more random"

    # type: string
    answers["(b)"] = "cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "after caluculating the entropies for all the cluster we can see that entropy for the cluster 1 is least with value of 0.0486847908152747916 and also it is considered to me less random"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Two diagonal squares display a deeper blue and a sharper boundary, signaling stronger internal unity for clusters B and C, in contrast to the less cohesive clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Rows 1 and 3, representing clusters A and C, have distinctively colored off-diagonal squares, illustrating the unique distances from these clusters to the others: Cluster A is nearest to C, next to B, and farthest from D, with a similar pattern for cluster C. Row 2, for cluster B, shows equal distance to clusters A and C with the greatest distance from D. Row 4, for cluster D, indicates equal distance to clusters A and C, with the most distance from B."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Two diagonal squares, indicative of clusters B and C, are highlighted with a bold blue and distinct edges, pointing to higher cluster integrity than the other two clusters, A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows with less defined diagonal entries (1 and 4) show a spectrum of colors in off-diagonal squares, denoting varied distances to other clusters, with no two clusters at the same distance from A and D. Rows with clearer diagonal entries demonstrate two identical off-diagonal colors, meaning equal proximity to two clusters and maximum distance from the third one."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Clusters B and C are denoted by two diagonals that are more vividly blue and well-defined, signifying stronger cohesion in comparison to the more indistinct clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Each row contains two off-diagonal squares of matching colors and one of a different hue, suggesting that each cluster has two other clusters at a relatively similar distance and one that is notably further away."


    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "The central square is not very defined, suggesting that this cluster is not very tight-knit. The varying colors in the non-diagonal squares indicate differing levels of distance to other clusters, with the closest being cluster B, followed by C, and the most distant is cluster A."
    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The central square is sharply defined, which shows a high degree of internal cluster unity. Two out of the three non-diagonal squares share a color, suggesting that this cluster is equidistant from clusters A and C, despite the connection with A being slightly less distinct, and it's most distant from cluster D."
    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = " the elements within the cluster are closely related to each other. For the non-central squares, two have the same hue, indicating that this cluster is at a similar distance from two other clusters (A and C), with the connection to A being somewhat blurrier. It is most distant from cluster D, which is implied by a distinctively different color in the corresponding non-diagonal square."
    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The explanation for this row mirrors that of row 1 but with the cluster relationships reversed in terms of distance. The less distinct central square suggests that this cluster is relatively dispersed, indicating less internal cohesion. The non-diagonal squares show varied colors, which means varying distances to the other clusters. In this inverted relationship, the cluster is closest to cluster C, then B, with the greatest distance from cluster A, as indicated by the non-diagonal square colors. This is the opposite of what was described in row 1, where the cluster was closest to B and furthest from A."
    return answers

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(b)"] = ['Partitional', 'exclusive', 'complete']

    # type: list
    answers["(c)"] = ['Partitional', 'exclusive', 'complete']

    # type: list
    answers["(d)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Because each student only receives one mark in a class, the discrete letter grades are used to categorize students. This method is known as partitional clustering. Because a student cannot have more than one grade for the same class, it is exclusive. The fact that each student in the class will receive a grade makes up the entire element."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "no"

    # type: string
    answers["(a) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN can work only for (b) because in (b) the points in the nose,  eyes, and mouth are much closer together than the points between  these areas, and DBSCAN could distinguish these areas. For (a),  the noise is much denser than the interest patterns, so the nose,  eyes, and mouth will be eliminated by DBSCAN."


    # type: string
    answers["(b) Figure (a)"] = "no"

    # type: string
    answers["(b) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means can work for (b) as long as the number of clusters  was set to 4, although the lower density points would also  be included. K-means does not work for (a)."

    # type: string
    answers["(c)"] = "Take the reciprocal of the density as the new density and use DBSCAN."
    return answers

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
