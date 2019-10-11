# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:51:56 2019

@author: dahaynes
"""

import gis


p1 = gis.point(0,5)
p2 = gis.point(0,0)
p3 = gis.point(3,3)

p3 = gis.point("David", "Haynes")

theLine = gis.line(p1,p2)
theLine2 = gis.line(p1,p3)
theLine3 = gis.line(p2,p3)

triangle = gis.triangle(theLine, theLine2, theLine3)
allPoints = triangle.calculate_area()
#listOfPoints = [gis.point(i, i-1) for i in range(1,100)]
#
#listOfPoints = []
#for i in range(1,100):
#    listOfPoints.append(gis.point(i,i-1))