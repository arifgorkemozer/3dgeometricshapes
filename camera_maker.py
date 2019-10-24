
# author: Gorkem Ozer
# more info: https://github.com/arifgorkemozer/3dgeometricshapes/

with open("cameras.xml", 'w') as out_file:

	out_file.write('<Cameras>\n')
	out_file.write('	<Camera id="1">\n')
	out_file.write('		<Position>0 0 100</Position>\n')
	out_file.write('		<Gaze>0 0 -1</Gaze>\n')
	out_file.write('		<Up>0 1 0</Up>\n')
	out_file.write('		<ImagePlane>-1 1 -1 1 2 1000 1000 1000</ImagePlane>\n')
	out_file.write('		<OutputName>camera_front.ppm</OutputName>\n')
	out_file.write('	</Camera>\n')
	out_file.write('	<Camera id="2">\n')
	out_file.write('		<Position>0 100 0</Position>\n')
	out_file.write('		<Gaze>0 -1 0</Gaze>\n')
	out_file.write('		<Up>0 0 -1</Up>\n')
	out_file.write('		<ImagePlane>-1 1 -1 1 2 1000 1000 1000</ImagePlane>\n')
	out_file.write('		<OutputName>camera_top.ppm</OutputName>\n')
	out_file.write('	</Camera>\n')
	out_file.write('</Cameras>\n')