from flask import*
import speech_recognition as sr
import _portaudio as p
import pyaudio
from playsound import playsound
from googletrans import Translator
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
   

@app.route("/translate",methods=["POST"])
def translate():
    if request.form['btn']=="speak":
        val=request.form['a']
        r=sr.Recognizer()
        with sr.Microphone() as src:
            r.adjust_for_ambient_noise(src)
            playsound("say.mp3")
            audio=r.listen(src)
            playsound("time1.mp3")
            try:
                a=r.recognize_google(audio,language=val)
                return render_template("index.html",out=a)
            except:
                return redirect(url_for("home"))
                       
    elif request.form['btn']=="Translate":
            try:
                t=Translator()
                txt1=request.form['a']
                txt2=request.form['b']
                txt3=request.form['txtarea']
                result=t.translate(txt3,src=txt1,dest=txt2)
                return render_template("index.html",r=result.text)
            except:
                return redirect(url_for("home"))

@app.route("/profile",methods=["POST"])
def profile():
    return render_template("index2.html")
    
if __name__=="__main__":
    app.run()
