var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

const extractCSS = new ExtractTextPlugin('[name].css');

module.exports = {
    entry: [
        './app/index.js',
        './web/assets/css/bootstrap.css'
    ],
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [{
            test: /\.css$/,
            include: path.resolve(__dirname, 'web/assets/css'),
            use: extractCSS.extract(['css-loader'])
        }]
    },
    plugins: [
        extractCSS
    ]
};
