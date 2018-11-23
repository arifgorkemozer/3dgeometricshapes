# 3dgeometricshapes
Vertex, color and triangle generation for objects in 3d space.

# What is this about?

These scripts generates 3d shapes such as
    - pyramid (pyramid_maker.py)
    - comet (star_maker.py)
    - cone (cone_maker.py)
    - rectangular parallelpiped (box_maker.py)


by generating vertices in 3d space. In addition, these scripts also generate triangles from these vertices. Each vertex of a triangle has a color associated with it. To understand what these scripts generate as a model, visuals are added in the repository.

# How to run?

If you run scripts without an argument, they will fail and write a message that states arguments needed. However, it is better to show them here as well:

Camera maker:

> python camera_maker.py <camera_file_name>

- "Camera file name" will be name of the output file, if ".txt" extension is not added, it generates it as "<camera_file_name>.txt"

Box maker:

> python box_maker.py <start_x>
>                    <start_y>
>                    <start_z>
>                    <length>
>                    <width>
>                    <height>
>                    <last_vertex_id_in_3d_space>

- "Start x, y, z" values are the first vertex of the box (rectangular parallelpiped). According to visuals provided, vertex with number 1.
- "Length" states distance between to edges of rectangle in X coordinates.
- "Width" states distance between to edges of rectangle in Z coordinates.
- "Height" states distance between to edges of rectangle in Y coordinates.
- "Last vertex in 3d space" means that if there is another object in the 3d space before, it gives new vertex ids after the last vertex id of the previous object. If this is the first object you will add, last vertex in 3d space should be given as 0. Otherwise, give it as last vertex id of the lastly added object.


Star maker:

> python star_maker.py <star_center_x>
>                    <star_center_y>
>                    <star_z_coord>
>                    <star_back_distance>
>                    <start_x>
>                    <start_y>
>                    <last_vertex_id_in_3d_space>

- "Star center x, y" values are the central vertex of the star. According to visuals provided, vertex with number 11.
- "Star z coordinate" states common Z coordinate that all points on the star has. This for generating flat 5-point star surface along XY axis.
- "Star back distance" states distance central vertex of the star and a point on the back that converts this star to a comet.
- "Start x, y" values are the first vertex of the star. Top of the star; in other words, edge that points to upward direction. According to visuals provided, vertex with number 1.
- "Last vertex in 3d space" means that if there is another object in the 3d space before, it gives new vertex ids after the last vertex id of the previous object. If this is the first object you will add, last vertex in 3d space should be given as 0. Otherwise, give it as last vertex id of the lastly added object.


Cone maker:

> python cone_maker.py <cone_bottom_center_x>
>                    <cone_bottom_center_y>
>                    <cone_bottom_z_coord>
>                    <cone_top_distance>
>                    <cone_bottom_radius>
>                    <step_threshold>
>                    <last_vertex_id_in_3d_space>
>                    <color_primary: "R|G|B">
>                    <color_secondary: "R|G|B">
>                    <color_bottom_center: "R|G|B">
>                    <color_top: "R|G|B">

- "Cone bottom center x, y" values are the central vertex of the cone bottom. According to visuals provided, vertex with number n-1, where n is the number of vertices generated for the cone.
- "Cone bottom z coordinate" states common Z coordinate that all points on the cone bottom has. This for generating flat round surface along XY axis.
- "Cone top distance" states distance central vertex of the cone bottom and a point on the back that converts this circle to a cone.
- "Cone bottom radius" states radius of the round surface on the cone bottom.
- "Step threshold" states the X distance between the vertices of the cone bottom. While generating round surface, many triangles are appended to each other to make it look like a round surface. If step threshold decreases and approaches to 0, you will get full circle.
- "Last vertex in 3d space" means that if there is another object in the 3d space before, it gives new vertex ids after the last vertex id of the previous object. If this is the first object you will add, last vertex in 3d space should be given as 0. Otherwise, give it as last vertex id of the lastly added object.
- "Color primary" states the color of the first vertex of a triangle on cone bottom. Optional parameter. Default red.
- "Color secondary" states the color of the second vertex of a triangle on cone bottom. Optional parameter. Default blue.
- "Color bottom center" states the color of the central vertex on cone bottom. Vertices with color primary and color secondary connects to central vertex, making a small triangle. Optional parameter. Default green.
- "Color top" states the color of the point on the back that converts this circle to a cone. Optional parameter. Default cyan.

