from unittest import result
from flask import Flask, jsonify
import math
import random

from flask import Flask

app = Flask(__name__)

@app.get("/")

def generateOTP() :
    digits = "0123456789"
    OTP = ""

    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]

        result = {
                "OTP": OTP,
                "Success": True
            }
            
    return jsonify(result)

if __name__ == "__main__" :
    app.run(debug=True)
