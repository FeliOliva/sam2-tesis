import cv2 as cv

# Iniciar captura desde DroidCam o EpocCam (usualmente índice 1 o una URL)
capture = cv.VideoCapture(1)  # o usa la URL de la app, como 'http://<IP>:4747/mjpegfeed'

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    # Aquí podrías pasar el frame a SAM2 después de procesarlo
    cv.imshow('Live Feed', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
