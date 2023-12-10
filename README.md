# DashBoard Angular-Flask Project

This project demonstrates the integration of Angular with Flask for creating a web application to display data from Excel files in a pie chart.

## Overview

The project comprises two main components: Angular frontend and Flask backend. Angular is used for the frontend development, handling UI components, and making API requests to the Flask backend. Flask serves as the backend server, providing APIs to retrieve data from Excel files and prepare it for visualization in the frontend.

### Technologies Used

- Angular (Frontend)
- TypeScript
- HTML/CSS
- Angular Material
- Flask (Backend)
- Python
- Pandas library for data manipulation

## Project Structure

The project structure consists of the following components:

- `frontend/`: Angular application
  - `src/app`: Contains components, services, and modules for frontend functionality.
  - `src/app/components`: Angular components like `AppComponent`, `PiechartComponent`.
  - `src/app/services`: Angular services handling API requests.
- `backend/`: Flask application
  - `app.py`: Backend code using Flask to serve APIs.
  - `Data/`: Folder containing Excel files with data.

## Setup Instructions

### Frontend (Angular)

1. Navigate to the `frontend/` directory.
2. Install dependencies: `npm install`
3. Start the Angular development server: `ng serve`

### Backend (Flask)

1. Navigate to the `backend/` directory.
2. Create a virtual environment (optional but recommended).
3. Install Flask and required dependencies: `pip install flask pandas flask-cors`
4. Run the Flask server: `python app.py`

## Usage

1. Access the Angular application by visiting `http://localhost:4200` in a web browser.
2. Use the provided components to navigate, select an Excel file, and visualize data in a pie chart.
3. The frontend sends requests to the Flask backend to retrieve and process data from Excel files.

## Screenshot

![Application Screenshot](/Dashboard_img.PNG)

![Application Screenshot](/Dashboard_img_2.PNG)

![Application Screenshot](/Dashboard_img_3.PNG)
