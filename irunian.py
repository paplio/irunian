from PIL import Image

irumsg = raw_input("Enter super duper secret message: ") 

imglist = []

for letter in irumsg:
	if letter != ' ':
		imglist.append(str('po/'+letter+'.png'))

images = [Image.open(x) for x in imglist]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('scripts/iru.png')
