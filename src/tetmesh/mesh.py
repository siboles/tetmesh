import subprocess
import os
import re
import trimesh
import time

class Mesher(object):
    """
    Reads a surface mesh from file and generates a 3-D tetrahedral mesh using
    an executable built with the Computer Geometry Algorithms Library (CGAL).
    Surface mesh formats supported for input using the trimesh module:
      - STL (ASCII and binary)
      - OBJ
      - Wavefront
      - OFF
      - PLY
    Trimesh also can use pyassimp loaders for other formats if pyassimp and assimp libraries are installed.

    Parameters
    ----------
    inputname : str, required
        The surface mesh to construct 3-D tetrahedral mesh from.
    outputname : str="mesh.vtu", optional
        The filename for the 3-D mesh to be saved. If non-.vtu extension is specified this will be replaced.
    facetAngle : float=30, optional
        The target minimum angle between tetrahedral edges to achieve.
    facetDistance : float 0.1, optional
        The distance a surface facet node can deviate from the original surface mesh.
    edgeRatio : float=2.0, optional
        The target maximum-minimum edge ratio.
    edgeLength : float 0.3, optional
        The target maximum element edge length.
    """

    def __init__(self, inputname=None,
                 outputname="mesh.vtu",
                 facetAngle=30,
                 facetDistance=0.1,
                 edgeRatio=2.0,
                 edgeLength=0.3):

        if inputname is None:
            raise SystemError("A surface mesh file name was not supplied. Please provide as parameter inputname.")
        else:
            self.inputname = inputname

        if outputname.endswith(".vtu"):
            self.outputname = outputname
        else:
            self.outputname = re.sub(r"^\.$", ".vtu", outputname)

        self.facetAngle = facetAngle
        self.facetSize = edgeLength
        self.facetDistance = facetDistance
        self.edgeRatio = edgeRatio
        self.elementVolume = edgeLength

        path = os.path.dirname(__file__)
        if os.name == "posix":
            self.exe = os.path.join(path, "mesh_polyhedral_domain")
        elif os.name == "nt":
            self.exe = os.path.join(path, "mesh_polyhedral_domain.exe")
        else:
            raise SystemExit("This operating system is not supported.")

    def _convertFormat(self):
        mesh = trimesh.load_mesh(self.inputname)
        self.inputname = "temporary{:d}.off".format(int(time.time()))
        mesh.export("off", self.inputname)

    def makeMesh(self):
        remove = False
        if not self.inputname.endswith(".off"):
            self._convertFormat()
            remove = True
        subprocess.call([self.exe, str(self.inputname), str(self.outputname),
                         str(self.facetAngle), str(self.facetSize), str(self.facetDistance),
                         str(self.edgeRatio), str(self.elementVolume)])
        if remove:
            os.remove(self.inputname)
