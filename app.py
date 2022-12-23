#python file
# create a flask app
from flask import Flask, render_template
app = Flask(__name__)

# create a route
@app.route('/')
def hello_world():
    return render_template('index.html')

# create a new route for cpu information
@app.route('/api/cpu')

def api():
    #return as string cpu percent and cpu count
    import psutil
    cpu_percent = psutil.cpu_percent(interval=0.1)
    cpu_count = psutil.cpu_count()
    return f'from app.py CPU percent: {cpu_percent}%, CPU count: {cpu_count}'





# run the app
if __name__ == '__main__':
    app.run(debug=True)
