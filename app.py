from flask import Flask, render_template, request

app = Flask(__name__)

port = "5003"

def encrypt(text):
    # Convert each character to its corresponding ASCII code and join them with spaces
    encrypted_string = ' '.join(str(ord(char)) for char in text)
    return encrypted_string

def decrypt(encrypted_text):
    # Split the string into individual numbers
    numbers = encrypted_text.split()
    # Convert each number to its corresponding ASCII character
    decrypted_text = ''.join(chr(int(num)) for num in numbers)
    return decrypted_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        option = request.form['option']
        text = request.form['text']
        if option == 'encrypt':
            result = encrypt(text)
        elif option == 'decrypt':
            result = decrypt(text)
        else:
            result = 'Invalid option. Please choose either "encrypt" or "decrypt".'
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    # Run the Flask app with the specified port
    app.run(port=port)