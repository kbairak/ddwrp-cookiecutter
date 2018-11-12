FROM postgres:11-alpine
ENV PGDATA=/data
COPY db/init.sql /docker-entrypoint-initdb.d/
