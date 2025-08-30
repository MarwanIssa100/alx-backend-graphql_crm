"""
CRM Cron Jobs
This module contains functions that can be executed by django-crontab.
"""

import os
import sys
from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    """
    Logs a heartbeat message to indicate CRM is alive.
    Optionally queries GraphQL hello field to verify endpoint responsiveness.
    """
    
    # Get current timestamp in DD/MM/YYYY-HH:MM:SS format
    timestamp = datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    
    # Log file path
    log_file = '/tmp/crm_heartbeat_log.txt'
    
    # Create heartbeat message
    heartbeat_message = f"{timestamp} CRM is alive"
    
    try:
        # Append to log file (does not overwrite)
        with open(log_file, 'a') as f:
            f.write(heartbeat_message + '\n')
        
        # Optionally query GraphQL hello field to verify endpoint is responsive
        try:
            # GraphQL endpoint
            graphql_endpoint = "http://localhost:8000/graphql"
            
            # GraphQL query for hello field
            query = gql("""
                query {
                    name
                }
            """)
            
            # Create GraphQL client
            transport = RequestsHTTPTransport(url=graphql_endpoint)
            client = Client(transport=transport, fetch_schema_from_transport=True)
            
            # Execute the query
            result = client.execute(query)
            
            # Log successful GraphQL query
            graphql_status = f"{timestamp} GraphQL endpoint responsive: {result.get('name', 'No response')}"
            with open(log_file, 'a') as f:
                f.write(graphql_status + '\n')
                
        except Exception as graphql_error:
            # Log GraphQL error but don't fail the heartbeat
            graphql_error_msg = f"{timestamp} GraphQL endpoint error: {str(graphql_error)}"
            with open(log_file, 'a') as f:
                f.write(graphql_error_msg + '\n')
    
    except Exception as e:
        # If we can't write to log file, print to stderr
        print(f"Error writing heartbeat log: {str(e)}", file=sys.stderr)
        sys.exit(1)
