from flask import Flask, request, jsonify , redirect
from pptgenerator import generateppt
linko = generateppt("AI Industry")

print('linko')
print(linko)
print('linko')

if __name__ == '__main__':
  #  app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
