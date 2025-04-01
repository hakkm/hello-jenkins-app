FROM jenkins/jenkins:2.492.2-jdk17

# Switch to root user for system-level installations
USER root

# Set root password
RUN echo 'root:j' | chpasswd

# Update apt and install basic utilities
RUN apt-get update && apt-get install -y \
    lsb-release \
    ca-certificates \
    curl \
    vim \
    ranger \
    && rm -rf /var/lib/apt/lists/*

# Install Docker CLI (separate layer for caching)
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
    chmod a+r /etc/apt/keyrings/docker.asc && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
    https://download.docker.com/linux/debian $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" \
    | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && apt-get install -y docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# Install Jenkins plugins (separate step for caching)
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"

# Switch back to jenkins user after installation
USER jenkins
