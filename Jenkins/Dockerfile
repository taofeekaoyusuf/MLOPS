# Base Image with Node.js (Alpine is small and efficient)
FROM node:24-alpine

# Set environment variables
ENV NETLIFY_CLI_VERSION latest

# Install bash, git, curl, and necessary tools
RUN apk update && \
    apk add --no-cache \
    bash \
    git \
    curl \
    bash-completion \
    && rm -rf /var/cache/apk/*

# Install Netlify CLI globally
RUN npm install -g netlify-cli@$NETLIFY_CLI_VERSION

# Verify installations
RUN node --version && \
    npm --version && \
    netlify --version && \
    git --version && \
    bash --version

# Set default shell to bash (optional but helpful)
SHELL ["/bin/bash", "-c"]

# Default work directory
WORKDIR /workspace

# Default command (optional)
CMD ["bash"]