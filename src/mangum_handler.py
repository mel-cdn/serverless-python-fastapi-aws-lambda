from mangum import Mangum

from main import app

# Mangum handler for AWS Lambda deployment
handler = Mangum(app)
