from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
import sys
sys.path.append('../sam_model/sam2/training/model')
# sys.path.append('C:/Users/felit/OneDrive/Escritorio/Proyectos/test-cv/sam_model/sam2/training/model')
import sam_model
print(dir(sam_model))  # Para ver qué contiene y confirmar la ruta
# # from sam2 import SAM
# app = FastAPI()
# # model = SAM()  # Carga el modelo SAM2

# @app.post("/segment/")
# async def segment_image(file: UploadFile = File(...)):
#     image_data = await file.read()
#     np_array = np.frombuffer(image_data, np.uint8)
#     frame = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
#     segmented = model.segment(frame)  # Aplica SAM2
#     # Procesa la salida para retornarla en el formato deseado
#     return {"segmentation": segmented.tolist()}
