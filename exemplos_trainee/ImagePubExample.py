#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

import cv2
from cv_bridge import CvBridge

from sensor_msgs.msg import Image


class CvImagePublisher(Node):
    def __init__(self):
        super().__init__('cv_image_publisher')

        self.publisher_ = self.create_publisher(
            Image,
            '/camera/image_raw',
            10
        )

        self.timer = self.create_timer(1.0 / 30.0, self.timer_callback)
        self.bridge = CvBridge()

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            self.get_logger().error('Could not open video device')
        else:
            self.get_logger().info('Camera opened successfully')

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn('Frame capture failed')
            return

        msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'camera_frame'

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CvImagePublisher()
    rclpy.spin(node)

    node.cap.release()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
