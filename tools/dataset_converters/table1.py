# Import libraries
import numpy as np
import cv2
import json
import pycocotools.mask as mask

# Read the annotations
file_path = "coco/annotations/stuff_annotations_trainval2017/stuff_train2017.json"
with open(file_path, 'r') as f:
    data = json.load(f)

updated_data = []

# For each annotation
for annotation in data['annotations']:

    # Initialize variables
    obj = {}
    segmentation = []
    segmentation_polygons = []

    # Decode the binary mask
    mask_list = mask.decode(annotation['segmentation'])
    mask_list = np.ascontiguousarray(mask_list, dtype=np.uint8)
    mask_new, contours, hierarchy = cv2.findContours(
        (mask_list).astype(np.uint8), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Get the contours
    for contour in contours:
        contour = contour.flatten().tolist()
        segmentation.append(contour)
        if len(contour) > 4:
            segmentation.append(contour)
    if len(segmentation) == 0:
        continue

    # Get the polygons as (x, y) coordinates
    for i, segment in enumerate(segmentation):
        poligon = []
        poligons = []
        for j in range(len(segment)):
            poligon.append(segment[j])
            if (j+1) % 2 == 0:
                poligons.append(poligon)
                poligon = []
        segmentation_polygons.append(poligons)

    # Save the segmentation and polygons for the current annotation
    obj['segmentation'] = segmentation
    obj['segmentation_polygons'] = segmentation_polygons
    updated_data.append(obj)
