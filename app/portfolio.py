from flask import(
    Blueprint, render_template,request, current_app,redirect, url_for
)
import sendgrid
from sendgrid.helpers.mail import *
bp = Blueprint('portfolio',__name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/es/index.html')

@bp.route('mail', methods=['POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        sendEmail(name, email, message)

    return redirect(url_for('portfolio.sentmail'))

@bp.route('sentmail', methods=['GET'])
def sentmail():
    return render_template('portfolio/es/sent_mail.html')


@bp.route('en/', methods=['GET'])
def enIndex():
    return render_template('portfolio/en/index.html')
@bp.route('en/mail', methods=['POST'])
def enMail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        sendEmail(name, email, message)

    return redirect(url_for('portfolio.enSentmail'))

@bp.route('en/sentmail', methods=['GET'])
def enSentmail():
    return render_template('portfolio/en/sent_mail.html')
def sendEmail(name, email, message):
    myEmail=current_app.config['FROM_EMAIL']
    sg= sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])

    fromEmail = Email(myEmail)
    toEmail = To(myEmail, substitutions={
        "-name-": name,
        "-email-": email,
        "-message-": message,
    })

    htmlContent = """
        <p>Hola, tienes un nuevo contacto desde la web: </p>
        <p>Nombre: -name- </p>
        <p>Email: -email- </p>
        <p>Mensaje: -message- </p>
    """
    mail = Mail(fromEmail,toEmail,"Nuevo contacto de la web", html_content=htmlContent)
    response = sg.send(mail)