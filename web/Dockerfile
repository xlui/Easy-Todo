FROM node:8-alpine AS builder
COPY . /data
WORKDIR /data
RUN yarn install && yarn build && yarn cache clean

FROM nginx:1.15-alpine
COPY --from=builder  /data/dist/* /usr/share/nginx/html/
CMD ["nginx", "-g", "daemon off;"]
