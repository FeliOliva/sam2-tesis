import cv2 as cv  # Importa la librería OpenCV para procesamiento de imágenes y video

# Leer una imagen y mostrarla en una ventana
img = cv.imread('Photos/cat.jpg')  # Carga una imagen desde la ruta especificada
cv.imshow('Cat', img)  # Muestra la imagen en una ventana llamada 'Cat'

# Función para redimensionar el tamaño del cuadro de video o imagen
def reescaleFrame(frame, scale=0.75):
    # Calcula nuevas dimensiones según el factor de escala dado
    width = int(frame.shape[1] * scale)  # Ancho escalado
    height = int(frame.shape[0] * scale)  # Alto escalado
    dimensions = (width, height)  # Guarda las dimensiones nuevas en una tupla
    
    # Redimensiona la imagen o cuadro al nuevo tamaño y la devuelve
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Cambia la resolución de la transmisión en vivo de video (cámaras)
def changeRes(width, height):
    # Cambia el ancho y el alto del video capturado
    capture.set(3, width)  # ID 3 es para ancho
    capture.set(4, height)  # ID 4 es para alto

# Leer video desde un archivo y escalar sus cuadros
capture = cv.VideoCapture('Videos/dog.mp4')  # Carga el video desde la ruta especificada

# Bucle para procesar cada cuadro del video
while True:
    # Lee un cuadro del video
    isTrue, frame = capture.read()  # isTrue indica si el cuadro se lee correctamente
    
    # Redimensiona el cuadro leído usando la función de reescalado
    frame_resized = reescaleFrame(frame, scale=0.2)
    
    # Muestra el cuadro original y el redimensionado en ventanas separadas
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    # Si se presiona la tecla 'd', se sale del bucle y cierra las ventanas
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Libera los recursos y cierra las ventanas de video
capture.release()  # Libera el video capturado
cv.destroyAllWindows()  # Cierra todas las ventanas abiertas
