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


def _CreateTree():
  tree = minidom.Element('svg')

  tree.setAttribute('viewBox', '0 0 1 1')

  def AddPolygon(points):
    tri = minidom.Element('polygon')

    point_strings = []
    for point in points:
      point_strings.append('%f, %f' % point)

    points_string = ' '.join(point_strings)
    tri.setAttribute('points', points_string)
    tri.setAttribute('style', 'fill:#3C8D0D')
    tree.appendChild(tri)

  def AddTriangle(top, bottom, width):
    points = [
      (0.5, top),
      (0.5 - (width / 2.0), bottom),
      (0.5 + (width / 2.0), bottom)]
    AddPolygon(points)

  AddTriangle(0, 0.25, 0.3)
  AddTriangle(0.1, 0.45, 0.45)
  AddTriangle(0.2, 0.66, 0.6)
  AddTriangle(0.3, 0.9, 0.78)
  
  return tree

def main():

  doc = minidom.Document()

  svg = doc.createElement('svg')
  svg.setAttribute('xmlns', "http://www.w3.org/2000/svg")

  doc.appendChild(svg)

  # Build tree with triangles
  tree = _CreateTree()

  x_offset = 100
  y_offset = 100
  tree.setAttribute('width', str(800))
  tree.setAttribute('height', str(800))
  tree.setAttribute('x', str(x_offset))
  tree.setAttribute('y', str(y_offset))

  svg.appendChild(tree)

  # Append a bullet. translate should be a tuple.
  def AppendBullet(bullet_name, translate=None):

    g = doc.createElement('g')
    svg.appendChild(g)

    if translate:
      g.setAttribute('transform', 'translate(%s, %s)' % translate)

    path = 'bullets/NYCS-bull-trans-%s.svg' % bullet_name
    bullet_svg = _LoadSvg(path)
    g.appendChild(bullet_svg)

  AppendBullet('A', (400, 400))
  AppendBullet('B', (500, 150))
  AppendBullet('C', (500, 650))
  AppendBullet('D', (400, 200))
  AppendBullet('E', (200, 500))
  AppendBullet('F', (300, 200))
  AppendBullet('G', (400, 300))
  AppendBullet('J', (400, 800))
  AppendBullet('L', (300, 240))
  AppendBullet('M', (350, 500))
  AppendBullet('N', (400, 200))
  AppendBullet('Q', (400, 200))
  AppendBullet('R', (400, 200))
  AppendBullet('S', (400, 200))
  AppendBullet('Z', (400, 200))
  AppendBullet('1', (400, 200))
  AppendBullet('2', (400, 200))
  AppendBullet('3', (400, 200))
  AppendBullet('4', (400, 200))
  AppendBullet('5', (400, 200))
  AppendBullet('6', (400, 200))
  AppendBullet('7', (400, 725))                
  
  xmlstr = doc.toprettyxml()

  # drop the first line, the <?xml ...> bit.
  for line in xmlstr.splitlines(True)[1:]:
    sys.stdout.write(line)
  

if __name__ == '__main__':
  main()
