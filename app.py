from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/arsenal')
def arsenal():
    return render_template('arsenal.html')

@app.route('/category')
def category():
    return render_template('category.html')
    
@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/discuss')
def discuss():
    return render_template('discuss.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
