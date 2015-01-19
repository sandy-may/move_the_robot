#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseActionResult

flag = False

def move(x, y):
    while not flag:
        pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    
        r = rospy.Rate(10) #10hz
    
        movePose = PoseStamped()
        movePose.header.frame_id = '/map'
        movePose.pose.position.x = x
        movePose.pose.position.y = y
        movePose.pose.position.z = 0.0
        movePose.pose.orientation.x = 0.0
        movePose.pose.orientation.y = 0.0
        movePose.pose.orientation.z = 0.0
        movePose.pose.orientation.w = 1.0
    
        rospy.loginfo(movePose)
        pub.publish(movePose)
        r.sleep()
        
        listener()
    
#listener to subscribe to move_baser/result
def listener():
        rospy.Subscriber("/move_base/result", MoveBaseActionResult, callback)
    
#check to see if status == 3 if true goal has been reached
def callback(msg):
    if msg.status.status == 3:
        global flag 
        flag = True
    
#moving the robot function
def link():
   
    rospy.init_node('link', anonymous=True)
   
    while not rospy.is_shutdown():
       
        move(0, 0)

        if flag:
            break

if __name__ == '__main__':
    try:
        link()
    except rospy.ROSInterruptException: pass
