import Record from '../../models/Record';
var Promise = require('bluebird');
export default (req, res) => {
    function getNurseByEducation(input) {
        return new Promise(function (resolve, reject) {
            Record.find({education: input})
                .then(function (result) {
                    return resolve(result.length);
                })
                .catch(function (error) {
                    reject(error);
                });
        });
    }
    return new Promise(function (resolve, reject) {
        Promise
            .resolve([
                getNurseByEducation('Bachelors'),
                getNurseByEducation('Associates')
            ])
            .spread(function (bachelors, associates) {
                var per = bachelors * 100 / (bachelors + associates);
                res.json({
                    percentAgeOfBachelorsNurse: per,
                    success: true,
                });
            })
    });
};
