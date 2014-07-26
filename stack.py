# -*- coding=utf8 -*-

class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if not len(self.stack):
      raise ValueError('stack is empty')
    return self.stack.pop()
  
  def peek(self):
    if not len(self.stack):
      raise ValueError('stack is empty')
    return self.stack[-1]
  
  def empty(self):
    return len(self.stack) == 0
    