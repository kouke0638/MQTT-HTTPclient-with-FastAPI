# MQTT-HTTPclient-with-FastAPI

This project is developed in Python and employs the highly efficient FastAPI framework as its core architecture. The primary aim is to facilitate the sending of MQTT message requests through a straightforward HTTP API, thereby extending MQTT messaging capabilities to a broader range of devices. This includes embedded systems and various internet-enabled devices, enhancing their connectivity and enabling them to participate in MQTT communications more effectively.

### Features

- Custom error handling
- MQTT message delivery support

## Getting Started

### Installing

- Clone this repository to your local machine.
- Ensure Python 3.11 is installed.
- Install required Python packages

## Usage

### Error Handling

Custom error pages are provided for server errors and not found errors. The server returns customized HTML responses for these cases.

### MQTT Messaging

Send a POST request to `/mqtt` with a JSON payload containing the MQTT server details and the message to be published:

```json
{
	"server": "test.io",
	"port": 1883,
	"topic": "test",
	"message": "Hello, MQTT!"
}
```

**Note!** If deploying with Vercel, please navigate to the settings and update the Node.js version to 18.x to prevent any errors.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the [MIT]. Please see the LICENSE.md file for details.
