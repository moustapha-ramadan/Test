#!/usr/bin/env python

def add(num1,num2):
	print("%s+%s=%s"%(num1,num2,num1+num2))
	return num1+num2

def sub(num1,num2):
	print("%s+%s=%s"%(num1,num2,num1-num2))
	return num1-num2

if __name__=='__main__':
	sub(add(2,6),sub(3,1))

