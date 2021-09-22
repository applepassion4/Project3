from flask import app, render_template
from flask import Flask, jsonify, render_template
import pandas as pd
import plotly
import plotly.express as px
from pymongo import MongoClient
import json
app=Flask(__name__)


client = MongoClient('localhost', 27017)
db = client['project3']
collection = db['years']
@app.route('/')
@app.route('/index')
def index():
    name = 'Rosalia'
    data={}
    data["col"]=["2015-1016","2017-2018"]
    d = db['y2015_2016']
    group=d.find_one()
    
    data['group']=list(group.keys())[1:]

    data['range']=list(group[data['group'][0]].keys())
    
    return render_template('index.html', title='Welcome', username=name,data=data)

@app.route('/home')
def home():
    name = 'Rosalia'
    return render_template('home.html', title='Welcome', username=name)


@app.route('/dashboardbar/<query>')
def dashboardbar(query):
    q=query.split('<>')
    # print(q)
    data = db['y2015_2016']
    if '2015' in q[0]:
        data = db['y2015_2016']
    else:
        data= db['y2017_2018']
    one=data.find_one()
    group=list(one.keys())[1:]
    range_=list(one[group[0]].keys())
    labels=[]
    sizes=[]
    total=list(one[group[0]][range_[0]].keys())[0]
    group1={}
    for i in group:
        group1[i]=0
        for c in range_:
            group1[i]+=one[i][c][total]
    for i in group1:
        # sizes.append(one[i][range_[0]][total])
        sizes.append(group1[i])
    df=pd.DataFrame({"group":group,"total":sizes})
    
    fig=px.bar(x=group,y=sizes, title="Group Graph ",color_discrete_sequence=px.colors.sequential.RdBu)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    # return json.dumps({"graph":graphJSON})
    # import plotly.graph_objects as go
    # animals=['giraffes', 'orangutans', 'monkeys']
    # print(len(group),len(sizes))
    # fig = go.Figure([go.Bar(x=group, y=sizes)])
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
@app.route('/dashboardbar3/<query>')
def dashboardbar3(query):
    q=query.split('<>')
    # print(q)
    data = db['y2015_2016']
    if '2015' in q[0]:
        data = db['y2015_2016']
    else:
        data= db['y2017_2018']
    one=data.find_one()
    group=list(one.keys())[1:]
    range_=list(one[q[1]].keys())
    labels=[]
    sizes=[]

    sample=one[q[1]][q[2]]
    labels=[]
    sizes=[]
    dic={}
    for x, y in sample.items():
        if 'Total' in x:
            continue
        labels.append(x)
        sizes.append(y)
    df=pd.DataFrame({"location":labels,"value":sizes})
    fig=px.pie(df,values='value',names="location", title="Group Range Location Graph  ",color_discrete_sequence=px.colors.sequential.RdBu)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
    df=pd.DataFrame({"Range":range_,"total":sizes})
    
    
    fig=px.bar(x=range_,y=sizes, title="Group Graph ",color_discrete_sequence=px.colors.sequential.RdBu)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    # return json.dumps({"graph":graphJSON})
    # import plotly.graph_objects as go
    
    # print(len(group),len(sizes))
    # fig = go.Figure([go.Bar(x=group, y=sizes)])
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
# @app.route('/dashboardbar/<query>')
# def dashboardbar(query):
#     q=query.split('<>')
#     # print(q)
#     data = db['y2015_2016']
#     if '2015' in q[0]:
#         data = db['y2015_2016']
#     else:
#         data= db['y2017_2018']
#     one=data.find_one()
#     group=list(one.keys())[1:]
#     range_=list(one[group[0]].keys())
#     labels=[]
#     sizes=[]
#     total=list(one[group[0]][range_[0]].keys())[0]
#     group1={}
#     for i in group:
#         group1[i]=0
#         for c in range_:
#             group1[i]+=one[i][c][total]
#     for i in group1:
#         # sizes.append(one[i][range_[0]][total])
#         sizes.append(group1[i])
#     df=pd.DataFrame({"group":group,"total":sizes})
    
#     fig=px.bar(x=group,y=sizes, title="Group Graph ",color_discrete_sequence=px.colors.sequential.RdBu)
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     # return json.dumps({"graph":graphJSON})
#     import plotly.graph_objects as go
#     animals=['giraffes', 'orangutans', 'monkeys']
#     print(len(group),len(sizes))
#     fig = go.Figure([go.Bar(x=group, y=sizes)])
#     # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return graphJSON
@app.route('/dashboardbar2/<query>')
def dashboardbar2(query):
    q=query.split('<>')
    # print(q)
    data = db['y2015_2016']
    if '2015' in q[0]:
        data = db['y2015_2016']
    else:
        data= db['y2017_2018']
    one=data.find_one()
    group=list(one.keys())[1:]
    range_=list(one[q[1]].keys())
    labels=[]
    sizes=[]
    total=list(one[q[1]][range_[0]].keys())[0]
    group1={}
    for i in range_:
        group1[i]=one[q[1]][i][total]
    for i in group1:
        sizes.append(group1[i])
    df=pd.DataFrame({"Range":range_,"total":sizes})
    

    fig=px.bar(x=range_,y=sizes, title="Group Graph ",color_discrete_sequence=px.colors.sequential.RdBu)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    # return json.dumps({"graph":graphJSON})
    # import plotly.graph_objects as go
    
    # print(len(group),len(sizes))
    # fig = go.Figure([go.Bar(x=group, y=sizes)])
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/dashboard/<query>')
def dashboard(query):
    q=query.split('<>')
    # print(q)
    data = db['y2015_2016']
    if '2015' in q[0]:
        data = db['y2015_2016']
    else:
        data= db['y2017_2018']
    one=data.find_one()
    keys=list(one.keys())
    keys_child=list(one[keys[1]].keys())
    key=""
    # print(keys_child)
    for i in keys:
        if q[1] in i:
            key=i
            break
    sample=one[keys[1]][keys_child[0]]
    labels=[]
    sizes=[]
    dic={}
    for x, y in sample.items():
        if 'Total' in x:
            continue
        labels.append(x)
        sizes.append(y)

    df=pd.DataFrame({"location":labels,"value":sizes})
    fig=px.pie(df,values='value',names="location", title="Group Location Graph ",color_discrete_sequence=px.colors.sequential.RdBu)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    # return json.dumps({"graph":graphJSON})

    return graphJSON
@app.route('/dashboardgroup/<query>')
def dashboardgroup(query):
    q=query.split('<>')
    # print(q,query)
    data = db['y2015_2016']
    if '2015' in q[0]:
        data = db['y2015_2016']
    else:
        data= db['y2017_2018']
    d=data
    data={}
    one=d.find_one()
    group=d.find_one()
    
    data['group']=list(group.keys())[1:]

    data['range']=list(group[data['group'][0]].keys())
    print(data['group'],q)

    return json.dumps(data)
    
if __name__ == '__main__':
    app.run(debug=True)