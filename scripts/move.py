#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped

def talker():
    pub = rospy.Publisher('movePose', PoseStamped, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        movePose = PoseStamped()
        movePose.header.frame_id = '/map'
        movePose.pose.position.x = 1.0
        movePose.pose.position.y = 1.0
        movePose.pose.orientation.w = 1.0
        rospy.loginfo(movePose)
        pub.publish(movePose)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
