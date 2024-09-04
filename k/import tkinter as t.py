import tkinter as tk
from pydub import AudioSegment
from pydub.playback import play

# Función para cargar sonidos
def load_sounds():
    sounds = []
    for i in range(31):  # Asegúrate de tener 31 archivos de sonido .wav
        try:
            sound = AudioSegment.from_wav(f'sound{i}.wav')
            sounds.append(sound)
        except Exception as e:
            print(f"Error: No se pudo cargar el sonido para sound{i}.wav - {e}")
    return sounds

# Carga inicial de sonidos
sounds = load_sounds()
sounds_per_octave = 10  # Cantidad de sonidos por octava
current_octave = 0

# Función para cambiar el tono de un sonido
def shift_pitch(sound, semitones):
    new_sample_rate = int(sound.frame_rate * (2.0 ** (semitones / 12.0)))
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate}).set_frame_rate(44100)

# Función para reproducir el sonido correspondiente
def play_sound(index):
    global current_octave
    sound_index = current_octave * sounds_per_octave + index
    if sound_index < len(sounds):
        semitones = (current_octave - 2) * 12  # Cambia 12 semitonos por octava
        altered_sound = shift_pitch(sounds[sound_index], semitones)
        play(altered_sound)
    else:
        print(f"Error: Índice de sonido {sound_index} fuera de rango")

# Cambiar la octava
def change_octave(octave):
    global current_octave
    current_octave = octave
    print(f"Octava cambiada a {current_octave + 1}")

# Configuración de la ventana
root = tk.Tk()
root.title("Órgano Musical")

# Crear botones para las teclas
for i in range(sounds_per_octave):
    button = tk.Button(root, text=f'Tecla {i+1}', width=10, height=3, command=lambda i=i: play_sound(i))
    button.grid(row=i // 5, column=i % 5, padx=5, pady=5)

# Crear botones para cambiar de octava
octave_frame = tk.Frame(root)
octave_frame.grid(row=3, columnspan=5, pady=10)

for octave in range(5):  # Ajusta el rango según las octavas que quieras
    octave_button = tk.Button(octave_frame, text=f"Octava {octave+1}", command=lambda o=octave: change_octave(o))
    octave_button.pack(side=tk.LEFT, padx=5)

# Iniciar la interfaz gráfica
root.mainloop()
import os
import tempfile
from pydub import AudioSegment

# Establece un directorio temporal específico
temp_dir = "C:\k\temp"  # Cambia esto a una ruta válida en tu sistema
os.makedirs(temp_dir, exist_ok=True)
tempfile.tempdir = temp_dir

# Resto de tu código...
sound = AudioSegment.from_wav('sound0.wav')
sound = AudioSegment.to_wav('sound31.wav')
