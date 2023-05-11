from pyexpat import features
import cv2
import labels as labels
from torch import threshold

img = cv2.imread('./download.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(gray, (100, 100))

sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(img, None)

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

model = SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)
logo_present = model.predict_proba('./download.jpg')[:, 1] > threshold
