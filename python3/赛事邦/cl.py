from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
for i in range(10):
    m.click(808 - 200+50, 585 - 110, 1)