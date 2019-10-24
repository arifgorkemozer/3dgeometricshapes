
# author: Gorkem Ozer
# more info: https://github.com/arifgorkemozer/3dgeometricshapes/


import sys

if len(sys.argv) < 8:
	print 'Usage: python box_maker.py <start_x>\n\t\t\t<start_y>\n\t\t\t<start_z>\n\t\t\t<length>\n\t\t\t<width>\n\t\t\t<height>\n\t\t\t<last_vertex_id_3d_space>'

else:
	
	start_x = (float)(sys.argv[1])
	start_y = (float)(sys.argv[2])
	start_z = (float)(sys.argv[3])

	length = (float) (sys.argv[4])
	width = (float) (sys.argv[5])
	height = (float) (sys.argv[6])
	last_vertex_id = (int) (sys.argv[7])

	color_red = (255, 0, 0)
	color_green = (0, 255, 0)
	color_blue = (0, 0, 255)
	color_cyan = (0, 255, 255)

	points = [] 	# contains vertex positions
	colors = []		# contains vertex colors
	triangles = []	# contains triangles, each represented with 3 vertex ids

	# 1st vertex position
	first = (start_x, start_y, start_z)
	points.append( first )
	colors.append( color_red )

	#2nd vertex position
	points.append( (first[0] , first[1] - height , first[2]) )
	colors.append( color_red )

	#3rd vertex position
	points.append( (first[0] + length , first[1] - height , first[2]) )
	colors.append( color_green )

	#4th vertex position
	points.append( (first[0] + length , first[1] , first[2]) )
	colors.append( color_green )

	#5th vertex position
	points.append( (first[0] + length , first[1] - height , first[2] - width) )
	colors.append( color_blue )

	#6th vertex position
	points.append( (first[0] + length , first[1] , first[2] - width) )
	colors.append( color_blue )
	
	#7th vertex position
	points.append( (first[0] , first[1] , first[2] - width) )
	colors.append( color_cyan )

	#8th vertex position
	points.append( (first[0] , first[1] - height , first[2] - width) )
	colors.append( color_cyan )

	"""
		Triangles should be:

		Front: 1-2-3, 1-3-4
		Bottom: 8-3-2, 5-3-8
		Right Side: 4-3-5, 4-5-6
		Back: 6-5-8, 6-8-7
		Top: 7-1-4, 7-4-6
		Left Side: 7-2-1, 7-8-2
	"""

	# front
	triangles.append( (1 + last_vertex_id , 2 + last_vertex_id, 3 + last_vertex_id ) )
	triangles.append( (1 + last_vertex_id , 3 + last_vertex_id, 4 + last_vertex_id ) )
	
	# bottom
	triangles.append( (8 + last_vertex_id , 3 + last_vertex_id, 2 + last_vertex_id ) )
	triangles.append( (5 + last_vertex_id , 3 + last_vertex_id, 8 + last_vertex_id ) )
	
	# right side
	triangles.append( (4 + last_vertex_id , 3 + last_vertex_id, 5 + last_vertex_id ) )
	triangles.append( (4 + last_vertex_id , 5 + last_vertex_id, 6 + last_vertex_id ) )
	
	# back
	triangles.append( (6 + last_vertex_id , 5 + last_vertex_id, 8 + last_vertex_id ) )
	triangles.append( (6 + last_vertex_id , 8 + last_vertex_id, 7 + last_vertex_id ) )
	
	# top
	triangles.append( (7 + last_vertex_id , 1 + last_vertex_id, 4 + last_vertex_id ) )
	triangles.append( (7 + last_vertex_id , 4 + last_vertex_id, 6 + last_vertex_id ) )

	# left side
	triangles.append( (7 + last_vertex_id , 2 + last_vertex_id, 1 + last_vertex_id ) )
	triangles.append( (7 + last_vertex_id , 8 + last_vertex_id, 2 + last_vertex_id ) )

		
	with open('box_scene.xml', 'w') as out_file:

		

		out_file.write('<Vertices count="%d">\n' % len(points))

		for i in range(0, len(points)):
			out_file.write( '	<Vertex id="%d" position="%s" color="%s" />\n' % (i+1, " ".join([str(elem) for elem in points[i]]), " ".join([str(elem) for elem in colors[i]]))  )

		out_file.write("</Vertices>\n")

		out_file.write('<Models count="1">\n')
		out_file.write('	<Model id="1" type="1">\n')

		out_file.write('		<Transformations count="0"></Transformations>\n')
		out_file.write('		<Triangles count="%d">\n' % len(triangles))

		for i in range(0, len(triangles)):
			out_file.write( '			<Triangle id="%d">%s</Triangle>\n' % (i+1, " ".join([str(vertexId) for vertexId in triangles[i]]))  )

		out_file.write("		</Triangles>\n")
		

		out_file.write("	</Model>\n")
		out_file.write("</Models>\n")
		
		
		
		
		
		
		
