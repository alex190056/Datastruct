import unittest
from utils.utils import Stack
from utils.queue import Queue


class TestNode(unittest.TestCase):

    def test_Stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.pop(), 'data2')

    def test_Queue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
