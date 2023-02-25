
# Sakyum

An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs. <a href="https://sakyum.readthedocs.io">Read more</a>

## Installation

Install and update the latest release from <a href="https://pypi.org/project/sakyum">pypi</a>. Basically the library was uploaded using `sdist` (Source Distribution) and this software (library) might not be compatible with `windows operating system` but it works on other `OS` such as `linux` and `macOS`

```
pip install --upgrade sakyum
```

## Create your first flask project using sakyum

After the installation paste the following command on your termianl

```
python -c "from sakyum import project; project('todo_project')"
```

this will create a project (directory) called `todo_project` now cd into the `todo_project` directory, if you do `ls` within the directory you just enter, you will see a module called `thunder.py` and some directories (some in the form of package) `auth`, `static`, `templates` and a directory with thesame name of your base directory name, in our case it is `todo_project`.

Boot up the flask server by running the below command

```
python thunder.py boot
```

Now visit the local url `http://127.0.0.1:5000` this will show you index page of your project

## Create flask app within your project (todo_project)

For you to start an app within your project `todo_project` shutdown the flask development server by pressing ( CTRL+C ) and then run the following command, by giving the name you want your app to be, in our case we will call our app `todo_app`

```
python thunder.py create_app -a todo_app
```

this will create an app (a new package called `todo_app`) within your project `(todo_project)`

## Register an app

Once the app is created open a file called `todo_project/routes.py` and import your `todo_app` blueprint which is in (`todo_app/views.py`), default name given to an app blueprint, is the app name so our `todo_app` blueprint name is `todo_app`, after importing it, append (register) the app blueprint in a list called `reg_blueprints` in that same file of `todo_project/routes.py`

importing blueprint

```py
from todo_app.views import todo_app
```

registering blueprint

```
reg_blueprints = [
  default,
  errors,
  auth,
  base,
  todo_app,
]
```

once you register the app, boot up the flask webserver again by

```
python thunder.py boot
```

visit `http://127.0.0.1:5000` which is your project landing page

visit `http://127.0.0.1:5000/todo_app` this will take you to your app landing page (todo_app)

visit `http://127.0.0.1:5000/todo_app` this will take you to admin page. From there you are ready to go. See more documentations <a href="https://sakyum.readthedocs.io">here!</a>

## Useful links

- Documentation: https://sakyum.readthedocs.io
- Repository: https://github.com/usmanmusa1920/sakyum
- PYPI Release: https://pypi.org/projects/sakyum
- Website: https://readthedocs.org/projects/sakyum

Pull requests are welcome
