When implementing a new setup, such as configuring a cluster of PostgREST servers with NGINX as a reverse proxy and securing connections with SSL certificates from Certbot, it's crucial to consider the impact on your running system. The process itself is designed to be non-destructive, but certain precautions are necessary to ensure smooth integration without disrupting existing services.

1. **Port Assignments**: Ensure new PostgREST instances do not conflict with other services by using unique ports.

2. **NGINX Configuration**: Modify NGINX configurations cautiously, creating backups of current files before changes.

3. **SSL Certificates**: Using Certbot to obtain SSL certificates modifies NGINX server blocks to handle HTTPS. This should enhance security without affecting existing configurations.

4. **Database Connection**: Multiple PostgREST instances will connect to the same database. Ensure your database can handle this without issues.

5. **Backup and Rollback Plan**: Always have a backup of configurations and data, and a plan for rolling back changes if necessary.

6. **Testing**: Test changes in a staging environment before applying them to production to identify any potential issues.

By following these guidelines, you can ensure that the setup process adds to your system without destructive changes, keeping your services running smoothly while implementing new configurations.