## Dependencies
* Python 3.5
* Virtualenv
* Node.js (>= v6.0.0)
* mongodb >= 3.4.0
* Yarn

## Installation
* Set up a virtual enviroment with:
  ```bash
  virtualenv venv
  source venv/bin/activate
  ```
* Install python dependencies in requirements.txt by:
  ```bash
  pip install -r requirements.txt
  ```
* Install node dependencies with:
  ```bash
  npm install
  ```

### Running in development mode
1. Start webpack-dev-sever by typing ```npm start```
2. With your virtual enviroment enabled, run ```flask run``` and navigate to [localhost:5000](http://localhost:5000)

### Running in production mode
1. set `NODE_ENV=production` in your `.env` file
2. Compile webpack using ```npm run build```
3. With your virtual enviroment enabled, run ```flask run``` and navigate to [localhost:5000](http://localhost:5000)


1. ``` cp sample.env .env ``` and set values as appropriate.

2. Run `npm run forever-start` and navigate to `<ip>:<port> (default=7999)`.

###  Developing:
1. Set `NODE_ENV=development` in `.env`.
2. Run `npm run dev`

### API URL
1. What’s the average per hour salary
   http://localhost:4783/api/records/average
2.  What are the top 10 nursing departments
    http://localhost:4783/api/records/topDepartment
3.  What percentage of nurses have bachelor’s v. associate’s?
    http://localhost:4783/api/records/percentageBachelorNurse

squash1
squash2