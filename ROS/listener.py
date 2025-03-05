# ROS listener node that listens to the topic /chatter and prints the message to the console
import rospy
from std_msgs import *
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()


# The listener code is similar to the talker code, but instead of publishing a message, it subscribes to the topic /chatter and defines a callback function that prints the message to the console. The rospy.spin() function keeps the node running and listening for messages.
# To run the listener node, open a new terminal and run the following command:
# $ rosrun ROS listener.py
# You should see the listener node printing the messages published by the talker node to the console.
# Note: Make sure the talker node is running before starting the listener node, as the listener node needs to subscribe to the /chatter topic that the talker node publishes to.
# Conclusion
# In this tutorial, we learned how to create a simple publisher and subscriber node in ROS using Python. We created a talker node that publishes a message to the /chatter topic and a listener node that subscribes to the /chatter topic and prints the message to the console. These nodes demonstrate the basic concepts of ROS communication and can be used as building blocks for more complex ROS applications.
# For more information on ROS and its features, refer to the official ROS documentation and tutorials.
# References
# ROS Wiki: http://wiki.ros.org/
# ROS Tutorials: http://wiki.ros.org/ROS/Tutorials
# ROS Python Client Library: http://wiki.ros.org/rospy
# ROS Message Types: http://wiki.ros.org/Messages
# ROS Topics: http://wiki.ros.org/Topics
# ROS Services: http://wiki.ros.org/Services
# ROS Actions: http://wiki.ros.org/Actions
# ROS Parameters: http://wiki.ros.org/Parameter%20Server
# ROS Launch Files: http://wiki.ros.org/roslaunch
# ROS Nodes: http://wiki.ros.org/Nodes
# ROS Messages: http://wiki.ros.org/Messages
# ROS Services: http://wiki.ros.org/Services
