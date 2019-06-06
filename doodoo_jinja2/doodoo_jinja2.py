
from doodoo.trait import Template
from doodoo.trait import Configurable
from doodoo.registry import register_template
from jinja2 import Template as JinjaTemplate
import os 

class Jinja2Wrapper (Template, Configurable):
  
  """
  wrapper class of Jinja2Wrapper for doodoo.
  """
  
  def __init__ (self, config=dict()):
    Template.__init__(self)
    Configurable.__init__(self, config=config)
    self.path = None 
  
  # override
  def setup (self):
    self.path = self.get_config()["path"]
  
  # override
  def render (self, stream, **keywords):
    with open(self.path, "r", encoding="utf-8") as streamin:
      template = JinjaTemplate(streamin.read())
      stream.write(template.render(**keywords))

  # override
  def get_update_time (self):
    return os.stat(self.path).st_mtime
  
def init (request):
  
  """
  register Jinja2Wrapper to doodoo.
  """
  
  register_template("jinja2", Jinja2Wrapper)
