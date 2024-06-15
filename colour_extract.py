import cv2
import numpy as np
from sklearn.cluster import KMeans

def do(pic, k=4):
    # to array
    img = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    img = img.reshape((-1,3))

    # clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(img)

    # extraction
    colours = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_
    counts = np.bincount(labels)

    # colour sorting
    sorted = np.argsort(counts)[::-1]
    dom_colours = colours[sorted]

    return dom_colours