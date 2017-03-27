#!/usr/bin/env python
import rospy

# $node_name
# Author: Teddy Ort
# Inputs: 
# Outputs: 

class $NodeName(object):
    def __init__(self):
        self.node_name = '$node_name'
        self.param_name     = self.setupParam("~<param_name>", '<default value>')

        rospy.loginfo("[%s] has started", self.node_name)

    def setupParam(self,param_name,default_value):
        value = rospy.get_param(param_name,default_value)
        rospy.set_param(param_name,value) #Write to parameter server for transparancy
        rospy.loginfo("[%s] %s = %s " %(self.node_name,param_name,value))
        return value

if __name__ == '__main__':
    rospy.init_node('$node_name', anonymous=False)
    $node_name = $NodeName()
    rospy.spin()