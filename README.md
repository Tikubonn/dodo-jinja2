
# DooDoo Jinja2

![DooDoo 0.9](https://img.shields.io/badge/DooDoo-0.9-orange.svg "DooDoo 0.9")
![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg "Python 3.6")
![GPLv3](https://img.shields.io/badge/License-GPL-green.svg "GPLv3")

DooDoo Jinja2 add the template engine of [Jinja2](https://github.com/tikubonn/peco) to DooDoo.  
Jinja2 is popular template engine in Python packages.

## Requirement

* [doodoo==0.9.1](https://github.com/tikubonn/doodoo)
* [jinja2==2.10.1](http://jinja.pocoo.org/)

## Installation

DooDoo Jinja2 has `setup.py`, so you can install it with this command.

```shell
$ python setup.py install
```

## Setup

DooDoo Peco is not enable if you just installed it.
if you want to enable this plugin, you should add configuration to `doodoo.json` like this.

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
        "name": "doodoo_jinja2",
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

DooDoo Jinja2 has released under the [GPLv3](LICENSE.txt).  
DooDoo Jinja2 has required [Jinja2](http://jinja.pocoo.org/), that has released under the [BSD License](license/LICENSE_JINJA2.txt). please read detail to [license/LICENSE_JINJA2.txt](license/LICENSE_JINJA2.txt).  
