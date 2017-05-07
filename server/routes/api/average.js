import Record from '../../models/Record';

export default (req, res) => {
    Record.aggregate({
        "$group": {
            "_id": null,
            "avg_sal": { "$avg": "$stdval" }
        }
    }).then((records) => {
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
