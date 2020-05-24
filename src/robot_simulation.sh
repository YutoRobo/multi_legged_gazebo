#!/bin/bash

while :
do
roslaunch multi_legged_gazebo multi_legged_world.launch&
sleep 10s
roslaunch multi_legged_control multi_legged_control.launch&
sleep 5s
done
#roslaunch multi_legged_control multi_legged_control.launch&
#while :
#do
  #echo "kill gazebo process"
  #roslaunch multi_legged_gazebo kill_gazebo_process.launch
  #sleep 10s
  #echo "spawn_model"
  #roslaunch multi_legged_gazebo respawn_robot_model.launch
  #sleep 10s
  #echo "spawn_controller"
  #roslaunch multi_legged_control respawn_controller.launch&
  #sleep 10s
#done
