# Use Node.js base image for frontend
FROM node:18 as frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend .
RUN npm run build

# Use Python base image for backend
FROM python:3.9-slim
WORKDIR /app
COPY --from=frontend /app/frontend/dist /app/frontend/dist
COPY backend /app/backend
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/backend/main.py"]