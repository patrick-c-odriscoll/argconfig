import argparse
import yaml

__author__ = "Patrick C O\'Driscoll"
__copyright__ = "2020"
__credits__ = ["Patrick C O\'Driscoll"]
__license__ = "MIT"
__version__ = "0.0.0"
__maintainer__ = "Patrick C O\'Driscoll"
__email__ = "patrick.c.odriscoll@gmail.com"


class argconfig(argparse.ArgumentParser):
  def __init__(self, config=None, *args, **kargs,):
    """ Initialization of the class """
    super().__init__(*args,**kargs)
    if config is not None:
      self.config = config
      try:
        with open(config,'r') as f:
          self.parms = yaml.safe_load(f)
      except:
        pass
    return
  
  def add_argument(self, *args, **kargs):
    try:
      kargs['default'] = self.getConfig(args,kargs['default'])
    except:
      try:
          kargs['default'] = self.getConfig(args,None)
      except:
        pass
      pass
    super().add_argument(*args,**kargs)
    return

  def getConfig(self,arg,value):
    for ii in arg:
      try:
        return self.parms[ii.lstrip('-')]
      except:
        pass
    return value


if __name__ == "__main__":
  parser = argconfig(description='argparse + yaml config file example',config='./example.yaml')
  parser.add_argument('-f','--foo', type=str, default='testing',help='foo (default=testing, config=test)')
  parser.add_argument('--bar',                                  help='bar (default=None, config = 2.0)')
  args = parser.parse_args()

  print(args.foo)
  print(args.bar)