from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/taf', methods=['GET'])
def get_taf():
    taf_url = "https://aviationweather.gov/cgi-bin/data/taf.php?ids=RJCC,RJCB,RJCH,RJEC,RJSM,RJSS,RJAA,RJTT,RJGG,RJBB,RJOO,RJOT,RJOM,RJOK,RJFF,RJFR,RJFO,RJFU,RJFT,RJFM,RJFK,RJKA,ROAH,RODN,ROIG,ROMY,RORS,RCTP,RCKH,RCSS,RPLL,RPLC,RPVM,ZSPD,ZSSS,ZSHC&sep=true"
    try:
        response = requests.get(taf_url)
        response.raise_for_status()
        return response.text, 200  # TAFデータをそのまま返す
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
