#!/usr/bin/python

import sys

import logging
#logging.basicConfig(level = logging.DEBUG)

import gi
gi.require_version('Vips', '8.0')
from gi.repository import Vips 

a = Vips.Image.black(100, 100)

a = a.draw_circle(128, 50, 50, 20)

b = a.hough_circle(scale = 1, min_radius = 15, max_radius = 25)

b.write_to_file("x.v")
