# HNG12 Stage 0 Backend API

## Project Description

This project is a **Flask API** that serves basic information, including the following details in JSON format:

- **Email Address**: The registered email address used to join the HNG12 Slack workspace.
- **Current Datetime**: The current date and time in **ISO 8601** format (UTC).
- **GitHub URL**: The GitHub URL where the project’s codebase is hosted.

The API is designed to be publicly accessible and is deployed to a hosting platform, supporting **Cross-Origin Resource Sharing (CORS)** for seamless integration with other applications.

## Features

- Provides email, current datetime, and GitHub URL in JSON format.
- Dynamic `current_datetime` that reflects the current time in **UTC**.
- CORS handling for cross-origin requests.

## Setup Instructions

### Prerequisites

Before running this project locally, make sure you have the following:

- **Python 3.7+**: The required version of Python to run this application.
- **pip**: Python's package installer to install dependencies.
  
### Steps to Run the Project Locally

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/dohoudaniel/hng-stage-0.git
   cd hng-stage-0
   ```

2. **Install Dependencies**

   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   This will install `Flask` and `flask_cors`, which are the primary dependencies for this project.

3. **Run the Flask App**

   To run the Flask app locally, use the following command:

   ```bash
   python app.py
   ```

   This will start the Flask development server at `http://127.0.0.1:5000/` (by default).

4. **Access the API**

   Open a web browser or API testing tool (like Postman) and access the following endpoint:

   ```
   GET http://127.0.0.1:5000/
   ```

   This will return the JSON response with the required information.

## API Documentation

### Endpoint URL

- **GET** `/`

### Request Format

The request should be made via an HTTP **GET** method to the root URL of the API.

- **URL**: `http://<your-deployed-url>/`
- **Method**: `GET`

### Response Format

The API will return a **JSON** response with the following structure:

```json
{
  "email": "dohoudanielfavour@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/dohoudaniel/hng-stage-0"
}
```

- **email**: My registered email address (used for HNG12).
- **current_datetime**: The current date and time in **ISO 8601** format (UTC).
- **github_url**: The GitHub URL of the project repository.

### Example Usage

Here’s an example of what the response will look like when you make a `GET` request:

```bash
curl http://127.0.0.1:5000/
```

**Response**:
```json
{
  "email": "dohoudanielfavour@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/dohoudaniel/hng-stage-0"
}
```

### Error Handling

If an invalid endpoint is accessed (e.g., a non-existing route), the application will redirect the user to the home page (`/`) with a **404 error**.

## Deployment

The API is deployed on **[Render](https://render.com/)**, and it is publicly accessible at the following URL:

- **Deployed URL**: `https://dohoudanielfavour-hng-stage-0.onrender.com`

### CORS

CORS is handled using the `flask_cors` library, ensuring that the API can be accessed by client applications running on different origins.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. <!-- For more detailed information, check out the [contributing guidelines](CONTRIBUTING.md). -->

<!-- 
## License

This project is licensed under the MIT License. -->
