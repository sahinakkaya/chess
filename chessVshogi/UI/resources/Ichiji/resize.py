from PIL import Image
import glob

files = glob.glob("*.png")

for file in files:
	print(file)
	img = Image.open(file)
	out = img.resize((43,48), Image.BILINEAR)
	out.save("./resize/"+file)