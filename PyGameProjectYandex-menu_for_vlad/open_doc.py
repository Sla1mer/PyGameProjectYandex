import os
import platform
import subprocess
# Функция открывает текстовый док(использую для открытия правил игры в разделе помощь)
# В функции подписано как на какую платформу открывать файлы

def open_documentation(name):
    path = os.path.join('data', name)
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', path))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(path)
    else:  # linux
        subprocess.call(('xdg-open', path))