"""
Runs the server for service2

example:

$ python3 src/server.py

"""

from quart import Quart

app = Quart(__name__)

@app.route('/')
async def hello():
    """
    Returns "hello from service2"
    """
    return 'hello from service2'

if __name__ == "__main__":
    app.run(port=5002, host='0.0.0.0')
