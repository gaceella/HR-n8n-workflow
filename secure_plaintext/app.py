from flask import Flask, render_template, request, send_file
from crypto import generate_key_matrix, encrypt, decrypt
from fileio import save_key, load_key
import os

app = Flask(__name__)

KEY_FILE = "keys/webkey.txt"

@app.route("/", methods=["GET","POST"])
def index():
    result = ""
    message = ""
    key_display = ""

    if request.method == "POST":
        action = request.form["action"]

        # ---- Generate Key ----
        if action == "genkey":
            if os.path.exists(KEY_FILE):
                message = "Key already exists. Delete old key to generate new."
            else:
                K, K_inv = generate_key_matrix()
                save_key("webkey.txt", K, K_inv)
                key_display = f"Encryption Matrix:\n{K}"
                message = "Secure key generated successfully!"

        # ---- Encrypt ----
        elif action == "encrypt":
            if not os.path.exists(KEY_FILE):
                message = "Please generate key first!"
            else:
                text = request.form["text"]
                K, _ = load_key("webkey.txt")
                result = encrypt(text, K)

        # ---- Decrypt ----
        elif action == "decrypt":
            if not os.path.exists(KEY_FILE):
                message = "Please generate key first!"
            else:
                text = request.form["text"]
                _, K_inv = load_key("webkey.txt")
                result = decrypt(text, K_inv)

    return render_template("index.html",
                           result=result,
                           message=message,
                           key_display=key_display)

@app.route("/download_key")
def download_key():
    return send_file(KEY_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
