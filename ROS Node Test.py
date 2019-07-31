#!/usr/bin/env python
import rospy
import unittest
import rostest

class $TestClassName(unittest.TestCase):
               
    def setUp(self):
        # Setup the node
        rospy.init_node('$test_name', anonymous=False)
        self.msg_received = False
        
        # Setup the publisher and subscriber
        self.pub  = rospy.Publisher("~<<topic>>", <<Type>>, queue_size=1, latch=True)
        self.sub = rospy.Subscriber( "~<<topic>>", <<Type>>, self.<<Callback>>)

        # Wait for the node  to finish starting up
        self.do_until_timeout(lambda: self.sub.get_num_connections() > 0 
                    and self.pub.get_num_connections() > 0)

    def test_publishers_and_subscribers(self):
        pass

    def callback(self, msg):
        self.msg_received = True
        
    def do_until_timeout(self, condition, msg='Test timed out', action=None, timeout=5, hz=10):
        # Wait for the condition or until the timeout passes
        rate = rospy.Rate(hz)
        timeout = rospy.Time.now() + rospy.Duration(timeout)
        while not condition() and not rospy.is_shutdown() and rospy.Time.now() < timeout:
            if action is not None:
                action()
            rate.sleep()
        self.assertLess(rospy.Time.now(), timeout, msg)
        
if __name__ == '__main__':
    rostest.rosrun('$package_name', '$test_name', $TestClassName)
