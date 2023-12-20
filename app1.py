from flask import Flask, request
obj=Flask(__name__)
@obj.route('/')
def welcome():
    return "Welcome to my new page"

@obj.route('/mark', methods=["GET"])
def mark_total():
    ops=request.json["ops"]
    tamil=request.json["Tamil"]
    english=request.json['English']
    maths=request.json['Maths']
    science=request.json['Science']
    social=request.json['Social']

    
    if ops=="Total":
        result=int(tamil)+int(english)+int(maths)+int(science)+int(social)
    else:
        if ops=="Average":
            result=(int(tamil)+int(english)+int(maths)+int(science)+int(social))/5
    
    return "the operation is {} and the result is {}". format(ops,result) 
print(__name__)
if __name__=="__main__":
    obj.run()