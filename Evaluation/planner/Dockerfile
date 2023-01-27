FROM node:14-alpine

WORKDIR /evaluation

COPY ./planner/package.json .
RUN npm install

COPY . .

CMD [ "node", "./planner/main" ]