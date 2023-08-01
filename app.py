from flask import Flask, render_template, request
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        yaml_content = request.form.get('yaml_content')
        try:
            data = yaml.safe_load(yaml_content)
            return render_template('index.html', result='Valid YAML', color='green')
        except Exception as e:
            return render_template('index.html', result='Invalid YAML', color='red')
    return render_template('index.html', result='', color='black')

if __name__ == '__main__':
    app.run(debug=True)
