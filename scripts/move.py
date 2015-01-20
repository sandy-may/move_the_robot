#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseActionResult

flag = False
#move function accepts x and y coordinate
def move(x, y):
    while not flag:
        #create a move base publisher
        pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    
        r = rospy.Rate(10) #10hz
        #create a PoseStamped object and pass values
        movePose = PoseStamped()
        movePose.header.frame_id = '/map' #set map as frame id
        movePose.pose.position.x = x
        movePose.pose.position.y = y
        movePose.pose.position.z = 0.0
        movePose.pose.orientation.x = 0.0
        movePose.pose.orientation.y = 0.0
        movePose.pose.orientation.z = 0.0
        movePose.pose.orientation.w = 1.0
    
        rospy.loginfo(movePose) #pass info to terminal
        pub.publish(movePose) #pass info to any subscribers
        r.sleep()
        
        listener()#call listener
    
#listener to subscribe to move_baser/result
def listener():
        rospy.Subscriber("/move_base/result", MoveBaseActionResult, callback)
    
#check to see if status == 3 if true goal has been reached
def callback(msg):
    if msg.status.status == 3:
        global flag 
        flag = True
    
#main function function
def corridor():
   
    rospy.init_node('link', anonymous=True)
   
    while not rospy.is_shutdown():
       
        move(-2.5, 0.0)

        global flag
        flag = False
        
        move(-2.0, 0.0)
        flag = False
        
        move(1.5, 0.0)
        flag = False
       
        #move 1.5 meteres forward
        move(-1.0, 0.0)
        flag = False
        
        move(-0.5, 0.66)
        flag = False
        
        move(0.0, 1.33)
        flag = False
        #move 1.5 meteres forward and 2 meteres left diagonally
        move(0.5, 2.0)
        
        flag = False
        #move 1.5 meteres forward and 2 meteres right diagonally
        move(2.0, 0.0)
        
        if flag:
            break

if __name__ == '__main__':
    try:
        corridor()
    except rospy.ROSInterruptException: pass
