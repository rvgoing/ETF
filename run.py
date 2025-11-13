"""
Entry point for the Flask application.
Run this file to start the development server.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import app after loading environment variables
from app import app

if __name__ == '__main__':
    # Get configuration from environment variables
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"🚀 Starting Flask Application")
    print(f"📍 Server: http://{host}:{port}")
    print(f"🔧 Debug Mode: {debug}")
    print(f"💡 Press CTRL+C to stop the server\n")
    
    app.run(host=host, port=port, debug=debug)
