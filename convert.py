#!/usr/bin/env python
# -*- coding=utf8 -*-
from Stack import Stack
    
def convert(infix):
  '''
    convert infix to postfix with variables(single char)
  '''
  stack = Stack()
  res = []
  for c in infix:
    if c == ' ':
      continue
    if c in ('+', '-'):
      if (not stack.empty()) and stack.peek() in ('*', '/', '%'):
        while not stack.empty():
          s = stack.peek()
          if s == '(':
            break
          res.append(s)
          stack.pop()
      stack.push(c)
    elif c in ('*', '/', '%'):
      while not stack.empty():
        s = stack.peek()
        if s not in ('*', '/', '%'):
          break
        res.append(s)
        stack.pop()
      stack.push(c)
    elif c == '(':
      stack.push(c)
    elif c == ')':
      while not stack.empty():
        s = stack.pop()
        if s == '(':
          break
        res.append(s)
    else:
      res.append(c)
      
  while not stack.empty():
    res.append(stack.pop())
  return res

def convert_num(infix):
  '''
    convert infix to postfix with numbers
  '''
  stack = Stack()
  res = []
  num = 0
  flag = False
  for c in infix:
    if c == ' ':
      continue
    if c.isdigit():
      num *= 10
      num += int(c)
      flag = True
      continue
    
    if flag:
      res.append(str(num))
      num = 0
    flag = False

    if c in ('+', '-'):
      if (not stack.empty()) and stack.peek() in ('*', '/', '%'):
        while not stack.empty():
          s = stack.peek()
          if s == '(':
            break
          res.append(s)
          stack.pop()
      stack.push(c)
    elif c in ('*', '/', '%'):
      while not stack.empty():
        s = stack.peek()
        if s not in ('*', '/', '%'):
          break
        res.append(s)
        stack.pop()
      stack.push(c)
    elif c == '(':
      stack.push(c)
    elif c == ')':
      while not stack.empty():
        s = stack.pop()
        if s == '(':
          break
        res.append(s)
    ## print c, stack.stack ##
      
  if flag:
    res.append(str(num))
  while not stack.empty():
    res.append(stack.pop())
  return res

def eval_infix(infix, scope={}):
  return eval(infix, scope)

def eval_postfix(postfix, scope={}):
  '''
    eval postfix expression result
    postfix is a list, the result of convert function
  '''
  stack = Stack()

  for c in postfix:
    if c not in ('+', '-', '*', '/', '%'):
      stack.push(c)
      continue

    op1 = 0
    op2 = 0
    if not stack.empty():
      op2 = stack.pop()
    if not stack.empty():
      op1 = stack.pop()
    ##print op1, c, op2
    res = eval(str(op1) + c + str(op2), scope)
    stack.push(res)

  return stack.pop()

def test(infix, func=convert_num):
  scope = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}

  if isinstance(infix, (list, tuple)):
    infix = ' '.join(infix)
  infix_res = eval_infix(infix, scope)
  print 'infix:   ', infix, '=', infix_res

  postfix = func(infix)
  res = eval_postfix(postfix, scope)

  print 'postfix: ', ' '.join(postfix), ' = ', res
  #assert res == infix_res
  return res

if __name__ == '__main__':
  test('a + b * c + (d / e + f) * g', convert)
  test(['a', '+', 'b', '%', 'c', '-', '(', 'd', '/', 'e', '-', 'f', ')', '*', 'g'], convert)
  test(('a', '+', 'b', '/', 'c', '+', '(', 'd', '%', 'e', '+', 'f', ')', '*', 'g'), convert)

  test('12 + 5 * (9 - 8) / 3 + 5 * 3 % 4 + 0')
  test('12 + 5 * (-8 + 7) / 3 + 5 * 3 % 4 + 0')
  test('-5 * 3 / 4 + 0')
  test('-5 * -4')
  test('+5 * +4')

  assert test('-5 * 3 / 4') == -3
  assert test('5 * 3 / 4') == 3
  assert test('5 / 3 * 4') == 4
  assert test('5 * 3 % 4') == 3
  assert test('5 % 3 * 4') == 8
  assert test('5 * 3 / 4 % 2') == 1
  assert test('5 * ( 5 / 2)') == 10
  assert test('5 / ( 7 - 9)') == -3