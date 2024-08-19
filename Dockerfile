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

COPY --from=build usr/src/app/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build usr/src/app/dist /usr/share/nginx/html

EXPOSE 80