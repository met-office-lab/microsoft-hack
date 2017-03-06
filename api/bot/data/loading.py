import glob
from types import *
import iris
from multipledispatch import dispatch


class Parameter(object):
    def __init__(self, name, data_path):
        self.name = name
        self.data_path = data_path

    def _load(self, filenames):
        cubes = iris.load(filenames)
        return cubes.concatenate_cube()

    @dispatch()
    def load(self):
        filenames = '{}/*'.format(self.data_path)
        return self._load(filenames)

    @dispatch(str)
    def load(self, pattern):
        filenames = glob.glob('{}/*{}*'.format(self.data_path, pattern))
        return self._load(filenames)
