#!/usr/bin/env python

"""Kenan Kel Quote generator"""
__author__ = "Andrew Pennebaker (andrew.pennebaker@gmail.com)"
__date__ = "6 May 2006 - 8 Aug 2007"
__copyright__ = "Copyright 2006 2007 Andrew Pennebaker"
__version__ = "0.1"

import logging
import random
import sys
import getopt

class KenanKelQuote:
  def __init__(self):
    self.logger = logging.getLogger("File")
    self.file_handler = logging.FileHandler("kenankelquote.log")

    self.file_handler.setFormatter(
      logging.Formatter("%(asctime)s %(levelname)s %(message)r")
    )

    self.logger.addHandler(self.file_handler)
    self.logger.setLevel(logging.INFO)

    self.objects = []
    self.places = []

  def load_lines(self, filename):
    """Load funny lines from a text file into a list."""

    self.logger.debug("Opening %s" % (filename))

    f = open(filename, "r")

    self.logger.debug("Opened %s in read text mode" % (filename))
    self.logger.debug("Reading lines")

    lines = ("".join(f.readlines())).split("\n")

    self.logger.debug("Read lines")
    self.logger.debug("Closing %s" % (filename))

    f.close()

    self.logger.debug("Closed %s" % (filename))

    return lines

  def load_quotes(self, objectfile = "objects.txt", placefile = "places.txt"):
    """Load funny items from text files."""

    self.logger.debug("Loading object lines")

    self.objects = self.load_lines(objectfile)

    self.logger.debug("Loaded object lines %s" % (self.objects))
    self.logger.debug("Loading place lines")

    self.places = self.load_lines(placefile)

    self.logger.debug("Loaded place lines %s" % (self.places))

    self.logger.error("Error loading files")

    if len(self.objects) < 1 or len(self.places) < 1:
      self.logger.warn("Objects or places empty: %s %s" % (self.objects, self.places))

  def get_quote(self):
    """Generate random quote"""

    self.logger.debug("Getting random objects")

    o = [random.choice(self.objects) for i in range(3)]

    self.logger.debug("Got random objects: %s" % (o))
    self.logger.debug("Getting random place")

    place = random.choice(self.places)

    self.logger.debug("Got random place %s" % (place))
    self.logger.debug("Concatenating quote")

    quote = "Grab %s, %s, and %s, and meet me %s!" % (
      o[0].strip(),
      o[1].strip(),
      o[2].strip(),
      place.strip()
    )

    self.logger.info("Concatenated quote: %s" % (quote))

    return quote

def usage():
  """Print usage message"""

  print("Usage: [options] %s <objectfile> <placefile>" % (sys.argv[0]))
  print("--loglevel <level>")
  print("-h --help (usage)")

  sys.exit()

def main():
  """Print a random quote"""

  system_args = sys.argv[1:] # ignore program name

  objectfile = "objects.txt"
  placefile = "places.txt"
  loglevel = logging.INFO

  optlist, args = [], []
  try:
    optlist, args = getopt.getopt(system_args, "h", ["loglevel=", "help"])
  except getopt.GetoptError:
    usage()

  for option, value in optlist:
    if option == "-h" or option == "--help":
      usage()
    elif option == "--loglevel":
      try:
        loglevel = int(value)
        if loglevel < logging.NOTSET or loglevel > logging.CRITICAL:
          raise Exception
      except:
        raise Exception("Loglevel is an integer from 0 to 50")

  if len(args) == 2:
    objectfile, placefile = args[0], args[1]

  kenan_kel_quote = KenanKelQuote()
  kenan_kel_quote.logger.setLevel(loglevel)
  kenan_kel_quote.load_quotes(objectfile, placefile)

  quote = kenan_kel_quote.get_quote()

  print(quote)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt as e:
    pass
