FROM node:11.14.0

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
RUN npm install -g @angular/cli@7.3.8
COPY . /usr/src/app
RUN cd /usr/
CMD npm install && ng serve --host 0.0.0.0 --port 4200 --disable-host-check