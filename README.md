# account-transaction-summary
System for processing transactions from a csv file
Windows instructions
docker run -v %cd%/data:/app/data -i -t <image_id> /bin/bash

Linux/OSX instructions
docker run -v $(pwd)/data:/app/data -i -t <image_id> /bin/bash