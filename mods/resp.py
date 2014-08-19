from flask import make_response
import flask
import os

#print os.path.dirname(os.path.abspath(__file__))
#print os.getcwd()
#print os.path.abspath(__file__)

def render_template1(file):
	app_path = os.path.dirname(os.getcwd())
	temp_dir = app_path+"/flask contact/static/templates/"
	print temp_dir
	return make_response(open(temp_dir+file).read())