#!/usr/bin/env python
import rospy


class $NodeName(object):
    """$NodeName
    Author: Teddy Ort
    Inputs:
    Outputs:
    """

    def __init__(self):
        """Initializes the node"""
        self.node_name = rospy.get_name()

        # Get parameters
        self.param_name = rospy.get_param("~<param_name>", '<default value>')

        self.loginfo("has started")

    def loginfo(self, msg):
        rospy.loginfo("[%s] %s", self.node_name, msg)


if __name__ == '__main__':
    rospy.init_node('$node_name', anonymous=False)
    $node_name = $NodeName()
    rospy.spin()
