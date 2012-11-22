#!/bin/sh

rst2pdf exercise.rst -s kerning,friendly,freetype-sans,eightpoint && mupdf exercise.pdf
