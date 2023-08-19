from flask import Flask, render_template, redirect, request, jsonify, send_file
from text_to_speech import text_to_speech
from pydub import AudioSegment
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    try:
        audio_data = request.files['audio']
        if audio_data:
            audio_path = 'test.wav'
            audio_data.save(audio_path)
            text_to_speech()
            
            # Convert audio to out.wav
            filename = 'speech.wav'
            sound = AudioSegment.from_file(filename, format=filename[-3:])
            sound.export("out.wav", format="wav")
            
            return jsonify({'message': 'Audio generated and saved successfully'}), 200
        else:
            return jsonify({'error': 'No audio data received'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_response_audio', methods=['GET'])
def get_response_audio():
    try:
        if os.path.exists('out.wav'):
            return send_file('out.wav', as_attachment=True)
        else:
            return jsonify({'error': 'Audio not generated yet'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
