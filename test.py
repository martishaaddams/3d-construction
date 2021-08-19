# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:49:05 2021

@author: Marisha
"""  

import myclasses

 
Vertex1=myclasses._vertex(0,0,0)
Vertex2=myclasses._vertex(1,1,0)
Vertex3=myclasses._vertex(2,0,0)
Vertex4=myclasses._vertex(1,-1,0)
Line1=myclasses._line(Vertex1,Vertex2)

Line2=myclasses._line(Vertex2,Vertex3)
Line1.print()
Line2.print()
Line3=myclasses._line(Vertex3,Vertex4)
Line3.print()
Line4=myclasses._line(Vertex4,Vertex1)
Line4.print()
Surface1=myclasses._surface()
Surface1.add_line(Line1)
Surface1.add_line(Line2)
Surface1.add_line(Line3)
Surface1.add_line(Line4)
Surface1.print()