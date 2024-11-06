from flask import Flask
server = Flask(__name__)

def calcular_factorial(numero):
    if numero < 0:
        return "El factorial de un número negativo no está definido"
    elif numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

@server.route('/factorial/<int:valor>', methods=['GET'])
def obtener_factorial(valor):
    resultado_factorial = calcular_factorial(abs(valor))
    if valor < 0 and valor % 2 == 0:
        resultado_factorial = -resultado_factorial
    return str(resultado_factorial)

if __name__ == '__main__':
    server.run(debug=True)
