from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(package='signal_pipeline', executable='signal_pub', name='signal_pub',
             parameters=[{'frequency':1.0,'amplitude':1.0}]),
        Node(package='signal_pipeline', executable='rms_sub', name='rms_sub',
             parameters=[{'window':60}]),
    ])
