# Python API Polylith Example

Example Python project using Polylith, and uv, to have a monorepo with FastAPI APIs.

---

## Testing
To test if the code works as expected, and compiles / runs, use pytest:
```
uv run pytest
```
To only test one base/component, you can do this:
```
uv run pytest -k api_foo
```
Where `api_foo` is the name of the base or component you want to test.

You can also test multiple at once like this:
```
uv run pytest -k "api_foo or math_utils or service_foo"
```

You can also test against all changes in the last N commits:
```
uv run pytest -k "$(uv run poly diff --since @~10 --bricks --short | sed "s/,/ or /g")"
```
Where `@~10` indicates to compare it againsts what it was like 10 commits ago.  You can also give a specific commit, etc.


## Running
To run a specific project, use the `run.sh` script, and pass in the name of a project, e.g. `api_foo` (this will get checked, so it will tell you if the project doesn't exist).
Alternativelly, you can directly call uvicorn like this:
```
uv run uvicorn example.api_foo.core:app
```
Where `example` is the namespace, `api_foo` is the project, `core` is the module, and `app` is in this case specifying that it's going to run the FastAPI app.


## Dockerfile
Each project has a dockerfile that can be used to deploy.  To build and run the dockerfile, you have to do this:
```
cd projects/api_foo
uv export --no-emit-project --output-file requirements.txt
uv build --out-dir ./dist
sudo docker build -t image_name .
sudo docker run --name container_name -p 8000:8000 image_name
```
Where `api_foo` is the project, `image_name` is the name of the image, and `container_name` is the name of the container.
Also, the port 8000 is exposed as that is the port specified in the dockerfile.


## Listing project dependencies
To see which bases and components and project depends upon, you can use this command:
```
uv run poly info
```
To see what third-party libraries the projects depend upon, you can use this command:
```
uv run poly libs
```


## Testing in a REPL
If you want to test functionality in a REPL before writing out a component or base, you can do that in the `development` folder.
I already have set up a python file for me there, with instructions about how to run that with a REPL, but if you want to import other modules,
or just want to have your own setup, you can create your own file there to do this.

You can read more about this here:
- https://davidvujic.github.io/python-polylith-docs/workspace/?h=development#development
- https://polylith.gitbook.io/polylith/architecture/2.4.-development


## Creating new projects
Each project has metadata in `projects/`, and an implementation in `base/`.  Then it's dependencies are in `components/`.  Each project is essentially just an interface to a given set of components.
You can create a new base with this command:
```
uv run poly create base --name <name of base>
```
You can create a new project with this command:
```
uv run poly create project --name <name of project>
```
You may want to copy over the dockerfile from an existing project, and modify it to fit the needs of the project.
You may also want to do the same with the `pyproject.toml` file, where you have to add the dependencies, base, and components that the project uses.

You may also want to update the generated tests in `tests/base/<namespace>/<base name>/`.  Don't remove the test that was generated for you, as this can be used to make sure it at least compiles.

You can read more about this here:
- https://davidvujic.github.io/python-polylith-docs/workspace/?h=bases#bases
- https://davidvujic.github.io/python-polylith-docs/workspace/?h=project#projects
- https://polylith.gitbook.io/polylith/architecture/2.2.-base
- https://polylith.gitbook.io/polylith/architecture/2.6.-project


## Creating new components
Components are the building blocks of the projects.
You can create a new component with this command:
```
uv run poly create component --name <name of component>
```
Here you don't need to have any other setup, but it may be woth noting that you should add in the functions you want to expose in `components/<namespace>/<component name>/__init__.py`,
and you may want to add more test in `tests/components/<namespace>/<component name>/`.  Don't remove the test that was generated for you, as this can be used to make sure the component
at least compiles.

You can read more about this here:
- https://davidvujic.github.io/python-polylith-docs/workspace/?h=components#components
- https://polylith.gitbook.io/polylith/architecture/2.3.-component
