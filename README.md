# query-generator-generator

### Install **virtualenv** using pip3

    sudo pip3 install virtualenv

### Now create a virtual environment

    python3 -m venv venv

### Active your virtual environment and install the required libraries:    

    source venv/bin/activate
    pip  install -r requirements.txt

### Give dig.sh executable permission:

    chmod +x dig.sh

### Now run dig.sh with following command:

    ./dig.sh 30 "127.0.0.1" 1
    # Here Number of queries per minute=30, Resolver="127.0.0.1"
    # Dig time period in minutes=1
