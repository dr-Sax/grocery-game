FROM node:18 as frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
RUN npm install vue3-google-map
COPY frontend .
RUN npm run build

FROM python:3.9-slim
WORKDIR /app
COPY --from=frontend /app/frontend/dist /app/frontend/dist
COPY backend /app/backend
COPY requirements.txt .
RUN pip install -r requirements.txt gunicorn
RUN ls -la /app/frontend/dist && cat /app/frontend/dist/index.html
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "backend.main:app"]