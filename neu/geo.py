import paramak
import os


rotated_circle = paramak.ExtrudeCircleShape(
    points=[
         (0, 0),
       
        
    ],
    radius=.95,
    distance=1.2,
    workplane='XZ',
    stl_filename='part0.stl',
)





grey_part = paramak.ExtrudeMixedShape(
    points=[
         (-1.15, -1.25, 'straight'),
         (1.15, -1.25, 'straight'),
         (1.15, 1.75, 'straight'),
         (-1.15, 1.75, 'straight'),
         
    ],
    distance=1.2,
    color=(0.5,0.5,0.5),
    cut=rotated_circle,
    material_tag='tungsten',
    stp_filename='part1.stp',
    stl_filename='part1.stl',
)





rotated_straights = paramak.RotateMixedShape(
    points=[
         (.75, -.6, 'straight'),
         (.95, -.6, 'straight'),
         (.95, .6, 'straight'),
         (.75, .6, 'straight'),
         
    ],
    workplane='XY',
    rotation_angle=360,
    material_tag='Cu',
    stl_filename='part2.stl',
)


rotated_straights1 = paramak.RotateMixedShape(
    points=[
         (.6, -.6, 'straight'),
         (.75, -.6, 'straight'),
         (.75, .6, 'straight'),
         (.6, .6, 'straight'),
         
    ],
    workplane='XY',
    rotation_angle=360,
    material_tag='cuzrcr',
    stl_filename='part3.stl',
)



myreactor=paramak.Reactor([grey_part,rotated_straights,rotated_straights1])


# exports the reactor shapes as a DAGMC h5m file which can be used as
# neutronics geometry by OpenMC
my_reactor.export_dagmc_h5m('dagmc.h5m')

# this converts the neutronics geometry h5m file into a vtk file for
# visualisation in Paraview or Visit
os.system('mbconvert dagmc.h5m dagmc.vtk')
