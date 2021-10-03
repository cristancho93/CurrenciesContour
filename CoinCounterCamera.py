import cv2
import numpy

def orderPoints(points):
    n_points = numpy.concatenate(points[0], points[1], points[2], points[3]).tolist()
    y_order = sorted(n_points, key= lambda n_points: n_points[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

def aling(image, width, high):
    image_aling = None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresholdType, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("threshold", threshold)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
    contours = sorted(contours, key=cv2.countourArea, reverse=True)[:1]

    for c in contours:
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        if len(approx) == 4:
            points = orderPoints(approx)
            pointS1 = numpy.float32(points)
            pointS2 = numpy.float32([[0, 0], [width, 0], [0, high], [width, high]])
            M = cv2.getPerspectiveTransform(pointS1, pointS2)
            image_aling = cv2.warpPerspective(image, M, (width, high))