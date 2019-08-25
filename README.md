
# DoDo Jinja2

![DoDo 0.9](https://img.shields.io/badge/DoDo-0.9-orange.svg "DoDo 0.9")
![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg "Python 3.6")
![GPLv3](https://img.shields.io/badge/License-GPL-green.svg "GPLv3")

DoDo Jinja2 is a official plugin that add a popular template engine to your environment.

## Usage

after installed and configured, this plugin will render page with template automatically.

## Setup

this plugin is not enabled if you just installed, so you should add configuration to your config file.

```json
{
  "post": {
    "template": {
      "name": "jinja2",
      "config": {
        "path": "static/template.html"
      }
    }
  },
  "recent": {
    "template": {
      "name": "jinja2",
      "config": {
        "path": "static/template-recent.html"
      }
    }
  },
  "date": {
    "template": {
      "name": "jinja2",
      "config": {
        "path": "static/template-date.html"
      }
    }
  },
  "plugin": {
    "init": [
      {
        "name": "dodo_jinja2"
      }
    ]
  }
}
```

### Customization

you can customize this plugin with editing `config` section.

#### `path` parameter

this parameter is necessary.
this take a path name of template file.

## Installation

this package contain a `setup.py`, so you can install it with this command.

```shell
$ python setup.py install
```

## Requirement

* [dodo==0.9.3](https://github.com/tikubonn/dodo)
* [jinja2==2.10.1](http://jinja.pocoo.org/)

## License

* DoDo Jinja2 has released under the [GPLv3](LICENSE). 
* [DoDo](https://github.com/tikubonn/dodo) has released under the [GPLv3](license/dodo/LICENSE_DODO). please read detail to [license/dodo/LICENSE_DODO](license/dodo/LICENSE_DODO). 
* [Jinja2](http://jinja.pocoo.org/) has released under the [BSD License](license/jinja2/LICENSE_JINJA2). please read detail to [license/jinja2/LICENSE_JINJA2](license/jinja2/LICENSE_JINJA2). 
