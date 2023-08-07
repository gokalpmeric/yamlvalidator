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

@app.route('/validate', methods=['POST'])
def validate_yaml():
    file = request.files.get('file')
    
    if file is None:
        return 'No file provided\n', 400

    yaml_content = file.read().decode('utf-8')

    try:
        yaml.safe_load(yaml_content)
        return 'Valid YAML\n', 200
    except Exception as e:
        return 'Invalid YAML\n', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
