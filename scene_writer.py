


def write_scene_to_file(filename, points, colors, triangles, last_vertex_id):
    with open(filename, 'w') as out_file:
		out_file.write('<Vertices count="%d">\n' % len(points))

		for i in range(0, len(points)):
			out_file.write( '	<Vertex id="%d" position="%s" color="%s" />\n' % (last_vertex_id+i+1, " ".join([str(elem) for elem in points[i]]), " ".join([str(elem) for elem in colors[i]]))  )

		out_file.write("</Vertices>\n")

		out_file.write('<Models count="1">\n')
		out_file.write('	<Model id="1" type="1">\n')

		out_file.write('		<Transformations count="0"></Transformations>\n')
		out_file.write('		<Triangles count="%d">\n' % len(triangles))

		for i in range(0, len(triangles)):
			out_file.write( '			<Triangle>%s</Triangle>\n' % (" ".join([str(vertexId) for vertexId in triangles[i]]))  )

		out_file.write("		</Triangles>\n")
		

		out_file.write("	</Model>\n")
		out_file.write("</Models>\n")