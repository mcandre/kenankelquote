from invoke import run, task

@task(default = True)
def test():
  run("python kenankelquote.py")

@task
def pep8():
  run("pep8 .")

@task
def pylint():
  run("pylint *.py")

@task
def pyflakes():
  run("pyflakes .")

@task("pep8", "pylint", "pyflakes")
def lint():
  pass

@task
def guard():
  run("bundle exec guard")

@task
def clean():
  run("rm -rf *.pyc; true")
