#!/usr/bin/env python

import sys
import svgwrite
from xml.dom import minidom

def _LoadSvg(path):
  doc = minidom.parse(path)
  doc_frag = minidom.DocumentFragment()
  for node in doc.childNodes:
    if node.nodeType == minidom.Node.ELEMENT_NODE:
      if node.tagName == 'svg':
        return node

  raise Exception('no svg found')


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
    tri.setAttribute('style', 'fill:#006400')
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

  ornaments = doc.createElement('svg')
  ornaments.setAttribute('width', '800')
  ornaments.setAttribute('height', '800')
  ornaments.setAttribute('x', str(x_offset))
  ornaments.setAttribute('y', str(y_offset))
  ornaments.setAttribute('viewBox', '0 0 1 1')  
  
  svg.appendChild(ornaments)
  
  # Append a bullet. translate should be a tuple.
  def AddOrnament(bullet_name, translate=None):
    g = doc.createElement('g')
    ornaments.appendChild(g)
    
    if translate:
      g.setAttribute('transform', 'translate(%s, %s)' % translate)

    path = 'bullets/NYCS-bull-trans-%s.svg' % bullet_name
    bullet = _LoadSvg(path)

    bullet_size = 0.13
    bullet.setAttribute('width', str(bullet_size))
    bullet.setAttribute('height', str(bullet_size))
    bullet.setAttribute('viewBox', '0 0 100 100')    
    g.appendChild(bullet)

  AddOrnament('A', (0.5, 0.5))
  AddOrnament('B', (0.45, 0.32))
  AddOrnament('C', (0.32, 0.33))
  AddOrnament('D', (0.41, 0.63))
  AddOrnament('E', (0.67, 0.50))
  AddOrnament('F', (0.17, 0.80))
  AddOrnament('G', (0.34, 0.74))
  AddOrnament('J', (0.66, 0.57))
  AddOrnament('L', (0.30, 0.64))
  AddOrnament('M', (0.65, 0.72))
  AddOrnament('N', (0.55, 0.30))
  AddOrnament('Q', (0.61, 0.70))
  AddOrnament('R', (0.32, 0.45))
  AddOrnament('S', (0.41, 0.22))
  AddOrnament('Z', (0.50, 0.17))
  AddOrnament('1', (0.43, 0.1))
  AddOrnament('2', (0.26, 0.53))
  AddOrnament('3', (0.66, 0.71))
  AddOrnament('4', (0.55, 0.70))
  AddOrnament('5', (0.44, 0.41))
  AddOrnament('6', (1, 0.25))
  AddOrnament('7', (0.40, 0.52))
  
  
  xmlstr = doc.toprettyxml()

  # drop the first line, the <?xml ...> bit.
  for line in xmlstr.splitlines(True)[1:]:
    sys.stdout.write(line)
  

if __name__ == '__main__':
  main()
