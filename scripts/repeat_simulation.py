#!/usr/bin/env python
# coding: utf-8
import roslaunch
import rospy
from std_srvs.srv import Empty

uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)

cli_args1 = ['multi_legged_gazebo', 'multi_legged_world.launch']
cli_args2 = ['multi_legged_control', 'multi_legged_control.launch']
cli_args3 = ['multi_legged_walk', 'simple_walk.launch']
roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(cli_args1)[0]
roslaunch_file2 = roslaunch.rlutil.resolve_launch_arguments(cli_args2)[0]
roslaunch_file3 = roslaunch.rlutil.resolve_launch_arguments(cli_args3)[0]
launch_files = [roslaunch_file1, roslaunch_file2, roslaunch_file3]

while not rospy.is_shutdown():
    parent = roslaunch.parent.ROSLaunchParent(uuid, launch_files)

    parent.start()
    rospy.loginfo("started")

    rospy.init_node('reset_world')

    while not rospy.is_shutdown():
        rospy.loginfo("loop now")
        rospy.sleep(10)
        rospy.wait_for_service('/gazebo/reset_world')
        reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)
        reset_world()

    parent.shutdown()
    rospy.loginfo("killed")
    rospy.sleep(30)