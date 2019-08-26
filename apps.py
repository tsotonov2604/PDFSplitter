from flask import *
import PDFsplitter

apps = Flask(__name__) #looks for defined static file

@apps.route("/") #homepage
def upload():
    return render_template("file_upload.html")

@apps.route("/success",methods=["POST"]) #selection of file upload
def success():
   global st #start page int
   global en #end page int
   global file #filename
   st= int(request.form['start'])
   en = int(request.form['end'])
   f = request.files['file']
   file = f.filename
   f.save(file)
   return render_template("success.html",start = st,end = en, name= file)

@apps.route("/convert")
def cropper(): # execution of crop
    PDFsplitter.cropper(st,en,file)
    return render_template("download.html")


@apps.route("/download")
def download():
    filename = file.split(".")[0]+"cropped.pdf"
    return send_file(filename,as_attachment=True)


if __name__ == "__main__":
    apps.run(debug = True)