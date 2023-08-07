
# YAML Validator

This project provides a web interface and API to validate YAML files for proper formatting and structure.

## Features

- **Web Interface**: Paste YAML content directly and validate its structure.
- **API Endpoint**: Programmatic access to validate YAML files.
- **Instant Feedback**: Immediate results with clear indications for valid or invalid YAML.
- **Docker and Kubernetes Deployments**: Multiple deployment options to cater to different environments.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- PyYAML

### Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/yaml-validator.git
    cd yaml-validator
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**

    ```bash
    python app.py
    ```

   Once running, the application will be accessible at [http://0.0.0.0:5000](http://0.0.0.0:5000).

## Usage

### Web Interface

- **Validate YAML**: Paste your YAML content into the provided text area and click "Validate" to check its structure.
- **Instant Feedback**: Get immediate results showing whether the YAML is valid or not.

### API

You can also validate YAML files programmatically via the API.

#### Validate YAML File

- **Endpoint**: `/validate`
- **Method**: POST
- **Request Data**: Attach the YAML file with the key "file".

- **Response**: A string message indicating "Valid YAML" or "Invalid YAML".

- **Example cURL Command**:

    ```bash
    curl -F "file=@path/to/yourfile.yaml" http://0.0.0.0:5000/validate
    ```

## Contributing

For those interested in contributing, please fork the project, create a feature branch, and then submit a pull request once your changes are complete.

## License

This project is licensed under the MIT License.

## Acknowledgements

