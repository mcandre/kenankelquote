from invoke import run, task

@task
def test():
  run("python kenankelquote.py")

@task
def lint():
  run("pylint *.py")

@task
def guard():
  run("bundle exec guard")

@task
def clean():
  run("rm -rf *.pyc; true")
