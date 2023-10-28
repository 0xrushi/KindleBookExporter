import img2pdf
import os

jpg_files = [i for i in os.listdir('./') if i.endswith(".jpg")]

# Sort the list in serial order by numeric value
jpg_files.sort(key=lambda x: int(x.split('.')[0]))

# print(jpg_files)
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(jpg_files))
