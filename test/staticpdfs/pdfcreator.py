import pdfkit
from pyrebase import pyrebase

options = {
    "enable-local-file-access": None,
    "page-size": "A5",
    "viewport-size": "1366 x 768",
    'disable-smart-shrinking': '',
    'margin-top': '0in',
    'dpi': 900,
    'margin-right': '0.8in',
    'margin-bottom': '0in',
    'margin-left': '0.8in',
}
config = {
    "apiKey": "AIzaSyB7cTfNmxp_OA9vOKL94O10FRHe_PyyziQ",
    "authDomain": "whoabot-181f2.firebaseapp.com",
    "databaseURL": "https://whoabot-181f2.firebaseio.com",
    "projectId": "whoabot-181f2",
    "storageBucket": "whoabot-181f2.appspot.com",
    "messagingSenderId": "437598146366",
    "appId": "1:437598146366:web:b36b6702a749b7466da66f",
    "measurementId": "G-LCRZ7MP631"
}

# pdfkit.from_file("D:\Misc Practice\Chatbot\Rasa Projects\webpages\page2.html", './staticpdfs/myfile.pdf', options=options)
def upload_pdf():
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    path_local = "./Insomnia/3.pdf"
    path_on_cloud = "pdfs/Insomnia/3.pdf"
    storage.child(path_on_cloud).put(path_local)
    print(storage.child(path_on_cloud).get_url(path_on_cloud))

def get_pdf(story,number):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    path_on_cloud = "pdfs/{}/{}.pdf".format(str(story),str(number))
    print(storage.child(path_on_cloud).get_url(path_on_cloud))
    return storage.child(path_on_cloud).get_url(path_on_cloud)

if __name__ == "__main__":
    upload_pdf()
#     # get_pdf("Insomnia",1)

