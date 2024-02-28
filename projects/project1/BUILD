python_source(
  name="app",
  source="run.py",
  dependencies=[":config"]
)

resource(
  name="config",
  source="config.ini"
)

python_requirements(
    name="reqs"
)

# NOTE: Sources restricted from the default for python_sources due to conflict with
#   - projects/project1:app
python_sources(
    sources=[
        "utils.py"
    ],
)

python_tests(
    name="tests",
    sources=["utils.py"],
    dependencies=["requirements.txt"]
)
