import logging
import os
import sys
import zookeeper
from baseutil import BaseUtil

logger = logging.getLogger()

class ZKUtil(BaseUtil):
  def __init__(self, zk_servers, path):
    if zk_servers is None:
      try:
        zk_servers = os.environ['ZK_SERVERS']
      except KeyError:
        logger.critical('No ZooKeeper servers specified! Exiting.')
        sys.exit(1)
    zookeeper.set_debug_level(zookeeper.LOG_LEVEL_ERROR)
    self.zh = zookeeper.init(zk_servers)
    self.ZOO_OPEN_ACL_UNSAFE = {'perms': 0x1f,
        'scheme': 'world', 'id': 'anyone'}
    self.path = path

  def cat(self):
    return zookeeper.get(self.zh, self.path)[0]

  def exists(self):
    if (zookeeper.exists(self.zh, self.path)):
      return True
    else:
      return False

  def ls(self):
    return zookeeper.get_children(self.zh, self.path)

  def mkdir(self):
    zookeeper.create(self.zh, self.path, '', [self.ZOO_OPEN_ACL_UNSAFE])

  def read(self):
    return zookeeper.get(self.zh, self.path)[0]

  def rm(self):
    zookeeper.delete(self.zh, self.path)

  def stat(self):
    return zookeeper.get(self.zh, self.path)[1]

  def write(self, contents):
    zookeeper.create(self.zh, self.path, contents, [self.ZOO_OPEN_ACL_UNSAFE])

