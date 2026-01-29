FROM alpine:latest
WORKDIR /app
COPY peaks-scheduler /usr/local/bin/peaks-scheduler
RUN chmod +x /usr/local/bin/peaks-scheduler
ENTRYPOINT ["/usr/local/bin/peaks-scheduler"]

