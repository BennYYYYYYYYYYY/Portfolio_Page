from flask import Flask, render_template # Flask類用於創建Flask應用、render_template函數用於渲染HTML模板

app = Flask(__name__) # app 是創建的Flask應用實例，用這個對象來配置和運行Web應用
'''
__name__ 是一個特殊的內建變量，表示當前模塊的名稱。

當直接運行一個Python腳本時，__name__ 會被設置為 '__main__'。
如果這個腳本被作為一個模塊導入到其他腳本中，__name__ 就會是這個模塊的名稱。

傳遞 __name__ 給 Flask 構造函數有助於Flask確定應用的根目錄。
這樣Flask就能正確地找到靜態文件夾和模板文件夾的位置，這些文件夾通常放在應用的根目錄中。

靜態文件: 通常包括CSS、JavaScript和圖像文件，這些文件通常放在一個名為 static 的文件夾中。
模板文件: 包括HTML文件，這些文件通常放在一個名為 templates 的文件夾中。

當創建Flask應用並傳遞 __name__ 時，Flask會假設你的靜態文件和模板文件是相對於這個根目錄的。
假設項目結構如下：

    my_flask_app/
        static/
            style.css
        templates/
            index.html
        app.py

運行 app.py 時，Flask使用 __name__ 的值來確定應用的根目錄。
在這個例子中，app.py 位於 my_flask_app/ 目錄下，因此 my_flask_app/ 成為應用的根目錄。
Flask使用Python的標準庫(如os)來解析當前模塊的路徑，確定應用的根目錄。
根據這個路徑，Flask知道在哪裡查找靜態文件和模板文件。

'''

@app.route('/') # 這是一個裝飾器，它告訴Flask，當用戶訪問網站的根URL ('/') 時，應該運行下面定義的函數。
# @: 表示這是一個裝飾器。
# app: 創建的Flask應用對象。
# route: 是Flask應用對象的route方法，它用來定義URL路由。
# '/': 是URL路徑，這裡表示網站的【根URL】。

def home(): 
    return render_template('index.html') # 返回一個渲染後的index.html模板
    # render_template 是 Flask 提供的一個函數，用於渲染模板。模板是包含靜態數據和動態數據併入的文件，通常用於生成 HTML 文件。
    # Flask 預設會在 templates 料夾中查找模板文件

if __name__ == '__main__': # 檢查是否直接運行該腳本 (而不是作為模塊被導入)
    app.run(debug=True) # 如果是，它會啟動Flask開發Web服務器。
    # debug=True參數告訴Flask啟動調試模式，這樣在代碼發生更改時，服務器會自動重啟，並顯示錯誤信息。
    # 自動重新加載: 當代碼發生變更時，Flask 服務器會自動重新加載。不需要手動重啟服務器來查看代碼變更的效果，這大大提高了開發效率。

'''
app.run()：這個方法會啟動Flask的內建開發伺服器。
當它運行後，你的Flask應用就會在本地的某個端口上被託管，默認情況下是5000端口。
'''


'''
根URLS:
    根URL是指網站的主頁或首頁的地址，也就是網站的起始點。
    它通常不包括具體的路徑或文件名。在URL中，根URL通常表示為一個斜杠/。

    
假設網站的域名是 https://www.example.com。

根URL是 https://www.example.com/，即首頁的地址。

當用戶在瀏覽器中輸入 https://www.example.com 或 https://www.example.com/，他們將被導向網站的首頁。

'''

'''
靜態數據:
    靜態數據是模板中固定不變的部分，無論何時渲染模板，這些數據始終保持不變。
    這些數據通常包括 HTML 標籤、固定的文本、CSS 和 JavaScript 文件的鏈接等。

動態數據:
    動態數據是模板中根據上下文或外部數據源 (如數據庫、用戶輸入等)而改變的部分。
    這些數據在每次渲染時都可能不同。動態數據通常由後端應用程序生成並插入到模板中。

'''
