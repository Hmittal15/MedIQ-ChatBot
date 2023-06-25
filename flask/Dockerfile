FROM python:3.11.1

# Pull the base docker image of python with tag 3.11.1

RUN pip install --upgrade pip

WORKDIR /app
# Change the working dir inside the container - cd /app

ADD main.py /app/
ADD intents.json /app/
ADD requirements.txt /app/
ADD tokenizer.pickle /app/
ADD label_encoder.pickle /app/
ADD chat_model /app/chat_model/
ADD chat_model/assets /app/chat_model/
ADD chat_model/variables /app/chat_model/
ADD chat_model/variables/variables.data-00000-of-00001 /app/chat_model/variables
ADD chat_model/variables/variables.index /app/chat_model/variables
ADD chat_model/fingerprint.pb /app/chat_model/
ADD chat_model/keras_metadata.pb /app/chat_model/
ADD chat_model/saved_model.pb /app/chat_model/

RUN pip install -r requirements.txt
# Install the dependency

### Container Env same as local at this point

EXPOSE 8090

CMD ["python", "main.py"]