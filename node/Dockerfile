FROM node:slim

RUN apt-get update -y && apt-get install -y openssl

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

RUN npx prisma generate

CMD ["sh", "-c", "npx prisma db push && npm start"]
