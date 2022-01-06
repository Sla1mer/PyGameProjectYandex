import os
import platform
import subprocess
def open_documentation(name):
    path = os.path.join('data', name)
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', path))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(path)
    else:  # linux
        subprocess.call(('xdg-open', path))