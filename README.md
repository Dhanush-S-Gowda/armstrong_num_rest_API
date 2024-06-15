# Armstrong Number API

Welcome to the Armstrong Number API! This simple Flask-based API allows you to check if a given number is an Armstrong number.

## Overview

An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because \(1^3 + 5^3 + 3^3 = 153\).

## Features

- **Check Armstrong Number**: Determine if a given integer is an Armstrong number.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. You'll also need `Flask`, which can be installed using pip:

```bash
pip install Flask
```
### Running the API

- Clone the repository:
```bash
git clone https://github.com/yourusername/armstrong-number-api.git
cd armstrong-number-api
```

- Run the Flask application:
```bash
python app.py
```

- By default, the application will run on http://127.0.0.1:5000/  or https://armstrong-num-rest-api.onrender.com/.

## API Endpoints

### Welcome Message

- URL: /
- Method: GET
- Description: Returns a welcome message.

#### Response

```text
welcome to armstrong number api
```

### Check Armstrong Number

- URL: /<int:n>
- Method: GET
- Description: Check if the provided number n is an Armstrong number.

#### URL Parameters

- n (integer): The number to be checked.
- 
#### Response

- Content-Type: application/json

- Example Response:

If the number is an Armstrong number:
```json
{
  "number": 153,
  "is Armstrong": true
}
```

If the number is not an Armstrong number:
```json
{
  "number": 123,
  "is Armstrong": false
}
```
