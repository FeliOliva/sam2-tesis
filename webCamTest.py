import cv2 as cv
import requests
import numpy as np

# Inicia la captura desde DroidCam
capture = cv.VideoCapture(1)  # Índice o URL

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    # Codifica el frame como imagen JPEG para enviarla al servidor
    _, img_encoded = cv.imencode('.jpg', frame)
    response = requests.post(
        "http://127.0.0.1:8000/segment/",
        files={"file": img_encoded.tobytes()}
    )

    # Procesa la respuesta de segmentación si está disponible
    if response.status_code == 200:
        segmentation = np.array(response.json()["segmentation"])
        cv.imshow('Segmented Feed', segmentation)

    # Cierra con 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
