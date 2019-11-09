import os
import bottle

bottle.route("/")
def func():
	return "Ok"

bottle.run(server="gunicorn", host="0.0.0.0", port = int(os.environ.get("PORT",5000)))

