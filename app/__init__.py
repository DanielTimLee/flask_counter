from flask import Flask, render_template, request, make_response

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    a=request.cookies.get('counter')
    if a:
        a=int(a)

    if not a:
        a=1
    else:
        a=a+1

    print(a)

    resp = make_response(render_template('index.html',a=a))
    resp.set_cookie('counter',str(a))

    return resp

