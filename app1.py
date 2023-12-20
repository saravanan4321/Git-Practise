from flask import Flask, request
obj=Flask(__name__)
@obj.route('/')
def welcome():
    return "Welcome to my new page"

@obj.route('/mark', methods=["GET"])
def mark_total():
    ops=request.json["ops"]
    number1=request.json["number1"]
    number2=request.json['number2']
    
    if ops=="Total":
        result=int(number1)+int(number2)
    else:
        if ops=="Average":
            result=int(number1)+int(number2)/2
    
    return "the operation is {} and the result is {}". format(ops,result) 
print(__name__)
if __name__=="__main__":
    obj.run()