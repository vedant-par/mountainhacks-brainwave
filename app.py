from flask import Flask, render_template, request, send_from_directory
import os
import clear_speech
import lung_detection

app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/audio')
def audio():
    return render_template('audio.html')

@app.route('/breath')
def breath():
    return render_template('breath.html')
    

@app.route('/hand')
def hand():
    return render_template('hand.html')


@app.route('/download', methods=['POST'])
def download():
    # get the filename of the captured image from the request
    filename = request.form.get('filename')

    # construct the full path to the captured image file in the Downloads folder
    path = os.path.join(os.path.expanduser("~"), 'Downloads', filename)

    # check if the file exists
    if not os.path.isfile(path):
        return 'File not found', 404

    # return the file to the client for download
    return send_from_directory(os.path.expanduser("~")+'/Downloads', filename, as_attachment=True)

app.route('/final')
def final():
    rslt = clear_speech.check_clarity('/Users/vparikh/Downloads/recorded-video.mp4')
    if rslt == 1:
        return render_template('good.html')
    else:
        return render_template('brain.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
