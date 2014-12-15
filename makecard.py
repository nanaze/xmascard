#!/usr/bin/env python

import sys
import svgwrite

def main():
  drawing = svgwrite.Drawing(size=('1000', '1400'))

  img = svgwrite.image.Image('bullets/NYCS-bull-trans-1.svg',insert=(100, 100), size=(100,100))
  
  drawing.add(img)
  
  sys.stdout.write(drawing.tostring())
  

if __name__ == '__main__':
  main()
