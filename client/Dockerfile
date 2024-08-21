FROM node:lts-alpine AS build

WORKDIR /usr/src/app

RUN npm install -g pnpm

# Copy package.json and package-lock.json
COPY package.json ./
COPY pnpm-lock.yaml ./

RUN pnpm install --frozen-lockfile 

COPY . .

RUN pnpm run build

FROM nginx:stable-alpine

COPY --from=build /usr/src/app/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /usr/src/app/dist /usr/share/nginx/html

COPY /etc/letsencrypt/live/terre.rhamzthev.com/fullchain.pem /etc/ssl/certs/fullchain.pem
COPY /etc/letsencrypt/live/terre.rhamzthev.com/privkey.pem /etc/ssl/private/privkey.pem

EXPOSE 80
EXPOSE 443