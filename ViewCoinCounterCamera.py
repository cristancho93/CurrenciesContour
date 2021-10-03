import cv2 as cv

captureVideo = cv.VideoCapture(0)
if not captureVideo.isOpened():
    print("No se encontro una camara")
    exit()

while True:
    tipoCamara, frame = captureVideo.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Vivo", gray)
    if cv.waitKey(1) == ord("q"):
        break

captureVideo.release()
cv.destroyAllWindows()