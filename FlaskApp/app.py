from flask import Flask, render_template, request

app = Flask(__name__)

# Data obat (Nama & Fungsi)
data_obat = {
    "Amlodipine": "Menurunkan tekanan darah pada hipertensi dan mengatasi angina.",
    "Amoxicillin": "Antibiotik untuk infeksi bakteri, seperti infeksi saluran pernapasan dan saluran kemih.",
    "Betamethasone": "Kortikosteroid untuk mengurangi peradangan dan reaksi alergi.",
    "Bisoprolol": "Beta-blocker untuk mengontrol tekanan darah tinggi dan gagal jantung.",
    "Ceftriaxone": "Antibiotik untuk infeksi bakteri berat, seperti meningitis dan pneumonia.",
    "Cetirizine": "Antihistamin untuk meredakan alergi, seperti rinitis alergi dan urtikaria.",
    "Dexamethasone": "Kortikosteroid untuk inflamasi, alergi, dan terapi tambahan pada beberapa penyakit autoimun.",
    "Diclofenac": "Antiinflamasi nonsteroid (NSAID) untuk mengatasi nyeri dan peradangan.",
    "Enalapril": "ACE inhibitor untuk mengobati hipertensi dan gagal jantung.",
    "Furosemide": "Diuretik untuk mengurangi kelebihan cairan pada edema dan hipertensi.",
    "Paracetamol": "Analgesik dan antipiretik untuk meredakan nyeri ringan hingga sedang serta menurunkan demam.",
    "Ibuprofen": "NSAID untuk mengatasi nyeri, peradangan, dan demam.",
    "Metformin": "Antidiabetes oral untuk meningkatkan sensitivitas insulin pada diabetes tipe 2.",
    "Omeprazole": "PPI untuk mengurangi asam lambung dan mengobati GERD serta tukak lambung."
}

@app.route('/', methods=['GET', 'POST'])
def home():
    hasil = None
    if request.method == 'POST':
        nama_obat = request.form['nama_obat'].strip().capitalize()
        hasil = data_obat.get(nama_obat, "Obat tidak ditemukan.")
    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
