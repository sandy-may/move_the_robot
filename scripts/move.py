#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped

def move():
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.init_node('move', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        movePose = PoseStamped()
        movePose.header.frame_id = '/map'
        movePose.pose.position.x = 0.0
        movePose.pose.position.y = 0.0
        movePose.pose.position.z = 0.0
        movePose.pose.orientation.x = 0.0
        movePose.pose.orientation.y = 0.0
        movePose.pose.orientation.z = 0.0
        movePose.pose.orientation.w = 1.0
        
        rospy.loginfo(movePose)
        pub.publish(movePose)
        r.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
