import os
import subprocess

path = "pdfimgs"
if not os.path.exists(path):
	os.mkdir(path)

pdfs = os.listdir("pdfs")
for pdf in pdfs:
	args = ["python",
	"pdf2img.py",
	"pdfs/"+pdf,
	path+"/"+pdf[:pdf.index(".")]+".png"
	]
	subprocess.call(args)

