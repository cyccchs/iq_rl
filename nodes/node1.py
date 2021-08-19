#!/usr/bin/env python

from iq_gnc.py_gnc_functions import *
import rospy
from iq_rl import *

if __name__ == '__main__':
    main()
    LaserProcNode()
    rospy.spin()
