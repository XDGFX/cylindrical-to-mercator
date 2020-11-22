#!/usr/bin/env python3
"""
mercator_stretcher.py

Convert cylindrical projections to mercator projections

XDGFX, 2020
"""

import cv2
import numpy as np

# --- Variables
source_file = "GRAY_HR_SR_W.tif"
target_file = "GRAY_HR_SR_W_STRETCH.tif"

index = 2
multiplier = 2

# --- Main Script
X = cv2.imread(source_file)

if X is None:
    raise Exception("File not found!")

# Split into top and bottom
X_top = X[0:X.shape[0]//2, :]
X_bottom = X[X.shape[0]//2:, :]

# Flip bottom image
X_bottom = cv2.flip(X_bottom, 0)

# Initialise parameters
scale = X_top.shape[0]
width = X_top.shape[1]

input_array = np.linspace(0, 1, scale * multiplier)
output_array = np.multiply(multiplier, np.power(input_array, index))

i = range(0, round(scale * multiplier) - 1)

input_values = np.round(np.multiply(scale, np.divide(output_array[i], multiplier))).astype(int)

# Output matrix
X_top_out = X_top[input_values, :]
X_bottom_out = X_bottom[input_values, :]

# Flip bottom image back
X_bottom_out = cv2.flip(X_bottom_out, 0)

X_out = np.append(X_top_out, X_bottom_out, 0)

cv2.imwrite(target_file, X_out)
