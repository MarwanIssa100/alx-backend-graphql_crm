# CRM Cron Jobs

This directory contains automated scripts for maintaining the CRM system.

## clean_inactive_customers.sh

This script automatically removes customers who have not placed any orders in the last year.

### Features

- Uses Django's `manage.py shell` to execute Python commands
- Deletes customers with no orders since a year ago
- Logs all activities with timestamps to `/tmp/customer_cleanup_log.txt`
- Includes error handling and validation
- Automatically handles the Django project directory detection

### Usage

1. **Manual execution:**
   ```bash
   ./crm/cron_jobs/clean_inactive_customers.sh
   ```

2. **Set up as a cron job:**
   ```bash
   # Edit crontab
   crontab -e
   
   # Add this line to run daily at 2 AM
   0 2 * * * /path/to/your/project/crm/cron_jobs/clean_inactive_customers.sh
   ```

### Requirements

- Django project with Customer and Order models
- Proper database migrations applied
- Script must be executable (`chmod +x`)

### Log File

The script logs all activities to `/tmp/customer_cleanup_log.txt` with timestamps:
```
2024-01-15 14:30:00 - Starting customer cleanup script
2024-01-15 14:30:01 - Executing Django shell command
2024-01-15 14:30:02 - Successfully completed customer cleanup. Deleted 5 customers.
2024-01-15 14:30:02 - Customer cleanup script completed
```

### Model Requirements

The script expects the following Django models:

- **Customer**: Linked to Django User model with OneToOneField
- **Order**: Linked to Customer with ForeignKey and includes `created_at` field

### Safety Features

- Validates Django project directory before execution
- Logs all operations with timestamps
- Handles errors gracefully
- Provides detailed output of operations performed

### Customization

You can modify the script to:
- Change the inactivity period (currently 365 days)
- Add additional filtering criteria
- Modify the log file location
- Add email notifications for cleanup results
