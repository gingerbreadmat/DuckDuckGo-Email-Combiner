from flask import Flask, request, render_template

app = Flask(__name__)

def combine_emails(sender_email, receiver_email):
    modified_receiver_email = receiver_email.replace("@", "_at_")
    combined_email = f"{modified_receiver_email}_{sender_email}"
    return combined_email

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        sender_email = request.form['sender_email']
        receiver_email = request.form['receiver_email']
        result = combine_emails(sender_email, receiver_email)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)