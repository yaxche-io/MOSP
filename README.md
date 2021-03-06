# MONARC Objects Sharing Platform

[![MOSP logo](https://github.com/CASES-LU/MOSP/blob/master/mosp/static/img/logo-large.png)](https://github.com/CASES-LU/MOSP)

[![Latest release](https://img.shields.io/github/release/CASES-LU/MOSP.svg?style=flat-square)](https://github.com/CASES-LU/MOSP/releases/latest)
[![License](https://img.shields.io/github/license/CASES-LU/MOSP.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Contributors](https://img.shields.io/github/contributors/CASES-LU/MOSP.svg?style=flat-square)](https://github.com/CASES-LU/MOSP/graphs/contributors)
[![Stars](https://img.shields.io/github/stars/CASES-LU/MOSP.svg?style=flat-square)](https://github.com/CASES-LU/MOSP/stargazers)
[![Workflow](https://github.com/CASES-LU/MOSP/workflows/Python%20application/badge.svg?style=flat-square)](https://github.com/CASES-LU/MOSP/actions?query=workflow%3A%22Python+application%22)


## Presentation

[MOSP](https://github.com/CASES-LU/MOSP) is a platform for creating, editing
and sharing *validated* JSON objects of any type.

The goal is to gather security related JSON objects, in the first place aimed
to be used with [MONARC](https://github.com/monarc-project/MonarcAppFO).

You can use any available JSON schemas in order to create new JSON objects via a
web form dynamically generated and based on the selected schema.  
It is possible to interact with MOSP programmatically thanks to its API.  
Some JSON objects can be exported to a
[MISP galaxy](https://github.com/MISP/misp-galaxy).

As example you can have a look at [official instance](https://objects.monarc.lu)
operated by [CASES](https://github.com/CASES-LU) and more particularly the
[objects](https://objects.monarc.lu/organization/MONARC) shared by the
[MONARC project](https://github.com/monarc-project).


## Installation

There are different ways to deploy MOSP.


### Clone the repository and use a Python virtualenv

```bash
$ git clone https://github.com/CASES-LU/MOSP.git
$ cd MOSP/
$ npm install
$ poetry install
$ poetry shell
$ python manager.py db_create
$ python manager.py db_init
$ python manager.py import_licenses_from_spdx
$ python manager.py create_admin <username> <password>
$ pybabel compile -d mosp/web/translations
$ python runserver.py
```


### Deploy to Heroku

Manually with some simple commands:

```bash
$ git clone https://github.com/CASES-LU/MOSP.git
$ cd MOSP/
$ heroku create --region eu <name-of-your-instance>
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku config:set APPLICATION_SETTINGS='heroku.cfg'
$ heroku buildpacks:add --index 1 heroku/python
$ heroku buildpacks:add --index 2 https://github.com/heroku/heroku-buildpack-nodejs
$ git push heroku master
$ heroku run init
$ heroku run python manager.py import_licenses_from_spdx
$ heroku ps:scale web=1
```

or simply with this button:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/CASES-LU/MOSP)

The default credentials are *admin* for the login and *password* for the
password.

If you want to create other users programmatically:

```bash
$ heroku run python manager.py create_user <login> <password>
$ heroku run python manager.py create_admin <login> <password>
```

## Contributing

Contributions are welcome and there are many ways to participate to the
project. You can contribute to MOSP by:

- reporting bugs;
- suggesting enhancements or new features;
- improving the documentation;
- creating new objects on [our instance](https://objects.monarc.lu).

Feel free to fork the code, play with it, make some patches and send us
pull requests.

There is one main branch: what we consider as stable with frequent updates as
hot-fixes.

Features are developed in separated branches and then regularly merged into the
master stable branch.


## Documentation

A [documentation](https://www.monarc.lu/documentation/MOSP-documentation)
is available on the MONARC website.


## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)


* Copyright (C) 2018-2019 Cédric Bonhomme
* Copyright (C) 2018-2019 SMILE gie securitymadein.lu

For more information, the [list of authors and contributors](AUTHORS.md) is
available.
