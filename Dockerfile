FROM python


COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY /app /app

COPY credentials.json .

ENV GOOGLE_APPLICATION_CREDENTIALS ./credentials.json
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000" ]

EXPOSE 3000