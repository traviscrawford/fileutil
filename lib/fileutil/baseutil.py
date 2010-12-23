class BaseUtil(object):
  """Common file system interface."""
  def __init__(self, path):
    pass

  def cat(self):
    raise NotImplementedError

  def exists(self):
    raise NotImplementedError

  def ls(self):
    raise NotImplementedError

  def mkdir(self):
    raise NotImplementedError

  def read(self):
    raise NotImplementedError

  def rm(self):
    raise NotImplementedError

  def stat(self):
    raise NotImplementedError

  def write(self, contents):
    raise NotImplementedError
