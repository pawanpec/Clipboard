import Record from '../../models/Record';
export default (req, res) => {
    Record.aggregate([
        {"$group": {
            "_id": "$department",
            "department_count": { "$sum": 1 }
        }},
        {$sort: {"department_count": -1}},
        {$limit: 10}
    ]).then((records) => {
        res.json({
            records: records,
            success: true,
        });
    }).catch((error) => {
        res.json({
            error,
            success: false,
        });
    });
};
