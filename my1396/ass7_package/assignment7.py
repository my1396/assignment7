'''
Created on Nov 3, 2015

@author: ds-ga-1007
'''
from ass7_package.Question1 import Question1st 
q1=Question1st()
print "----answers of Quesiton1-----"
print q1
print "The 2nd and 4th rows are:\n", q1.first()
print "The 2nd colomn is:\n", q1.second()
print "The chosen rectangular section is:\n",q1.third()
print "Elements belong to [3,11]:\n",q1.forth()

from question2 import Q2
q2=Q2()
print "\n\n----answers of Quesiton2-----"
print q2.divide_col_elewise()

from question3 import Q3
q3=Q3()
print "\n\n----answers of Quesiton3-----"
print "The original array is\n",q3.a
print "The number closest to 0.5 in each row:\n", q3.pick()

from quesiton4 import *
Q4()




