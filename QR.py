# lo principal es instalar la libreria de qrcode 
# mediante --> pip install qrcode en consola

# importamos la libreria
import tkinter as tk
import qrcode

def generar_codigo():
    # Obtiene el texto del cuadro de entrada
    data = texto.get()

    # Genera el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=25,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Crea una imagen PIL desde el código QR
    imagen = qr.make_image(fill_color="black", back_color="white")

    # Muestra la imagen en la ventana
    imagen.show()

    imagen.save('qr_image.png')

# Crea una ventana
ventana = tk.Tk()
ventana.title("Generador de Códigos QR")
ventana.geometry("200x150")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese el Texto para el código QR:")
etiqueta.pack()

# Cuadro de entrada
texto = tk.Entry(ventana)
texto.pack()

# Botón para generar el código QR
boton_generar = tk.Button(ventana, text="Generar", command=generar_codigo)
boton_generar.pack()

# Ejecuta la aplicación
ventana.mainloop()
