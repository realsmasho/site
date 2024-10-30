from flask import Flask, send_file, request
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

# Endpoint to create a profile card
@app.route('/profile-card', methods=['GET', 'POST'])
def profile_card():
    # Get parameters from the request
    username = request.args.get('username', 'Guest')
    messages = request.args.get('messages', '0')
    memes = request.args.get('memes', '0')
    
    # Open the template image
    template = Image.open("assets/profile_card_template.png")  # Make sure this file is in your project folder

    # Set up the drawing context and fonts
    draw = ImageDraw.Draw(template)
    font_path = "fonts/InterDisplay-Black.ttf"  # Adjust the path if necessary
    font = ImageFont.truetype(font_path, 48)  # Set the desired size

    # Add text to the template
    draw.text((192, 56), f"{username}", font=font, fill="white")
    draw.text((56, 289), f"{messages}", font=font, fill="white")
    draw.text((320, 289), f"{memes}", font=font, fill="white")

    # Convert to a format that can be sent as an HTTP response
    img_io = io.BytesIO()
    template.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)