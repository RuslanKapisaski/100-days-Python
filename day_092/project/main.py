from flask import Flask, render_template, request, url_for
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % tuple(map(int, rgb))


@app.route("/", methods=["GET", "POST"])
def home():
    colors = []
    image_path = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            image_path = url_for("static", filename=f"uploads/{file.filename}")

            img = Image.open(filepath).convert("RGB")
            img = img.resize((200, 200))

            pixels = np.array(img).reshape(-1, 3)

            kmeans = KMeans(n_clusters=10, random_state=42, n_init=10)
            kmeans.fit(pixels)

            colors = [rgb_to_hex(color) for color in kmeans.cluster_centers_]

    return render_template("index.html", colors=colors, image_path=image_path)


if __name__ == "__main__":
    app.run(debug=True)