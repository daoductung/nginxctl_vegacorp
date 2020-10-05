from flask import Flask, redirect, request, jsonify
import nginxctl

app = Flask(__name__)


def message_response(status=200, msg = ""):
    return {
        "msg": msg,
        "status": status
    }
        

@app.route("/")
def hello_world():
    return "Hello Wrold!"


@app.route("/nginx", methods=['POST'])
def process_nginx():
    if request.method == "POST":
        type_request_get = request.form.get('type').lower().strip()
        if type_request_get not in ['start', 'stop', 'reload', 'restart']:
            return message_response(404, "Cannot get the type of command to be executed")
        n = nginxctl.nginxCtl()
        if type_request_get == "start":
            status, err = n.start_nginx()
            if err:
                return message_response(404, err)
            return message_response(200, "Start nginx susccess")
        if type_request_get == "stop":
            status, err = n.stop_nginx()
            if err:
                return message_response(404, err)
            return message_response(200, "Stop nginx susccess")
        if type_request_get == "reload":
            status, err = n.reload_config_nginx()
            if err:
                return message_response(404, err)
            return message_response(200, "Reload config nginx susccess")

        if type_request_get == "restart":
            status, err = n.restart_nginx()
            if err:
                return message_response(404, err)
            return message_response(200, "Restart nginx susccess")
    return message_response(404, "Cannot get the type api")
        



if __name__ == "__main__":
    app.run()
