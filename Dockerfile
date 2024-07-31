#This will get the python installed
FROM python:3.9-slim 

#This will setup the working directory in the container
WORKDIR /app 

#This will copy the requirements file into the container
COPY requirements.txt . 

#Copy rest of the code into the container
COPY src ./src 
COPY static ./satic
COPY template ./template
COPY src/Chain/app.py .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.Chain.app:app", "--host", "0.0.0.0", "--port", "8000"]