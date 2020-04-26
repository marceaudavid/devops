FROM mariadb

ENV MYSQL_DATABASE=database
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=password
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_HOST=mariadb

ADD setup.sql /docker-entrypoint-initdb.d
