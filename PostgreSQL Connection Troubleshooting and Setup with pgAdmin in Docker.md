# PostgreSQL Connection Troubleshooting and Setup with pgAdmin in Docker

This user story outlines the troubleshooting and setup process for connecting pgAdmin in Docker to a PostgreSQL database, addressing common issues such as authentication errors, network configurations, and SSL setup.

## Troubleshooting Steps

1. **Verify PostgreSQL Service is Running**

```bash
sudo systemctl status postgresql
```

2. **Ensure PostgreSQL is Configured to Listen Correctly**

```bash
sudo nano /etc/postgresql/12/main/postgresql.conf
```

Set `listen_addresses = '*'`.

3. **Adjust `pg_hba.conf` for Docker Connections**

```bash
sudo nano /etc/postgresql/12/main/pg_hba.conf
```

Add entries to allow connections from Docker.

4. **Restart PostgreSQL**

```bash
sudo systemctl restart postgresql@12-main.service
```

5. **Connect Using pgAdmin**

Update pgAdmin Server Configuration with the host's IP address.

## Connection Issues

Encountered "connection refused" and "no pg_hba.conf entry" errors. Adjusted `pg_hba.conf` to use `md5` for password authentication.

## Final Resolution

After correctly configuring `pg_hba.conf` and ensuring PostgreSQL listens on the appropriate interfaces, the connection from pgAdmin to the PostgreSQL database was successfully established.

## Command Line Logs

Reviewed PostgreSQL logs to identify and address errors:

```bash
sudo less /var/log/postgresql/postgresql-12-main.log
```

The logs indicated issues with the PostgreSQL configuration and provided clues for the necessary adjustments to resolve connection problems.
