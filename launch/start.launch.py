from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import os
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    parameter = os.path.join(get_package_share_directory('__TEMPLATE_PACKAGE'), 'config', 'params.yaml')

    converter_node = Node(
        package='__TEMPLATE_PACKAGE',
        executable='__TEMPLATE_EXEC_NAME',
        name='__TEMPLATE_NODE_NAME',
        output='screen',
        parameters=[parameter]
    )


    ld.add_action(converter_node)

    return ld