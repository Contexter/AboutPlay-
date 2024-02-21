Setting up a cluster of PostgREST servers pointing to the same PostgreSQL instance, with NGINX as a reverse proxy and using Certbot for SSL certificates, involves several steps. Below is a step-by-step guide tailored for an Ubuntu 20.04 machine. Ensure you have root or sudo privileges to execute these steps.

### 1. Configure PostgREST Instances

You'll create configuration files for each PostgREST instance. Assuming you've already installed PostgREST and have one instance running, you'll clone the configuration for additional instances.

1. **Create Configuration Files**:
   
   For each PostgREST instance (api-1 to api-10), create a copy of your existing PostgREST configuration file, adjusting the port number for each so they don't conflict:
   
   ```bash
   for i in {1..10}; do
       cp /etc/postgrest/config api-$i.conf
       sed -i 's/port=3000/port=300$i/' api-$i.conf
   done
   ```
   
   Adjust `port=3000` to the actual port in your original config file, and increment ports accordingly (e.g., 3001 for api-1, 3002 for api-2, etc.).

2. **Start PostgREST Instances**:

   Use a process manager like `systemd` to manage your PostgREST instances. Create a systemd service file for each instance:
   
   ```bash
   for i in {1..10}; do
       cat <<EOF > /etc/systemd/system/postgrest-api-$i.service
       [Unit]
       Description=PostgREST API-$i Service
       
       [Service]
       ExecStart=/usr/local/bin/postgrest /etc/postgrest/api-$i.conf
       
       [Install]
       WantedBy=multi-user.target
       EOF

       systemctl enable postgrest-api-$i
       systemctl start postgrest-api-$i
   done
   ```
   
   Replace `/usr/local/bin/postgrest` with the path to your PostgREST executable if different.

### 2. NGINX Configuration

You'll configure NGINX to reverse proxy requests to the PostgREST instances. 

1. **Install NGINX and Certbot**:

   If NGINX and Certbot aren't installed:

   ```bash
   sudo apt update
   sudo apt install nginx certbot python3-certbot-nginx
   ```

2. **Configure NGINX**:

   For each API endpoint, create an NGINX server block:

   ```bash
   for i in {1..10}; do
       cat <<EOF > /etc/nginx/sites-available/api-$i.benedikt-eickhoff.de
       server {
           listen 80;
           server_name api-$i.benedikt-eickhoff.de;

           location / {
               proxy_pass http://localhost:300$i;
               proxy_set_header Host \$host;
               proxy_set_header X-Real-IP \$remote_addr;
               proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
               proxy_set_header X-Forwarded-Proto \$scheme;
           }
       }
       EOF

       ln -s /etc/nginx/sites-available/api-$i.benedikt-eickhoff.de /etc/nginx/sites-enabled/
   done

   nginx -t
   systemctl reload nginx
   ```

   Ensure the `proxy_pass` directive points to the correct port for each PostgREST instance.

3. **Obtain SSL Certificates**:

   Use Certbot to obtain an SSL certificate for each domain:

   ```bash
   for i in {1..10}; do
       certbot --nginx -d api-$i.benedikt-eickhoff.de
   done
   ```

   Follow the prompts to complete the certification process, which will automatically adjust your NGINX configuration to serve content over HTTPS.

### 3. Recommendations

- **Security**: Ensure your PostgreSQL database and PostgREST configurations are secured, especially in terms of authentication and permissions.
- **Monitoring**: Consider setting up monitoring for your PostgREST instances and NGINX to track performance and uptime (e.g., with Prometheus and Grafana).
- **Logging**: Ensure NGINX and PostgREST logs are correctly configured for debugging and monitoring access and errors.
- **Scaling**: For scaling beyond this setup, consider using a load balancer in front of NGINX or cloud services that can manage load balancing and SSL termination for you.

This setup will route requests to `https://api-1.benedikt-eickhoff.de` through `https://api-10.benedikt-eickhoff.de` to your PostgREST instances, leveraging NGINX for reverse proxying and SSL termination.