from PIL import Image, ImageDraw
import math
import timeit

proby = int(input("Ilosc prob: "))
isSave = input("Czy chcesz zapisać obrazek? [Y/n] ")
size = 3**(proby)
print("")
print("")
start_Time = timeit.default_timer()

im = Image.new("RGB", (size, size), color=(0,0,0))
draw = ImageDraw.Draw(im)
proggres = 0

pos = [0,0]

def drawPixel():
	draw.point((pos[0],pos[1]), fill=(255,255,255))

def nextIteration(t, x, y, step):
	for x2 in range (x + step, x + step + step):
		for y2 in range (y + step, y + step + step):
			t[x2][y2] = 'w'
			
	if step != 1:
        #top row
		nextIteration(t, x, y, step // 3)
		nextIteration(t, step + x, y, step // 3)
		nextIteration(t, step * 2 + x, y, step // 3)
		#mid row
		nextIteration(t, x, step + y, step // 3)
		nextIteration(t, step * 2 + x, step + y, step // 3)
		#bottom row
		nextIteration(t, x, step * 2 + y, step // 3)
		nextIteration(t, step + x, step * 2 + y, step // 3)
		nextIteration(t, step * 2 + x, step * 2 + y, step // 3)


def prepareKwadrat(size):
	step = 3 ** (size - 1) 
	maxSize = step * 3
	t = []
	for k in range(maxSize):		#tworzenie mapy
		t.append(["b"]*maxSize)     # Wszystko jest białe
		
	for x in range(step, step + step):
		for y in range(step, step + step):
			t[x][y] = 'w'
		
    #top row
	nextIteration(t, 0, 0, step // 3)
	nextIteration(t, step, 0, step // 3)
	nextIteration(t, step * 2, 0, step // 3)
    #mid row
	nextIteration(t, 0, step, step // 3)
	nextIteration(t, step * 2, step, step // 3)
    #bottom row
	nextIteration(t, 0, step * 2, step // 3)
	nextIteration(t, step, step * 2, step // 3)
	nextIteration(t, step * 2, step * 2, step // 3)
    
	return t

print("Wielkość dywanu: ",size,"x",size)
print("Generowanie mapy [...]",end="\r")
t = prepareKwadrat(proby)
print("Generowanie mapy [ GOTOWE ]")
print("")


for x in range(3**(proby)):
	for y in range(3**(proby)):
		if (t[x][y] == "w"):
			drawPixel()
		pos[0]= pos[0]+1
	proggres = proggres+1
	print("POSTĘP: ","%.1f" %(proggres/(size)*100),"%",end="\r")
	pos[0] = 0
	pos[1] = pos[1] + 1
	
stop_Time = timeit.default_timer()
print("Wyrenderowano dywan w ciągu:", "%.1f" %(stop_Time-start_Time),"sekund")

if isSave.upper() == "Y":
	im.save("dywanSierpinskiego("+str(proby)+").jpg")

im.show()


