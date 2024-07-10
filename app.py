from flask import Flask, request
from kata04.converter_service import ConverterService

app = Flask(__name__)

@app.route('/convert', methods= ['POST'])

def convertMatrix():
    matrixInput= request.data.decode('utf-8').strip()
    if matrixInput== '0 0':
        return 'Matriz faltante en el request', 400
    
    convertedMatrix= ConverterService.convertMatrix(matrixInput)

    return convertedMatrix, 200

if __name__=='__main__':
    app.run(debug=True)
