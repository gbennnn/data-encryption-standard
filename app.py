from flask import Flask, render_template, request
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

app = Flask(__name__)

def des_encrypt(plain_text, key):
    data_bytes = plain_text.encode('utf-8')
    key_bytes = key.encode('utf-8')

    if len(key_bytes) != 8:
        raise ValueError("Kunci harus tepat 8 karakter.")

    cipher = DES.new(key_bytes, DES.MODE_ECB)
    padded_data = pad(data_bytes, DES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return encrypted.hex()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        plaintext = request.form.get('plaintext')
        key = request.form.get('key')

        try:
            result = des_encrypt(plaintext, key)
        except Exception as e:
            error = str(e)

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
