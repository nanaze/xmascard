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

def main():

  doc = minidom.Document()

  svg = doc.createElement('svg')
  svg.setAttribute('xmlns', "http://www.w3.org/2000/svg")

  doc.appendChild(svg)

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
