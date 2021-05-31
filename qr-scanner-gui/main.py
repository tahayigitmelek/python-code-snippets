
from tkinter import Button, Label, Tk, filedialog
from PIL import Image
from pyzbar.pyzbar import decode

class QrOkuyucu:

    def __init__(self, root):
        root.title("Qr Okuyucu")
        root.geometry("400x400")
        root.resizable(width=True, height=True)
        Button(root, text='resmi sec', command=self.resim_ac).pack()
        Button(root, text='yazi temizle', command=self.yazi_temizle).pack()

    def openfilename(self):
        filename = filedialog.askopenfilename(title="resim")
        return filename

    def resim_ac(self):
        global label
        resim_adi = self.openfilename()
        yazi = ""
        for i in decode(Image.open(resim_adi)):
            yazi += str(i.data)[2:-1]
        label = Label(root, text=yazi)
        label.pack()

    def yazi_temizle(self):
        label.pack_forget()

if __name__ == "__main__":
    root = Tk()
    uygulama = QrOkuyucu(root)
    root.mainloop()
