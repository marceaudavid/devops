FROM mariadb

ENV MYSQL_DATABASE=devops
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=password
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_HOST=mariadb

# COPY my.cnf /etc/mysql/my.cnf
# COPY keyfile.enc /etc/mysql/encryption/keyfile.enc
# COPY keyfile.key /etc/mysql/encryption/keyfile.key

ADD setup.sql /docker-entrypoint-initdb.d