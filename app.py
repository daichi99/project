from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # 全てのオリジンからのリクエストを許可

@app.route('/taf', methods=['GET'])
def get_taf():
    taf_url = "https://aviationweather.gov/cgi-bin/data/taf.php?ids=RJCC,RJCB,RJCH,RJEC,RJSM,RJSS,RJAA,RJTT,RJGG,RJBB,RJOO,RJOT,RJOM,RJOK,RJFF,RJFR,RJFO,RJFU,RJFT,RJFM,RJFK,RJKA,ROAH,RODN,ROIG,ROMY,RORS,RCTP,RCKH,RCSS,RPLL,RPLC,RPVM,ZSPD,ZSSS,ZSHC&sep=true"
    
    try:
        # 外部APIからデータを取得
        response = requests.get(taf_url)
        response.raise_for_status()  # HTTPエラーをチェック
        return response.text, 200  # 成功時はデータをそのまま返す
    except requests.exceptions.RequestException as e:
        # エラー時にJSON形式でエラーメッセージを返す
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
