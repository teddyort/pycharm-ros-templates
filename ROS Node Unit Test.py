#!/usr/bin/env python
import rospy
import unittest
import rostest

class $TestClassName(unittest.TestCase):
               
    def setup(self):
        # Setup the node
        rospy.init_node('$test_name', anonymous=False)
        self.msg_received = False
        
        # Setup the publisher and subscriber
        self.pub  = rospy.Publisher("~<<topic>>", <<Type>>, queue_size=1, latch=True)
        self.sub = rospy.Subscriber( "~<<topic>>", <<Type>>, self.<<Callback>>)

        # Wait for the node  to finish starting up
        timeout = rospy.Time.now() + rospy.Duration(5) # Wait at most 5 seconds for the node to come up
        while (self.pub.get_num_connections() < 1 or self.sub.get_num_connections() < 1) and \
                not rospy.is_shutdown() and rospy.Time.now() < timeout:
            rospy.sleep(0.1)

    def test_publishers_and_subscribers(self):
        self.setup()    # Setup the node
        self.assertGreaterEqual(self.pub.get_num_connections(), 1, "No connections found on <<topic>> topic")
        self.assertGreaterEqual(self.sub.get_num_connections(), 1, "No connections found on <<topic>> topic")
        
if __name__ == '__main__':
    rostest.rosrun('$package_name', '$test_name', $TestClassName)
