
# DoDo Jinja2

![DoDo 0.9](https://img.shields.io/badge/DoDo-0.9-orange.svg "DoDo 0.9")
![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg "Python 3.6")
![GPLv3](https://img.shields.io/badge/License-GPL-green.svg "GPLv3")

DoDo Jinja2 add the template engine of [Jinja2](https://github.com/tikubonn/peco) to DoDo.  
Jinja2 is popular template engine in Python packages.

## Requirement

* [dodo==0.9.2](https://github.com/tikubonn/dodo)
* [jinja2==2.10.1](http://jinja.pocoo.org/)

## Installation

DoDo Jinja2 has `setup.py`, so you can install it with this command.

```shell
$ python setup.py install
```

## Setup

DoDo Peco is not enable if you just installed it.
if you want to enable this plugin, you should add configuration to `dodo.json` like this.

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
        "name": "dodo_jinja2",
        "config": {}
      }
    ]
  }
}
```

### Customization

you can customize this plugin with editing `config` section.

| Configuration | Description | 
| ------------- | ----------- |
| path          | template source file. it is necessary. |

## License

DoDo Jinja2 has released under the [GPLv3](LICENSE.txt).  
DoDo Jinja2 has required [DoDo](https://github.com/tikubonn/dodo), that has released under the [GPLv3](license/LICENSE_DODO.txt). please read detail to [license/LICENSE_DODO.txt](license/LICENSE_DODO.txt).  
DoDo Jinja2 has required [Jinja2](http://jinja.pocoo.org/), that has released under the [BSD License](license/LICENSE_JINJA2.txt). please read detail to [license/LICENSE_JINJA2.txt](license/LICENSE_JINJA2.txt).  
