import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('__TEMPLATEPACKAGENAME__'),
        'params',
        'params.yaml'
        )
        
    node=Node(
        package = '__TEMPLATEPACKAGENAME__',
        name = '__TEMPLATENODENAME__',
        executable = '__TEMPLATEEXENAME__',
        parameters = [config]
    )

    ld.add_action(node)
    return ld