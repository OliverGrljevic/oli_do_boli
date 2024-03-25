# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            '/broj',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Int32, '/kvadrat_broja', 10) # copy paste iz publshera, treba za echo
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        br = msg.data
        kbr = br**2
        kbr_msg = Int32()
        kbr_msg.data = kbr
        self.publisher_.publish(kbr_msg) # da i povuce gore publisher kad zovem echo
        # self.get_logger().info('data "%d"' % kbr)     s ovime sam radio da si mogu vizualizirati, a mi ne treba za zadacu


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
