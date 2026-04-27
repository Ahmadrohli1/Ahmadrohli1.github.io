import os

def bangun_sistem():
    # 1. Membuat file manifest.json (Agar web bisa di-install)
    manifest_content = """{
  "name": "Ahmad Project",
  "short_name": "Ahmad",
  "start_url": "index.html",
  "display": "standalone",
  "background_color": "#000000",
  "theme_color": "#000000",
  "description": "Portofolio Intelektual Ahmad"
}"""
    
    with open("manifest.json", "w") as f:
        f.write(manifest_content)
    print("[+] File manifest.json berhasil dibuat.")

    # 2. Membuat index.html baru (Menghapus jejak Facebook lama)
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Ahmad Rohli - Digital Home</title>
    <link rel="manifest" href="manifest.json">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: black; color: lime; font-family: monospace; text-align: center; padding: 50px; }
        .box { border: 1px solid lime; padding: 20px; display: inline-block; }
        a { color: white; text-decoration: none; border: 1px solid white; padding: 5px; }
    </style>
</head>
<body>
    <div class="box">
        <h1>AHMAD ROHLI SYSTEM</h1>
        <p>Status: Online & Intelektual</p>
        <hr>
        <p>Aplikasi ini sekarang terpasang di HP Anda.</p>
        <br>
        <a href="scatter.py">Lihat Script Scatter</a>
    </div>
</body>
</html>"""

    with open("index.html", "w") as f:
        f.write(html_content)
    print("[+] File index.html berhasil diperbarui.")

if __name__ == "__main__":
    bangun_sistem()
