Fileutil provides a common interface for simple operations on several filesystem-like storage systems. Operations can span filesystem implementations, enabling one to, say, copy a local file to ZooKeeper.

Modes:

*  cat <path>
*  cp [-f] <source> <destination>
*  ls <path>
*  mkdir <path>
*  rm <path>
*  stat <path>

Supported filesystems:

*  /local/absolute/path/name
*  zk:///zookeeper/znode
