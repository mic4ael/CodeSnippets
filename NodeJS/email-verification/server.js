var express = require('express');
var bodyParser = require('body-parser');
var nodeMailer = require('nodemailer');
var redis = require('redis');
var async = require('async');
var mandrillTransport = require('nodemailer-mandrill-transport');

var app = express();
var host = 'localhost:3000';
var redisClient = redis.createClient(6379, 'redis');

var smtpTransport = nodeMailer.createTransport(mandrillTransport({
    auth: {
        apiKey: ''
    }
}));

app.use(bodyParser.urlencoded({'extended': false}));

app.get('/', function(req, res) {
    res.sendfile('index.html');
});

app.post('/send', function(req, res) {
    async.waterfall([
        function(callback) {
            redisClient.exists(req.body.to, function(err, reply) {
                if (err) {
                    return callback(true, 'Error in redis');
                }

                if (reply === 1) {
                    return callback(true, 'Email already requested');
                }

                callback(null);
            });
        },
        function(callback) {
            var rand = Math.floor((Math.random() * 100) + 54);
            var encodedMail = new Buffer(req.body.to).toString('base64');
            var link = `http://${req.get('host')}/verify?mail=${encodedMail}&id=${rand}`
            var mailOptions = {
                from: 'no-reply@gmail.com',
                to: req.body.to,
                subject: "Please confirm your Email account",
                html: "Hello,<br> Please Click on the link to verify your email.<br><a href="+link+">Click here to verify</a>"
            }
            callback(null, mailOptions, rand);
        },
        function(mailData, secretKey, callback) {
            smtpTransport.sendMail(mailData, function(error, response) {
                if (error) {
                    console.log(error);
                    return callback(true, "Error when sending an email");
                }

                redisClient.set(req.body.to, secretKey);
                redisClient.expire(req.body.to, 600);
                callback(null, "Email has been sent");
            })
        }
    ], function(err, data) {
        res.json({error: !!err, data: data});
    });
});

app.get('/verify', function(request, response) {
    if (req.get('host') === host) {
        async.waterfall([
            function(callback) {
                var decodedMail = new Buffer(request.query.mail, 'base64').toString('ascii');
                redisClient.get(decodedMail, function(error, reply) {
                    if (error) {
                        return callback(true, 'error in redis');
                    }
                    if (reply === null) {
                        return callback(true, 'invalid email address');
                    }
                    callback(null, decodedMail, reply);
                });
            },
            function(key, redisData, callback) {
                if (redisData === request.query.id) {
                    redisClient.del(key, function(error, reply) {
                        if (error) {
                            return callback(true, 'Error in redis');
                        }
                        if (reply !== 1) {
                            return callback(true, 'Issue in redis');
                        }
                        callback(null, 'Email is verified');
                    })
                } else {
                    return callback(true, 'ivalid token');
                }
            }
        ], function(error, data) {
            response.send(data);
        });
    } else {
        response.end('<h1>Request is from unknown source</h1>')
    }
});

app.listen(3000, function() {
    console.log('Express started on port 3000');
})
