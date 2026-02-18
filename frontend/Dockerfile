FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

RUN adduser --disabled-password --gecos "" --no-create-home appuser && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
