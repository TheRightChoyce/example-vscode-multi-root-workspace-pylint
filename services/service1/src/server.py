"""
Runs the server for service1

example:

$ python3 src/server.py

"""

from quart import Quart

app = Quart(__name__)

@app.route('/')
async def hello():
    """
    Returns "hello from service1"
    """
    return 'hello from service1'

if __name__ == "__main__":
    app.run(port=5001, host='0.0.0.0')