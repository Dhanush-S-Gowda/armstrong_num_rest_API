from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def greet():
    return "welcome to armstrong number api"

@app.route('/<int:n>')
def armstorng_num(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum+= digit **order
        n = n//10
    
    if(sum == copy_n):
        result = {
            "number": copy_n,
            "is Armstrong": True
        }
    else:
        result = {
            "number": copy_n,
            "is Armstrong": False
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
