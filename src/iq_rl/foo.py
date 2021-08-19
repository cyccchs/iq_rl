#!/usr/bin/env python

from iq_gnc.py_gnc_functions import *
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import rospy

class LaserProcNode:
    def __init__(self, topic_name='/spur/laser/scan'):
        rospy.init_node('LaserProc', anonymous=True)
        self.topicName = topic_name
        self.laserData = LaserScan()
        self.dist = []
        rospy.Subscriber(self.topicName, LaserScan, self.callback)
    
    def bdCheck(self, i):
        if self.laserData.ranges[i] >30:
            self.dist.append(30)
        elif self.laserData.ranges[i] < 0.11:
            self.dist.append(0.1)
        else:
            self.dist.append(self.laserData.ranges[i])
    
    def callback(self, data):
        rangeSum = [0,0,0,0,0,0,0,0]
        self.laserData = data
        self.dist = []
        for i in range(0,1024):
            self.bdCheck(i)
            if i <64 or i>=960:
                rangeSum[0] = rangeSum[0] + self.dist[i]
            elif i >=64 and i<128:
                rangeSum[1] = rangeSum[1] + self.dist[i]
            else:
                print(i%128)
                #rangeSum[i%128] = rangeSum[i%128] + self.dist[i]
#        for i in rangeSum:
 #           print (i, end=' ')
        print("")


def foo_fun():    
    print("now executing foo_fun")

def main():
    print ("now executing main() in foo.py ")
    foo_fun()

