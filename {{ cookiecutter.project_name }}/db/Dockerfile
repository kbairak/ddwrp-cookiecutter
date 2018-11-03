FROM postgres:11
ENV PGDATA=/data
COPY db/init.sql /docker-entrypoint-initdb.d/
