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

  def AddPolygon(points, style=None):
    polygon = minidom.Element('polygon')

    point_strings = [] 
    for point in points:
      point_strings.append('%f, %f' % point)

    points_string = ' '.join(point_strings)
    polygon.setAttribute('points', points_string)

    if style:
      polygon.setAttribute('style', style)
    tree.appendChild(polygon)

  # Add the trunk
  trunk_width = 0.13
  half_trunk_width = trunk_width / 2.0
  left = 0.5 - half_trunk_width
  right = 0.5 + half_trunk_width
  AddPolygon([
    (left, 0.5),
    (right, 0.5),
    (right, 1),            
    (left, 1)], 'fill:#855E42')

  
  def AddTriangle(top, bottom, width):
    points = [
      (0.5, top),
      (0.5 - (width / 2.0), bottom),
      (0.5 + (width / 2.0), bottom)]
    AddPolygon(points, 'fill:#006400')

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

    hanger = doc.createElement('polygon')

    offset = 0.048
    width = 0.012
    half_width = width / 2.0
    left, top = offset - half_width, 0.005 
    right, bottom = offset + half_width, 0.05
    hanger.setAttribute(
      'points',
      ('%f,%f %f,%f %f,%f %f,%f' %
       (left, top, right, top, right, bottom, left, bottom)))
    hanger.setAttribute('style', 'fill:#777')
    g.appendChild(hanger)
    

    bullet_size = 0.13
    bullet.setAttribute('width', str(bullet_size))
    bullet.setAttribute('height', str(bullet_size))
    bullet.setAttribute('viewBox', '0 0 100 100')    
    g.appendChild(bullet)

  AddOrnament('A', (0.5, 0.76))
  AddOrnament('B', (0.45, 0.32))
  AddOrnament('C', (0.32, 0.33))
  AddOrnament('D', (0.43, 0.66))
  AddOrnament('E', (0.58, 0.44))
  AddOrnament('F', (0.17, 0.78))
  AddOrnament('G', (0.34, 0.76))
  AddOrnament('J', (0.48, 0.54))
  AddOrnament('L', (0.23, 0.69))
  AddOrnament('M', (0.65, 0.70))
  AddOrnament('N', (0.55, 0.30))
  AddOrnament('Q', (0.61, 0.54))
  AddOrnament('R', (0.35, 0.49))
  AddOrnament('S', (0.41, 0.22))
  AddOrnament('Z', (0.50, 0.17))
  AddOrnament('1', (0.43, 0.1))
  AddOrnament('2', (0.26, 0.53))
  AddOrnament('3', (0.70, 0.78))
  AddOrnament('4', (0.55, 0.67))
  AddOrnament('5', (0.44, 0.43))
  AddOrnament('6', (1, 0.25))
  AddOrnament('7', (0.33, 0.63))
  
  
  xmlstr = doc.toprettyxml()

  # drop the first line, the <?xml ...> bit.
  for line in xmlstr.splitlines(True)[1:]:
    sys.stdout.write(line)
  

if __name__ == '__main__':
  main()
