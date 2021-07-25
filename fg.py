from os import path
import math
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from utils import *
from analyze_fp import *
from ipywidgets import interact

def twp_fp_comparison(pic1, pic2):
	fp1 = cv.imread(pic1, cv.IMREAD_GRAYSCALE)
	fp2 = cv.imread(pic2, cv.IMREAD_GRAYSCALE)
	tf1 , tm1, tls1 = analyze_fp(fp1)
	tf2 , tm2, tls2 = analyze_fp(fp2)
	dists = np.sqrt(np.sum((tls1[:,np.newaxis,:] - tls2)**2, -1))
	dists /= (np.sqrt(np.sum(tls1**2, 1))[:,np.newaxis] + np.sqrt(np.sum(tls2**2, 1)))
	num_p = 5 
	pairs = np.unravel_index(np.argpartition(dists, num_p, None)[:num_p], dists.shape)
	score = 1 - np.mean(dists[pairs[0], pairs[1]]) 
	print(f'Comparison score: {score:.2f}')
	if score > 0.75:
		print("Matched!")
	else:
		print("Unmatched!")

#Pass the images to be compared names (if in the same folder) or path
twp_fp_comparison('fg1.jpeg', 'fg3.jpeg')
