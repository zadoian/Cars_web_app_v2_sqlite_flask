
# Car Management System

This is a Flask-based web application that allows users to manage customer car information. The application allows users to add new customers and their cars, edit existing records, view all cars in the database, search for specific cars, and delete records. The app stores car data in an SQLite database (`cars.db`).

## Features

- **Add Customer and Car:** Users can add new customers along with their car details (color and brand).
- **Edit Car Details:** Users can edit the details of a car (color and brand) for an existing customer.
- **View All Cars:** Users can view a list of all cars and their respective owners.
- **Search Cars:** Users can search for specific cars by the customer name, car color, and brand.
- **Delete Car:** Users can delete a car record from the database.

## Project Structure

```
car_management_web_app/
│
├── static/
│   └── css/
│       └── style.css        # Custom CSS for the application
│
├── templates/
│   ├── base.html            # Base HTML template
│   ├── index.html           # Home page
│   ├── cars.html            # Shows all cars
│   ├── add_customer.html    # Form to add new customer and car
│   ├── edit_car.html        # Form to edit car details
│   ├── search_car.html      # Form to search for cars
│   ├── search_results.html  # Display search results
│   └── delete_car.html      # Confirm deletion
│
├── cars.db                  # SQLite database (created after running the app)
├── app.py                   # Main Flask application
└── init_db.py               # Database initialization script
```

## Getting Started

### Prerequisites

Ensure that you have the following installed on your machine:
- Python 3.x
- Flask (`pip install flask`)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/car_management_web_app.git
   cd car_management_web_app
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask
   ```

4. **Initialize the database:**

   Run the following command to create the SQLite database and the `Cars` table:
   ```bash
   python init_db.py
   ```

   This will generate a `cars.db` file in the root directory of the project.

5. **Run the Flask application:**
   ```bash
   python app.py
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000/`.

### Application Usage

- **Home Page:**
  From the home page, you can navigate to various sections such as adding new customers, viewing cars, searching for cars, and managing the records.

- **Add Customer and Car:**
  Fill in the customer name, car color, and brand, and submit the form to add a new record.

- **View All Cars:**
  Navigate to the "View Cars" page to see all cars stored in the database. You can edit or delete cars from this view.

- **Edit Car Details:**
  In the car list, click "Edit" next to a car record to update the car's details.

- **Delete Car:**
  In the car list, click "Delete" next to a car record to remove it from the database.

- **Search for Cars:**
  Use the search page to search for specific cars by entering the customer name, car color, and brand.

### Customization

- **Styling:**
  You can modify the CSS in `static/css/style.css` to change the look and feel of the application.
  
- **Database Modifications:**
  You can modify the `Cars` table structure by editing `init_db.py`. After changes, run `init_db.py` again to update the schema.

## Technologies Used

- **Python**: The core programming language used for the application.
- **Flask**: The micro web framework used to handle routing and rendering HTML pages.
- **SQLite**: The database used to store customer and car data.
- **HTML/CSS**: For the frontend, including templates and styling.

## Future Improvements

- Add authentication to limit access to certain functionalities.
- Implement additional search features (e.g., partial name matching, filtering by brand).
- Add pagination to the "View Cars" page for better handling of large datasets.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
