import tkinter as tk
import pygame

# Inicializa pygame para el manejo de sonidos
pygame.init()
pygame.mixer.init()

# Cargar sonidos (asegúrate de tener archivos de sonido .wav en el directorio)
def load_sounds():
    sounds = []
    for i in range(31):
        sound = pygame.mixer.Sound(f'sound{i}.wav')
        sounds.append(sound)
    return sounds

sounds = load_sounds()

def play_sound(index):
    sounds[index].play()

# Configuración de la ventana
root = tk.Tk()
root.title("Teclado de 31 Teclas")

# Crear botones para el teclado
for i in range(31):
    button = tk.Button(root, text=f'Tecla {i+1}', command=lambda i=i: play_sound(i))
    button.grid(row=i // 5, column=i % 5, padx=5, pady=5)

# Iniciar la interfaz gráfica
root.mainloop()
