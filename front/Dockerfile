FROM node:alpine

ENV PORT 3000

RUN mkdir -p /code/

WORKDIR /code

COPY ./yarn.lock ./package.json ./

RUN npm install --no-optional

EXPOSE 3000

CMD ["yarn", "dev"]
