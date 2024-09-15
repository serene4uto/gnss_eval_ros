from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    params_file_path = get_package_share_directory('gnss_eval_ros') + '/params/gnss_eval_params.yaml'

    return LaunchDescription([

        # Declare the parameter file argument
        DeclareLaunchArgument(
            'params_file',
            default_value=params_file_path,
            description='Path to the YAML file containing the evaluation parameters'
        ),

        # GNSS evaluation node
        Node(
            package='gnss_eval_ros',
            executable='gnss_eval',
            name='gnss_eval',
            parameters=[LaunchConfiguration('params_file')],
            remappings=[('/fix', '/esp_gnss_demo/fix')]
        ),
    ])
