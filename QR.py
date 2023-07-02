# lo principal es instalar la libreria de qrcode 
# mediante --> pip install qrcode en consola

# importamos la libreria
import qrcode

# se le pide al usuario su nombre
nombre = input("Digita tu nombre: ")
# se realiza un saludo
print(f"Hola {nombre}")
# se le pide la cadena que desea usar en la convercion
data = input("Digita la cadena para convertir a QR: ")
# con la funcion make(crear) se realiza la conversion de cadena a qr
img = qrcode.make(data)
# por ultimo se guarda la imagen con su respectiva extencion
img.save('qr_image.png')
# se entrega mensaje de confirmacion
print("Revisa la carpeta del proyecto que ya se genero el QR")