from fastapi import FastAPI, Request
from datetime import datetime
import pulsar 

app = FastAPI()

@app.get("/")
async def root(request: Request):

    ip_address = request.client.host
    request_url = request.url._url
    request_port = request.url.port
    request_path = request.url.path
    request_method = request.method
    request_time = datetime.now()
    browser_type = request.headers["User-Agent"]
    operating_system = request.headers["Accept"]
    message = {
        "ip_address": ip_address,
        "request_url": request_url,
        "request_port": request_port,
        "request_path": request_path,
        "request_method": request_method,
        "request_time": request_time,
        "browser_type": browser_type,
        "operating_system": operating_system,
    }

    client = pulsar.Client('pulsar://localhost:6650')
    producer = client.create_producer('my-topic')
   
    producer.send(str(message).encode("utf-8"))
    client.close()
    return {"message": message}

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
