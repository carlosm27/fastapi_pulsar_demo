from fastapi import FastAPI
import pulsar 

app = FastAPI()

@app.get("/")
async def root():
    client = pulsar.Client('pulsar://localhost:6650')
    producer = client.create_producer('my-topic')
    producer.send(("Hello Pulsar").encode('utf-8'))
    client.close()
    return {"message": "Message send"}

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
