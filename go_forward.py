# First, import the necessary modules
import rospy
from geometry_msgs.msg import Twist

# Next, create a function that will be used to publish the command
def move_forward():
    # Initialize a publisher for the cmd_vel topic with a queue size of 10
    vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    # Initialize a ROS node with the name "move_forward"
    rospy.init_node('move_forward', anonymous=True)
    # Set the publish rate at 10 Hz
    rate = rospy.Rate(10)
    
    # Create a Twist message to hold the velocity command
    vel_cmd = Twist()
    
    # Set the linear velocity in the x-axis to 1 m/s
    vel_cmd.linear.x = 1.0
    # Set the angular velocity in the z-axis to 0 rad/s
    vel_cmd.angular.z = 0.0
    
    # Publish the velocity command until the node is shutdown
    while not rospy.is_shutdown():
        vel_pub.publish(vel_cmd)
        rate.sleep()

# Finally, call the move_forward function when the script is run
if __name__ == '__main__':
    try:
        move_forward()
    except rospy.ROSInterruptException:
        pass