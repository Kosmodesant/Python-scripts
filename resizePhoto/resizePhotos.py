from PIL import Image
im = Image.open("example.jpg")
new_im = im.resize((640, 480))
new_im.save("example_resized.jpg")

# from PIL import Image
# im = Image.open("example.jpg")
# new_im = im.rotate(90)
# new_im.save("example_rotated.jpg")

# from PIL import Image
# im = Image.open("example.jpg")
# im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

# import os
# import glob
# from PIL import Image
# for x in glob.glob("ic*"):
# 	mod_image = Image.open(x).convert("RGB")
# 	mod_image.rotate(270).resize((128,128)).save("/opt/icons/" + x,"jpg")
