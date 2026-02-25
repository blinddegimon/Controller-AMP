from PySide6.QtCore import QIODeviceBase, Slot, QByteArray

from mainwindow import AppConfig, QCheckBox, QLineEdit

def to_b16t(i):
    r = bytearray()
    for e in i:
        r += e.to_bytes(2,'big')
    return r

b = QByteArray(to_b16t([0x7a7b,0x1,12345,0x1]))


string = "CM"
print(ord("R"))



def v_type(value):
    match value:
        case int():
            print("u passed int")
        case str():
            print("u passed str")
        case _:
            print("u passed something else: " + str(type(value)))

v_type("s")


