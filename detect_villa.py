import cv2
import pytesseract
import numpy as np


def detect_villa(frame):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    morphological_img = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)
    canny_img = cv2.Canny(morphological_img, 200, 300)
    contours, _ = cv2.findContours(
        canny_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.015 * peri, True)
        if len(approx) == 4 and area > 5000:
            x, y, w, h = cv2.boundingRect(approx)

            if w > h:
                ROI = frame[y:y + h, x:x + w]
                cv2.imwrite('ROI.png', ROI)
                if text is not None:
                    print(text)
                text = pytesseract.image_to_string(ROI)
                # for key, value in array.items():
                #     if text.upper().strip() == array[key].upper():
                #         if (text != None):
                #             print(text)

