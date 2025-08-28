# English Test Project

This is a web application, developed with Django, to assess English language proficiency. It allows users to take dynamically generated tests based on customizable grammar topics and difficulty levels, and provides them with a detailed results breakdown.

### Features
- Dynamic test generation based on selected level (A1, A2, etc.) and topic priorities.
- Real-time score calculation for each topic and a final overall score.
- A timer to track the time spent on the test.
- Automated ordering and numbering of questions based on a given topic.
- User test results are saved in the database for future reference.
- Responsive design that works well on various devices.

### Technologies Used
- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite3
- **Version Control:** Git, GitHub

### Installation and Setup
1.  **Clone the repository**
    * `git clone https://github.com/Maryna-cell/english-test-project.git`
    * `cd english-test-project`
2.  **Set up the virtual environment**
    * `python -m venv venv`
    * `source venv/bin/activate` (for macOS/Linux) or `venv\Scripts\activate` (for Windows)
3.  **Install dependencies**
    * `pip install -r requirements.txt`
4.  **Database migrations**
    * `python manage.py makemigrations`
    * `python manage.py migrate`
5.  **Run the server**
    * `python manage.py runserver`
    * The application will be available at: `http://127.0.0.1:8000/`

### Screenshots / Demo
- A screenshot of the test results page .
  
  <img width="307" height="446" alt="зображення" src="https://github.com/user-attachments/assets/a8d8406b-20c0-46dc-8948-7d4cc258beb6" />

- A screenshot of the project's file structure .
  
- <img width="348" height="824" alt="зображення" src="https://github.com/user-attachments/assets/2e0b991b-910d-4c3b-bc85-8e5bf0db49eb" />


### Author and Contact
- **Author:** Maryna
- **GitHub:** [https://github.com/Maryna-cell](https://github.com/Maryna-cell)
