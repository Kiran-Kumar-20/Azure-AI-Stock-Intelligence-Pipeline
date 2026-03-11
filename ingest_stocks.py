import os
import pandas as pd
import yfinance as yf
from azure.storage.blob import BlobServiceClient
from io import StringIO

# CONFIGURATION
# SECURITY NOTE: Do not hardcode connection strings in public repositories.
# Use Environment Variables or Azure Key Vault for production.
CONNECTION_STRING = "YOUR_AZURE_STORAGE_CONNECTION_STRING" 
CONTAINER_NAME = "bronze"
TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA']

def upload_to_azure(data, filename):
    try:
        # Initializing the client using the connection string
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=filename)
        blob_client.upload_blob(data, overwrite=True)
        print(f"✅ Uploaded {filename} to Azure.")
    except Exception as e:
        print(f"❌ Failed to upload {filename}: {e}")

def fetch_and_upload():
    print("🚀 Starting Data Ingestion...")
    
    for ticker in TICKERS:
        print(f"Fetching data for {ticker}...")
        
        # 1. Fetch Data (1 Year History)
        df = yf.download(ticker, period="1y", interval="1d")
        
        # 2. Data Cleaning for raw ingest
        df.reset_index(inplace=True)
        # Add a column for the Ticker name (Crucial for analysis later)
        df['Ticker'] = ticker
        
        # 3. Convert to CSV string
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        
        # 4. Upload
        filename = f"{ticker}_raw.csv"
        upload_to_azure(csv_buffer.getvalue(), filename)

    print("🎉 Ingestion Complete!")

if __name__ == "__main__":
    fetch_and_upload()