from launch import LaunchDescription  
from launch_ros.actions import Node  
  
def generate_launch_description():  
    return LaunchDescription([  
        # 第一个静态变换  
        Node(  
            package='tf2_ros',  
            executable='static_transform_publisher',  
            name='static_transform_1',  
            arguments=['0', '0.7', '0.05', '0', '0', '0', 'fan1', 'buff_center'],  
            output='screen'  
        ),  
          
        # 第二个静态变换  
        Node(  
            package='tf2_ros',  
            executable='static_transform_publisher',  
            name='static_transform_2',  
            arguments=['-0.6657', '-0.2163', '-0.05', '-1.2566', '0', '0', 'buff_center', 'fan2'],  
            output='screen'  
        ),  
          
        Node(  
            package='tf2_ros',  
            executable='static_transform_publisher',  
            name='static_transform_3',  
            arguments=['-0.4114', '0.5663', '-0.05', '-2.5133', '0', '0', 'buff_center', 'fan3'],  
            output='screen'  
        ),  

        Node(  
            package='tf2_ros',  
            executable='static_transform_publisher',  
            name='static_transform_4',  
            arguments=['0.4114', '0.5663', '-0.05', '2.5133', '0', '0', 'buff_center', 'fan4'],  
            output='screen'  
        ),  

        Node(  
            package='tf2_ros',  
            executable='static_transform_publisher',  
            name='static_transform_5',  
            arguments=['0.6657', '-0.2163', '-0.05', '1.2566', '0', '0', 'buff_center', 'fan5'],  
            output='screen'  
        ), 
    ])