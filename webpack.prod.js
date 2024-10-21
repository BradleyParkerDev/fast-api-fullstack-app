const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const { WebpackManifestPlugin } = require('webpack-manifest-plugin'); // Import the WebpackManifestPlugin
const {merge} = require('webpack-merge')
const common = require("./webpack.common")

module.exports = merge(common, {
    mode: 'production',
    output: {
        path: path.resolve(__dirname, 'public/build/'),
        filename: 'js/[name].[contenthash].bundle.js', // JS files with content hash for cache busting
        clean: true, // Clean the output directory before each build
    },
    plugins: [
        new CleanWebpackPlugin(), 
        new MiniCssExtractPlugin({
            filename: 'css/[name].[contenthash].css', // CSS files with content hash for cache busting
        }),
        new WebpackManifestPlugin({
            fileName: 'manifest.json', // Name of the manifest file
            publicPath: '/public/build/', // Specify the public path
        }),        
    ],
})
