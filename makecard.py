#!/usr/bin/env python

import sys
import svgwrite
from xml.dom import minidom

def _LoadSvg(path):
  doc = minidom.parse(path)
  doc_frag = minidom.DocumentFragment()
  for node in doc.childNodes:
    doc_frag.appendChild(node)
  return doc_frag


def _CreateTriangle():
  tree = minidom.Element('svg')

  tree.setAttribute('viewBox', '0 0 1 1')
  
  tri = minidom.Element('polygon')
  tri.setAttribute('points', '0.5,0 0,1 1,1')
  tri.setAttribute('style', 'fill:#3C8D0D')
  tree.appendChild(tri)

  return tree

def main():

  doc = minidom.Document()

  svg = doc.createElement('svg')
  svg.setAttribute('xmlns', "http://www.w3.org/2000/svg")

  doc.appendChild(svg)

  # Build tree with triangles
  tri = _CreateTriangle()

  x_offset = 100
  y_offset = 200
  tri.setAttribute('width', str(800))
  tri.setAttribute('height', str(800))
  tri.setAttribute('x', str(x_offset))
  tri.setAttribute('y', str(y_offset))

  svg.appendChild(tri)

  # Append a bullet. translate should be a tuple.
  def AppendBullet(bullet_name, translate=None):

    g = doc.createElement('g')
    svg.appendChild(g)

    if translate:
      g.setAttribute('transform', 'translate(%s, %s)' % translate)

    path = 'bullets/NYCS-bull-trans-%s.svg' % bullet_name
    bullet_svg = _LoadSvg(path)
    g.appendChild(bullet_svg)

  # Just for now, paint out all the bullets.
  y = 0
  for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'L', 'M', 'N', 'Q', 'R', 'S', 'Z'] + range(1,8):
    AppendBullet(letter, (0, y))
    y += 50
  
  xmlstr = doc.toprettyxml()

  # drop the first line, the <?xml ...> bit.
  for line in xmlstr.splitlines(True)[1:]:
    sys.stdout.write(line)
  

if __name__ == '__main__':
  main()
