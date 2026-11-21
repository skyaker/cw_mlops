FROM python:3.11-slim

WORKDIR /app

COPY model_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bank_marketing_logreg.joblib .
COPY model_service/app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
