import cv2
import numpy as np

def redBinary(imgPath):
    # Use a breakpoint in the code line below to debug your script.
    imagen = cv2.imread(imgPath)

    # Convertimos la imagen a espacio de color HSV (Hue, Saturation, Value)
    imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    # Definimos el rango de colores rojos en HSV
    rojo_bajo = np.array([0, 100, 100])
    rojo_alto = np.array([10, 255, 255])

    # Crear una máscara que detecte los colores rojos en el rango especificado
    mascara_rojo1 = cv2.inRange(imagen_hsv, rojo_bajo, rojo_alto)

    # Definimos un segundo rango de colores rojos en HSV
    rojo_bajo = np.array([160, 100, 100])
    rojo_alto = np.array([180, 255, 255])

    # Crear una segunda máscara para el segundo rango de colores rojos
    mascara_rojo2 = cv2.inRange(imagen_hsv, rojo_bajo, rojo_alto)

    # Combinamos las dos máscaras de color rojo
    mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)

    # Binarizamos la imagen original usando la máscara de color rojo
    imagen_binarizada = cv2.bitwise_and(imagen, imagen, mask=mascara_rojo)

    # Mostramos la imagen original y la imagen binarizada
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Binarizada', imagen_binarizada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    redBinary("./Images/test2.jpg")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
