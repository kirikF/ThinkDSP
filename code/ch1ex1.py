import os
import urllib.request
import matplotlib.pyplot as plt
from thinkdsp import read_wave

# Функция для загрузки файлов
def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} downloaded.")
    else:
        print(f"{filename} already exists.")

# Ссылки на файлы
files = {
    "thinkdsp.py": "https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py",
    "170255__dublie__trumpet.wav": "https://github.com/AllenDowney/ThinkDSP/raw/master/code/170255__dublie__trumpet.wav"
}

# Скачиваем файлы
for filename, url in files.items():
    download_file(url, filename)

# Читаем WAV-файл
wave = read_wave("170255__dublie__trumpet.wav")
wave.normalize()

# Отображаем график сигнала
wave.plot()
plt.title("Waveform of Trumpet Sound")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

