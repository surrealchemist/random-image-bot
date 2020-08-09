This is a witter bot written to be used in AWS.

You will need to create a twitter developer account to get an API Key pair, then create a new Access Token pair with read/write permissions and set the environment variables.

**BUCKET_NAME** the source bucket where the images reside
**APP_KEY** Twitter API Key
**APP_SECRET** Twitter API secret
**OAUTH_TOKEN** Access Token with read/write permissions
**OAUTH_TOKEN_SECRET** Access Secret with read/write permissions



# TODO:

Wrap in serverless or SAM to make deploying easier and manage permissions

Add DB support and ability to avoid repeats

Add method to automatically trigger execution on schedule

Better file handling for larger sets of buckets (Right now it just does a random on the whole bucket list and I don't know how well that even will work or what the limits are because I haven't researched it)

