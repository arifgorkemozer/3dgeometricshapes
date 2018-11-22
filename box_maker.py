
# author: Gorkem Ozer

import sys

if len(sys.argv) < 8:
	print "Usage: python box_maker.py <start_x>\n\t\t\t<start_y>\n\t\t\t<start_z>\n\t\t\t<length>\n\t\t\t<width>\n\t\t\t<height>\n\t\t\t<last_vertex_id_3d_space>"

else:
	
	x1 = (float)(sys.argv[1])
	y1 = (float)(sys.argv[2])
	z1 = (float)(sys.argv[3])

	l = (int) (sys.argv[4])
	w = (int) (sys.argv[5])
	h = (int) (sys.argv[6])
	base = (int) (sys.argv[7])


	first = (x1, y1, z1)
	points = [first]

	#2nd
	points.append( (first[0] , first[1] - h , first[2])  )

	#3rd
	points.append( (first[0]+l , first[1] - h , first[2])  )

	#4th
	points.append( (first[0]+l , first[1] , first[2])  )

	#5th
	points.append( (first[0]+l , first[1] , first[2]-w)  )

	#6th
	points.append( (first[0]+l , first[1] - h , first[2]-w)  )

	#7th
	points.append( (first[0] , first[1] , first[2]-w)  )

	#8th
	points.append( (first[0] , first[1]-h , first[2]-w)  )

	print "------"
	print "colors are:"
	print "255 0 0"
	print "255 0 0"
	print "0 255 0"
	print "0 255 0"
	print "0 0 255"
	print "0 0 255"
	print "0 255 255"
	print "0 255 255"

	print "------"
	print "8 vertices"
	print "coordinates are:" 

	for elem in points:
		print elem[0], elem[1], elem[2]

	print "------"
	print "12 triangles"
	print "triangles are:"

	print 1+base, 2 + base, 3 + base
	print 1+base, 3 + base, 4 + base
	
	print 8+base, 3 + base, 2 + base
	print 6+base, 3 + base, 8 + base

	print 4+base, 3 + base, 6 + base
	print 4+base, 6 + base, 5 + base

	print 5+base, 6 + base, 8 + base
	print 5+base, 8 + base, 7 + base

	print 7+base, 1 + base, 4 + base
	print 7+base, 4 + base, 5 + base
	
	print 7+base, 2 + base, 1 + base
	print 7+base, 8 + base, 2 + base












