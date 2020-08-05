from commandlib import Command
from path import Path
import hitchbuild


class DockerImage(hitchbuild.HitchBuild):
    def __init__(self, filename, imagename):
        self._filename = Path(filename).abspath()
        self._imagename = imagename
        self._dkr = Command("docker")
    
    def build(self):
        self._dkr("build", ".", "-f", self._filename, "-t", self._imagename).run()
    
    @property
    def run(self):
        return self._dkr("run", self._imagename)
        
