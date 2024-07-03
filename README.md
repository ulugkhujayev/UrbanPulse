# UrbanPulse: Real-Time City Monitoring System

UrbanPulse is a comprehensive real-time city monitoring system built with Django. It tracks public transportation, traffic incidents, and local events, providing live updates via WebSockets and a RESTful API for querying urban data.

## Features

- Real-time tracking of public transportation vehicles
- Reporting and monitoring of traffic incidents
- Management of city events
- Geofencing capabilities
- Map-based visualizations
- RESTful API with JWT authentication
- WebSocket support for live updates
- Rate limiting to prevent API abuse

## Setup

1. Clone the repository:
   git clone https://github.com/yourusername/urbanpulse.git
   cd urbanpulse
   Copy
2. Create a `.env` file in the project root and add the necessary environment variables:
   `DEBUG=False
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=urbanpulse
DB_USER=urbanpulse
DB_PASSWORD=urbanpulse_password
DB_HOST=db
DB_PORT=5432
REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0`

3. Build and run the Docker containers:
   `docker-compose up --build`
4. Create a superuser:
   `docker-compose exec web python manage.py createsuperuser`
5. Access the API at `http://localhost:8000/api/` and the admin interface at `http://localhost:8000/admin/`

## API Usage

To use the API, you need to obtain a JWT token:
`curl -X POST http://localhost:8000/api/token/ -d "username=your_username&password=your_password"`

Then, use the token in your requests:
`curl -H "Authorization: Bearer your_token" http://localhost:8000/api/vehicles/`
For WebSocket connections:

```
javascript
const socket = new WebSocket('ws://localhost:8000/ws/vehicles/');

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data);
};
```

## Running Tests

`docker-compose exec web python manage.py test`

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

### Project is not complete yet :)
