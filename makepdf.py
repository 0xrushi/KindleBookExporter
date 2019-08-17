import img2pdf
import os
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir('./') if i.endswith(".jpg")]))