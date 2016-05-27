from tetmesh import mesh

m = mesh.Mesher(inputname="torus.stl",
                outputname="torus.vtu",
                facetAngle=30.0,
                facetDistance=0.1,
                edgeLength=.2,
                edgeRatio=1.5)
m.makeMesh()

