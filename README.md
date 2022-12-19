
# Account transaction summary
Account transaction summary was created as a coding challenge therefore **an email is not getting sent**, the program will just generate the body of the email in html format and will store it in **{path to folder}/data/email**. Likewise a sqlite database is generated in the folder **{path to folder}/data/db**

### How to execute
1. Clone the repository
```
git clone https://github.com/jpguitron/account-transaction-summary
```
2. Access the project folder
```
cd account-transaction-summary
```
3. With docker daemon initialized, build the docker image
```
docker build .
```
4. Get the docker image id
```
docker images
```
5. Execute the docker image
```
Windows
docker run -v %cd%/data:/app/data -e USER_ID=1 {image_id}
Linux/OSX
docker run -v $(pwd)/data:/app/data -e USER_ID=1 {image_id}
**For mounting data folder in OSX the path of data folder should be added to Preferences -> Resources -> File Sharing -> +**
```
User_id is the id of the user you want to process, the USER_ID should exist in the csv file, in the demo files the USER_ID 1,2 and 3 exist.
{image_id} should be changed to the image id that got created.

