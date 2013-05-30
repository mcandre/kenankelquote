from fabric.api import local

def test():
  local("python kenankelquote.py")

def guard():
  local("bundle exec guard")

def lint():
  local("pylint *.py; true")

def clean():
  local("rm -rf *.pyc; true")
