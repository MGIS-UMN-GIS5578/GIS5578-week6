# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:31:57 2019

@author: dahaynes
"""

class point(object):
    
    def __init__(self,theX,theY,theValue=0):
        self.x = theX
        self.y = theY
        self.value = theValue
    
    def __str__(self,):
        """
        prints the following statement
        """
        return("The X value is {} and the Y value is {}".format(self.x, self.y) )

class line(point):
    def __init__(self,start,end):
        
        for p in [start,end]:
            if isinstance(p, point):
                if isinstance(p.x, int) and isinstance(p.y, int):
                    flag = 1
                else:
                    flag = 0
                    print("Not a valid point")
                    
        if flag:                    
            self.start = start
            self.end = end
            self.length = self.calculate_length()
        else:
            raise Exception(ValueError)
            self.__del__()
        
    def __del__(self):
        """
        
        """
        print("not a valid point")
        
    def calculate_length(self):
        """
        We are using the Pythagorems thereom
        
        """
        length = ((self.end.x -self.start.x)**2 + (self.end.y - self.start.y)**2)**.5
        return length
    
class triangle(line):
    
    def __init__(self, line1, line2, line3):
        self.perimeter = self.calculate_perimeter(line1,line2,line3)
        
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
    
        self.area = self.calculate_area()
        #Needs self.line1,self.line2, self.line3
        
    def calculate_area(self,):
        """
        """
        newList = []
        for phone in [self.line1, self.line2, self.line3]:
            for thePoint in [phone.start, phone.end]:
                print(thePoint.x, thePoint.y)
                newList.append( (thePoint.x, thePoint.y) )
        
        a, b, c = set(newList)
        
        area = abs ( a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]) ) / 2
        
        return(area)
    
    def calculate_perimeter(self, l1,l2,l3):
        """
        
        """
        summingPerimeterVariable = 0
        #We are expecting lvariables to be line objects.
        for x in [l1, l2, l3]:
            newLineVar = line(x.start, x.end)
            #print(newLineVar.length)
            summingPerimeterVariable += newLineVar.length
        return summingPerimeterVariable
        
        
#        l11 = line(l1.start, l1.end)
#        l22 = line(l2.start, l2.end)
#        l33 = line(l3.start, l3.end)
#        
#        print(l.length)
    
    
    
    
    
    
    
        