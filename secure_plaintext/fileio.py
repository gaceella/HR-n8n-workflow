# fileio.py
import os
import numpy as np

# Ensure folders exist
os.makedirs("notes", exist_ok=True)
os.makedirs("keys", exist_ok=True)

# ---------- Notes ----------

def save_note(filename, text):
    with open("notes/" + filename, "w") as f:
        f.write(text)

def load_note(filename):
    with open("notes/" + filename, "r") as f:
        return f.read()

# ---------- Keys ----------

def save_key(filename, K, K_inv):
    with open("keys/" + filename, "w") as f:
        f.write(f"{K[0,0]} {K[0,1]}\n")
        f.write(f"{K[1,0]} {K[1,1]}\n")
        f.write(f"{K_inv[0,0]} {K_inv[0,1]}\n")
        f.write(f"{K_inv[1,0]} {K_inv[1,1]}\n")

def load_key(filename):
    with open("keys/" + filename, "r") as f:
        lines = f.readlines()
        K = np.array([[int(n) for n in lines[0].split()],
                      [int(n) for n in lines[1].split()]])
        K_inv = np.array([[int(n) for n in lines[2].split()],
                          [int(n) for n in lines[3].split()]])
    return K, K_inv
