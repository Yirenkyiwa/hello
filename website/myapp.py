from flask import *
import json
app = Flask(__name__)
items = []
@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html',to=name)

@app.route('/')
def index():
    return render_template('index.html',items=items)


@app.route('/add_todo')
def add_todo():
    item=request.args.get("item")
    dd=request.args.get("date")
    answer= item + "<br>" + dd
    items.append(item)
    return answer
    return redirect("http://localhost:5000/", code=302)

@app.route('/get_todos')
def get_todos():
    resp=Response(json.dumps(getlist))
    resp.header['Content-Type']='application/json'
    return resp

 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
