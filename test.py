from flask import Flask
app = Flask('credit-card-app') # give an identity to your web service
@app.route('/ping',methods=['GET'])
def ping():
    return 'PONG'

if __name__=='__main__':
   app.run(debug=True, host='0.0.0.0', port=9696)