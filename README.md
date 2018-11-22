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

Box maker:

python box_maker.py <start_x>
                    <start_y>
                    <start_z>
                    <length>
                    <width>
                    <height>
                    <last_vertex_id_in_3d_space>

- "Start x, y, z" values are the first vertex of the box (rectangular parallelpiped). 
- "Length" states distance between to edges of rectangle in X coordinates.
- "Width" states distance between to edges of rectangle in Z coordinates.
- "Height" states distance between to edges of rectangle in Y coordinates.
- "Last vertex in 3d space" means that if there is another object in the 3d space before, it gives new vertex ids after the last vertex id of the previous object. If this is the first object you will add, last vertex in 3d space should be given as 0. Otherwise, give it as last vertex id of the lastly added object.


Star maker:

python star_maker.py <star_center_x>
                    <star_center_y>
                    <star_z_coord>
                    <star_back_distance>
                    <start_x>
                    <start_y>
                    <last_vertex_id_in_3d_space>

Cone maker:

python cone_maker.py <cone_bottom_center_x>
                    <cone_bottom_center_y>
                    <cone_bottom_z_coord>
                    <cone_top_distance>
                    <cone_bottom_radius>
                    <step_threshold>
                    <last_vertex_id_in_3d_space>
                    <color_primary: "R|G|B">
                    <color_secondary: "R|G|B">
                    <color_bottom_center: "R|G|B">
                    <color_top: "R|G|B">


