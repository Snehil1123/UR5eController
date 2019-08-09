import urx
import keyboard
from inputs import get_gamepad

a = 0.3
v = 0.3

x = -0.13946
y =  -0.43113
z = 0.35938

incr = 0.05

rob = urx.Robot("10.0.2.15")

print("Moving to start")

rob.movep((x, y, z, 0, -3.14, 0.0), a, v)

print("start control")

while True:

	events = get_gamepad()

	for event in events:

		if event.code == "ABS_Y":
	
			z += (event.state * (-1 / 8000) + (128 / 8000))
	
			print("")
	
			print(z)
	
			rob.movep((x, y, z, 0, -3.14, 0.0), a, v)
	
		if event.code == "ABS_Z":
	
			y += (event.state * (1 / 8000) - (128 / 8000))
	
			print("")
	
			print(y)
	
			rob.movep((x, y, z, 0, -3.14, 0.0), a, v)
	
		if event.code == "ABS_RZ":
	
			x += (event.state * (1 / 8000) - (128 / 8000))
	
			print("")
	
			print(x)
	
			rob.movep((x, y, z, 0, -3.14, 0.0), a, v)
