'''
Created on 2015

@author: kaisquare
'''
from simple.SimpleDemo import CarSimple

class TestDemo():
    def setUp(self):
        print "setUp"


    def tearDown(self):
        
        print "tearDown"
    
    def __init__(self):
        self.a = 3
        self.b = 0
        pass
    
    def testDemoAdd(self):
        CarSimple()
        print "Add"
        assert self.a==3
    
    def testDemoUpdata(self):
        CarSimple()
        print "Updata"
        self.b = 2
        print self.b
        assert True
        
    def testDemoZelete(self):
        print "Delete"
        CarSimple()
        print self.b
        assert self.b==0
    
