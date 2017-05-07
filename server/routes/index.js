/* eslint-disable global-require */
import 'dotenv/config';
import reactApp from './views/app';
const recordService=require('./api/records');
const averageService=require('./api/average');
const departmentService=require('./api/department');
const edcationService=require('./api/educationService');
const routes = (app) => {

  /* example api route */
    app.get('/api/records',recordService );
    app.get('/api/records/average',averageService);
    app.get('/api/records/topDepartment',departmentService);
    app.get('/api/records/percentageBachelorNurse',edcationService);

    reactApp(app); // set up react routes
};

export default routes;
/* eslint-enable global-require */
