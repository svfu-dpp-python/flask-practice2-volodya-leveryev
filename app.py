from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    result = ""
    if 'expression' in request.args:
        print("================================================================================")
        print(request.args)  # Печать отладочного сообщения
        print("================================================================================")
        app.logger.warning(request.args)  # Печать отладочного сообщения
        print("================================================================================")
        result = str(eval(request.args['expression']))
    return render_template("index.html", result=result)
