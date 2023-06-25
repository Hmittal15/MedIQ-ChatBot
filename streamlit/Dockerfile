FROM python:3.11.1

# Pull the base docker image of python with tag 3.9.0

RUN python -m pip install --upgrade pip

WORKDIR /app
# Change the working dir inside the container - cd /app

ADD pages /app/pages/

ADD pages/app.py /app/pages/
ADD home.py health_bg.jpg requirements.txt /app/

RUN pip install -r requirements.txt
# Install the dependency

RUN pip install streamlit --upgrade

### Container Env same as local at this point

EXPOSE 8000

CMD ["streamlit", "run", "home.py", "--server.port", "8000"]