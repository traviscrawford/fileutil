import os
from baseutil import BaseUtil


class LocalUtil(BaseUtil):
  def __init__(self, path):
    self.path = path

  def cat(self):
    return open(self.path).read()

  def exists(self):
    try:
      os.stat(self.path)
      return True
    except OSError:
      return False

  def ls(self):
    return os.listdir(self.path)

  def mkdir(self):
    os.mkdir(self.path)

  def read(self):
    return open(self.path).read()

  def rm(self):
    os.unlink(self.path)

  def stat(self):
    return os.stat(self.path)

  def write(self, contents):
    fh = open(self.path, 'w')
    fh.write(contents)
    fh.close()
