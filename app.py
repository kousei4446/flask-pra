from flask import Flask, request, jsonify, abort
import nanoid
import cv2
app = Flask(__name__)

@app.route('/', methods=['GET']) # methods は省略可

def root():
 return 'hello, world'

@app.route('/jugemu/jugemu/gokono/')
def jugemu():
 return 'surikire'

@app.route('/greet/<name>') # パスの一部を変数で受け取る1
def greet(name):
 return f'hello, {name}!'

@app.route("/v1/photos", methods=['POST'])
def post_photos():
    file = request.files['file']
    if file.content_type == 'image/jpeg':
      filename = f'static/{nanoid.generate(size=4)}.jpg'
      file.save(filename)

      # モノクロ版の画像を保存
      img = cv2.imread(filename)  # 保存した画像を読み込む
      gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # モノクロに変換
      gray_filename = filename.replace('.jpg', '_gray.jpg')  # モノクロ版のファイル名
      cv2.imwrite(gray_filename, gray_img)  # モノクロ画像を保存

      resp = {'url': f'/{filename}'}
      return jsonify(resp)
    else:
      abort(400) # 400 Bad Request

if __name__ == "__main__":
    # host='0.0.0.0' を追加
    app.run(host="0.0.0.0", port=5000, debug=True)
