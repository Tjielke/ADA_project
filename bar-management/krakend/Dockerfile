# Use Krakend as the base image
FROM devopsfaith/krakend:2.6.0

# Install curl
RUN apk update && apk add curl

# Copy the Krakend configuration file
COPY krakend.json /etc/krakend/krakend.json

# Expose the Krakend port
EXPOSE 8081

# Run Krakend
CMD ["krakend", "run", "-c", "/etc/krakend/krakend.json"]
