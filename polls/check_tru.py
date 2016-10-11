import string
import sqlite3 as lite
from sympy.abc import x,y
from sympy import *  #for mathematical calculation
from exeCheckAnswer import StepChecking
from masCheckAnswer import MasStepChecking

con = lite.connect('db.sqlite3')

''' this is a intermediate class with the purpose of retreving the information on the working step answers and their relevant feedback with hints  '''

'''The function to clear all the whitespace from the user input'''
def preprocessInput(data_input):
	'''remove whitespace'''
	'''convert to lower case'''
	userInput = data_input.lower()
	userInput = userInput.replace(' ','')
	userInput = userInput.replace(',', '')
	# userInput = userInput.replace('(', '')
	# userInput = userInput.replace(')', '')
	print "user input after preprocess", userInput
	print "data type for user input after preprocess", type(userInput)
	return userInput
	
def checkworking(post_workingstep, skillid, exeQueNum, stepCount, workStepNo):
	raw_input = preprocessInput(post_workingstep)
	print workStepNo
	print type(workStepNo)
	c= StepChecking(raw_input, skillid, exeQueNum, stepCount, workStepNo)
	print "success in passing the parameter"
	getOutput1, getOutput2, getOutput3= c.intermediaGetValue()
	print "success"
	
	return getOutput1, getOutput2, getOutput3, raw_input


def mas_checkworking(mas_workingstep, skillid, masQueNum, stepCount, workStepNo):
	raw_input = preprocessInput(mas_workingstep)
	print workStepNo
	print type(workStepNo)
	mas = MasStepChecking(raw_input, skillid, masQueNum, stepCount, workStepNo)
	print "success in passing the parameter"
	get_masOutput1, get_masOutput2 = mas.intermediaGetValue()
	print "success"
	
	return get_masOutput1, get_masOutput2, raw_input



