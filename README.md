# Voice-based-age-detection-using-CNN

# Voice-Based Age Detection and Song Suggestion

## Project ID: PW20KKN01
**Project Type:** Minor  
**Project Title:** Voice-based Age Detection and Song Suggestion Based on Age Predicted  
**Team Members:** 
- G. Gautham (01FB16ECS118)
- D. Ganesh Kumar (01FB16ECS102)
- Chandhan Bhatta (01FB16ECS094)

**Project Guide:** Prof. Kavitha KN

## Project Abstract
With the rise of voice-based models, efficiently and accurately detecting age from voice samples presents significant opportunities. These analyzed voice samples can be used in a variety of applications, from demographic analytics to age-restricted access control. For this project, we focus on a song recommendation system that suggests songs based on the age predicted from the user's voice sample.

## Setup and Execution

### Prerequisites
- Python (with `virtualenv`)
- PostgreSQL
- Jupyter Notebook

### Dataset
The dataset can be downloaded from [Mozilla Common Voice](https://voice.mozilla.org/en). Due to its large size, it cannot be included in this repository.

### Step 1: Setting Up the Virtual Environment
Follow the instructions to create a Python virtual environment [here](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/).

1. Create and activate the virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Step 2: Data Preparation and Model Training
Use Jupyter Notebook to view and run the notebooks for data preparation, visualization, and model training.

### Step 3: Setting Up the Database
1. Install PostgreSQL and `psycopg2`:
    ```bash
    sudo apt-get install postgresql postgresql-contrib  # On Ubuntu
    pip install psycopg2
    ```

2. Open `pgAdmin4` from the Windows search bar. It will open in your web browser.

3. Enter the password you created during installation.

4. Create a new database named `SongRec`.

5. Create a table called `registration` with the following columns:
    - `username` (VARCHAR, length 40)
    - `password` (VARCHAR, length 40)
    - `age` (INTEGER)
    - `email` (VARCHAR, length 40)
    - `user_id` (SERIAL PRIMARY KEY)

### Step 4: Running the Application
Open two command prompts, one for the web server and the other for the prediction model.

1. **Web Server:**
    ```bash
    cd server
    python app.py
    ```
    Open your web browser and go to `http://localhost:5000`.

2. **Prediction Model:**
    ```bash
    cd server
    python app1.py > age.txt
    ```
    Ensure the `age.txt` file is placed inside the server folder.

### Step 5: Using the Application
1. Go to the registration page to create a new user account.
2. Log in using the registered credentials.
3. You will be prompted to record your voice. Record a voice sample for more than 2 seconds.
4. Upload the recorded file to the server.
5. The system will analyze the voice and update the `age.txt` file.
6. Click on the upload button to display a list of recommended songs.
7. Click on a song to play it.
