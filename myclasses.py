# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:28:02 2021

@author: Marisha
"""

class _vertex:
    _x=None
    _y=None
    _z=None
    is_free=True
    def __init__(self, x, y, z):
        self._x=x
        self._y=y
        self._z=z
    def print(self):
        print("({}, {}, {})".format(self._x, self._y, self._z))
    
    def  get(self):
        return "({}, {}, {})".format(self._x, self._y, self._z)
    
    def __eq__(self,other):
        
        if(self._x==other._x):
            if(self._y==other._y):
                if(self._z==other._z):
                    return True
        return False
            
class _line:
    _vertex_start=None
    _vertex_end=None
    def __init__(self, vertex_0, vertex_1):
        self._vertex_start = vertex_0
        self._vertex_end = vertex_1
    def __eq__(self, other):
        if (self._vertex_start==other._vertex_start):
            if(self._vertex_end==other._vertex_end):
                return True
        return False
    def get_start(self):
        return self._vertex_start
    def get_end(self):
        return self._vertex_end
    def print(self):
        print("start: {}".format(self._vertex_start.get()))
        print("end: {}".format(self._vertex_end.get()))
    
class _surface:
    #получилась ориентированная поверхность
    border_lines=[]
    _is_connected=False
    
    def if_connected(self):
        start=self.border_lines.get_start()
        if start is None:
            print("no surface")
        else:
            for i in self.border_lines:
                current_vertex=i.get_start
                next_vertex=i.get_end
                if (next_vertex==start):
                    print("connected")
                    self._is_connected=True
    
    def _add_line(self,line):
        self.border_lines.append(line)
    
    def add_line(self,line):
        if self._is_connected:
            print("already connected no need in this")
        else:
            if self.border_lines == []:
                    print("New surface")
                    self._add_line(line)
            
            #maybe there is a way to avoid it
            else:
                for i in self.border_lines:
                    end=i.get_end()
                    #print("current end: {}".format(end.get()))
                    if(i==line):
                        print("there already are this line")
                        break
                if end == line._vertex_start:
                    self._add_line(line)
                else:
                    if self.border_lines == []:
                        print("New surface")
                        self._add_line(line)
                    else:
                        print("Ending Vertex is not equal to starting") 
    
    def print(self):
        if self.border_lines == []:
            print("New surface")
        else:
            c=0
            for i in self.border_lines:
                c=c+1
                print("{}. {}".format(c,i._vertex_start.get()))
            
        