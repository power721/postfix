# -*- coding=utf8 -*-

class Stack:
  def __init__(self):
    self.stack = []
    self.top = 0
  
  def push(self, item):
    self.stack.append(item)
    self.top += 1

  def pop(self):
    if self.top == 0:
      raise ValueError('stack is empty')
    self.top -= 1
    res = self.stack[self.top]
    del self.stack[self.top]
    return res
  
  def peek(self):
    if self.top == 0:
      raise ValueError('stack is empty')
    return self.stack[self.top - 1]
  
  def empty(self):
    return self.top == 0
    