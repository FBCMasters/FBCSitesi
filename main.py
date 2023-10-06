from flask import Flask
import random
from flask import Flask, render_template

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

facts_list = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor",
            "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız",
            "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir"]

EskiParola = "FBCMasters+FBC-/*!&$#?=@abcdefghijklnopqrstuvwxyzABBBBBCCCDEFFFFFFFFFFGHIJKLMNOPQRSTUVWXYZ1234567890FBCParolası"
YT = ["Yazı",
      "Tura"]
TKM = ["Taş",
      "Kağıt",
      "Makas"]
YeniParola = ""
Cevap = ""
Cevap = random.choice(YT)
TKMC = ""
TKMC = random.choice(TKM)
for i in range(10):
    YeniParola += random.choice(EskiParola)

@app.route("/")
def hello_world():
    return render_template('main.html')

@app.route('/fbc')
def index():
    return render_template('fbc.html')

@app.route('/havadurumu')
def hava():
    return render_template('hava.html')

@app.route("/kodland")
def kod():
    return render_template('kod.html')

@app.route("/virüslüsakınindirmeyin")
def tehlike():
    return render_template('virüs.html')

@app.route("/yazitura")
def ello_world():
    return f'<h1>Yazı yı mı Tura yı mı seçiyorsunuz?</h1><a href = http://127.0.0.1:5000/yazi>     Yazı    </a><p>      Veya      </p><a href = http://127.0.0.1:5000/tura>     Tura</a>'

@app.route("/yazi")
def el_world():
    Cevap = ""
    Cevap = random.choice(YT)
    if Cevap == "Yazı":
        Cevap = "Kazandın, Yazı çıktı!"
    elif Cevap == "Tura":
        Cevap = "Kaybettin, Tura çıktı!"
    else:
        Cevap = "Düz durdu!"
    return f'<h1>{Cevap}</h1><a href = http://127.0.0.1:5000/yazitura>     Tekrar oynamak için tıklayın!</a>'

@app.route("/tura")
def lo_world():
    Cevap = ""
    Cevap = random.choice(YT)
    if Cevap == "Yazı":
        Cevap = "Kaybettin, Yazı çıktı!"
    elif Cevap == "Tura":
        Cevap = "Kazandın, Tura çıktı!"
    else:
        Cevap = "Düz durdu!"
    return f'<h1>{Cevap}</h1><a href = http://127.0.0.1:5000/yazitura>     Tekrar oynamak için tıklayın!</a>'

@app.route("/taskagıtmakas")
def tkm_world():
    return f'<h1>Taş mı Kağıt mı Makas mı?</h1><a href = http://127.0.0.1:5000/tas>     Taş    </a><p>      mı      </p><a href = http://127.0.0.1:5000/kagıt>     Kağıt    </a><p>      mı      </p><a href = http://127.0.0.1:5000/makas>     Makas   </a><p>      mı?      </p>'

@app.route("/tas")
def t_world():
    TKMC = ""
    TKMC = random.choice(TKM)
    if TKMC == "Taş":
        TKMC = "Berabere, Taşı seçmiştim!"
    elif TKMC == "Kağıt":
        TKMC = "Kaybettin, Kağıtı seçmiştim!"
    elif TKMC == "Makas":
        TKMC = "Kazandın, Makası seçmiştim!"
    else:
        Cevap = "Hile var, silahı seçmiştim!"
    return f'<h1>{TKMC}</h1><a href = http://127.0.0.1:5000/taskagıtmakas>     Tekrar oynamak için tıklayın!</a>'

@app.route("/kagıt")
def k_world():
    TKMC = ""
    TKMC = random.choice(TKM)
    if TKMC == "Taş":
        TKMC = "Kazandın, Taşı seçmiştim!"
    elif TKMC == "Kağıt":
        TKMC = "Berabere, Kağıtı seçmiştim!"
    elif TKMC == "Makas":
        TKMC = "Kaybettin, Makası seçmiştim!"
    else:
        Cevap = "Hile var, silahı seçmiştim!"
    return f'<h1>{TKMC}</h1><a href = http://127.0.0.1:5000/taskagıtmakas>     Tekrar oynamak için tıklayın!</a>'

@app.route("/makas")
def m_world():
    TKMC = ""
    TKMC = random.choice(TKM)
    if TKMC == "Taş":
        TKMC = "Kaybettin, Taşı seçmiştim!"
    elif TKMC == "Kağıt":
        TKMC = "Kazandın, Kağıtı seçmiştim!"
    elif TKMC == "Makas":
        TKMC = "Berabere, Makası seçmiştim!"
    else:
        Cevap = "Hile var, silahı seçmiştim!"
    return f'<h1>{TKMC}</h1><a href = http://127.0.0.1:5000/taskagıtmakas>     Tekrar oynamak için tıklayın!</a>'

@app.route("/sifre")
def h_world():
    EskiParola = "FBCMasters+FBC-/*!&$#?=@abcdefghijklnopqrstuvwxyzABBBBBCCCDEFFFFFFFFFFGHIJKLMNOPQRSTUVWXYZ1234567890FBCParolası"
    YeniParola = ""
    for i in range(10):
        YeniParola += random.choice(EskiParola)
    return f'<h4>{YeniParola}</h4><a href = http://127.0.0.1:5000/sifre>     Yeni bir şifre için tıklayın!</a>'

@app.route("/bilgi")
def hi_world():
    return f'<h1>{random.choice(facts_list)}</h1><a href = http://127.0.0.1:5000/bilgi>     Daha fazlası için tıklayın!</a>'

@app.route('/ev')
def ev():
    return render_template('index.html')

# İkinci sayfa
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights                           
                           )

# Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )

app.run(debug=False)