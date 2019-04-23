import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 465)
server.starttls()
email = input() # example@gmail.com
drowssap = input() # or replace with string
mail_to = input() # hello_world@gmail.com
url_inp = input() # https://in.bookmyshow.com/buytickets/avengers-endgame-hyderabad/movie-hyd-ET00100559-MT/20190426
theater = input() # "Prasads: Large Screen"
server.login(email, drowssap)
msg_from = email
msg_to = mail_to
message = MIMEMultipart()
message['From'] = msg_from
message["To"] = msg_to

message['Subject'] = "Avengers: Endgame Tickets Available at Prasads large Screen."
body = '''Avengers: Endgame Tickets Available at Prasads large Screen.

        Book ASAP!!

        bms: ''' + url_inp + '''

        Regards
        Naveen
        '''
message.attach(MIMEText(body, 'plain'))
text = message.as_string()


def movie():
    url = url_inp

    # open with GET method
    flag = True
    while flag is True:
        page = requests.get(url)

        if page.status_code == 200:
            # print("Successfully opened the web page")
            soup = BeautifulSoup(page.text, 'html.parser')

            for i in soup.find_all("a", class_="__venue-name"):
                if theater in i.text:
                    print("Its open!")
                    server.sendmail(msg_from, [msg_to],
                                    text)
                    flag = False
                    break;
        else:
            print(page.status_code + "Error")


movie()
