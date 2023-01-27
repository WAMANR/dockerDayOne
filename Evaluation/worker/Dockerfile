FROM node:14-alpine

WORKDIR /evaluation

COPY ./worker/package.json .
RUN npm install

COPY . .

CMD [ "node", "./worker/main" ]