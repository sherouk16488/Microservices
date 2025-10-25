import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Use PORT environment variable if available (Cloud Run sets this)
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

