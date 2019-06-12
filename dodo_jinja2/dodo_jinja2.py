
from dodo.trait import Template
from dodo.trait import Configurable
from dodo.registry import register_template
from jinja2 import Template as JinjaTemplate
from pathlib import Path
from bs4 import BeautifulSoup as Bs
import os


class Jinja2Wrapper (Template, Configurable):

    """
    wrapper class of Jinja2Wrapper for dodo.
    """

    def __init__(self, config=dict()):
        Template.__init__(self)
        Configurable.__init__(self, config=config)
        self.path = None
        self.rootdir = None

    # override
    def setup(self):
        self.path = Path(self.get_config()["path"])
        self.rootdir = Path(self.get_config().get("root_dir", "."))

    def fix_path(self, address):
        if address.startswith("http://"):
            return address
        if address.startswith("https://"):
            return address
        if address.startswith("/"):
            return address
        return Path("/").joinpath(
            self.path.parent.relative_to(
                self.rootdir
            ).joinpath(address))

    def fix_all_path(self, bs):
        for element in bs.find_all(href=True):
            element["href"] = self.fix_path(element["href"])
        for element in bs.find_all(src=True):
            element["src"] = self.fix_path(element["src"])

    # override
    def render(self, stream, **keywords):
        with open(self.path, "r", encoding="utf-8") as streamin:
            template = JinjaTemplate(streamin.read())
            rendered = template.render(**keywords)
            bs = Bs(rendered, "html5lib")
            self.fix_all_path(bs)  # fix all path
            stream.write(str(bs))

    # override
    def get_update_time(self):
        return os.stat(self.path).st_mtime


def init(request):
    """
    register Jinja2Wrapper to dodo.
    """

    register_template("jinja2", Jinja2Wrapper)
