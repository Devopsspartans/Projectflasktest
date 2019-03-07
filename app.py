from flask import Flask,request,render_template
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Course')

app = Flask(__name__)


@app.route('/')
def index_template():
  return render_template("newindex.html")

@app.route('/index_template')
def index_template1():
  return render_template("indexhome.html")

@app.route('/gcp_course')
def selction_course():
    pass

@app.route('/aws_course')
def selction_aws():
    response1 = table.query(
    KeyConditionExpression = Key('Platform').eq('AWS')
)
    response = response1['Items']
    return render_template("aws_template.html", response=response)





if __name__ == '__main__':
  app.run(port=80,debug=True)
