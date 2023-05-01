Currently, these screen captures are attempting to detect humans and automotive vehicles on a frame per frame basis. Obviously, false positives are common in this shortlist of images. 

haarcascade appears to be an OK classifier, but needs help. I am hoping that motion tracking algorithms or heuristics can filter out still false positives.

Challenges:
- poor lighting: cars in the shadows do not get recognized by the haarcascade models. particularly in the morning.
- car color bias: white vehicles are captured more often than other vehicles.
- false positives: the foliage in this shot is particularly difficult to parse for the haarcascade models.