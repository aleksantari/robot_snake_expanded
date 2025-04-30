import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aleksantari/projects/snake_robot/ros2_ws/install/depth_anything_v2_ros2'
