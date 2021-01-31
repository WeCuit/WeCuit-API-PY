from flask import Flask
from flask import request
from flask import jsonify
import muggle_ocr
import rsa
modulus = 'F2CBD6CE742CFA08DEDCE0C5AA293BEE7AD8F3E8512DE8FBE9B58D3A1CB280486864D5F2A7AFDA9AC8789ED5B992BA3236D95BC9DF3C8F8ED2C902F5D5F31A3939749146E89509E717CDC16885B38ADA4A29EC393A3061FF751A87952EDE7DB5F8B94D6352E58BAD1AAD0EA0B0BFCFBDE470898D7A7E6C93E1F043C1793921F6CF1577141989092FD37DFB8437D57D138AC74FF9F91A7E1EE3139BFD9238D3F8E3A46955DE7967BD41554F8E28A0D6ED3CF3452970FC8CF5F0DF188D11BD8D3D374EE4CBF88CCC173AC19CD9878AC09364D4D58E0E679F99685DD4D5B7CD0AD6050989EBD3312046D657ABF9CB40E5CE8D8866F18165D568B3DFA8B3509A7F27'

app = Flask(__name__)
OCR = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)


@app.route("/vercode", methods=["POST"])
def verify_code():
    img = request.files['captcha'].stream.read()
    result = OCR.predict(image_bytes=img)
    return jsonify({
        "result": result,
    })

@app.route("/webvpn", methods=["POST", "GET"])
def webvpn():
    string = request.form['str']
    pub_key = rsa.PublicKey(int(modulus, 16), 65537)
    encrypted_pwd = rsa.encrypt(f"{string}".encode("utf-8"), pub_key).hex()
    return jsonify({
        "result": encrypted_pwd,
    })

if __name__ == '__main__':
    app.run(
        debug=False,
        port=4006
    )
