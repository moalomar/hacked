import datetime, flask
app = flask.Flask(__name__, template_folder='')
@app.errorhandler(Exception)
def _(_):
    time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
    filename = time.strftime('%Y.%m.%d.%H.%M.%S.%f') + '.txt'
    with open(f'ips/{filename}', 'w', encoding='utf-8') as file:
        file.write(flask.request.remote_addr)
    return flask.render_template('index.html', ip=flask.request.remote_addr)