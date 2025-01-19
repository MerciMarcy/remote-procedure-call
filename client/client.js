const net = require('net');
const fs = require('fs');

const server_address = 'tmp/socket_file';

class Client {
  constructor(server_address) {
    this.server_address = server_address;
  }

  start() {
    const client = new net.Socket();

    const json = fs.readFileSync('data/data1.json');
    const data = JSON.parse(json);

    client.connect(this.server_address, () => {
      console.log('Connected to server');

      client.write(JSON.stringify(data));
    });

    client.on('data', (data) => {
      const res = JSON.parse(data);

      if (res.error) {
        console.error('Error: ', res.error);
      } else {
        console.log(res);
      }

      client.end();
    });

    client.on('close', () => {
      console.log('Connection closed');
    });

    client.on('error', (error) => {
      console.error('Error: ', error);
    });
  }
}

function main() {
  const client = new Client(server_address);
  client.start();
}

main();
