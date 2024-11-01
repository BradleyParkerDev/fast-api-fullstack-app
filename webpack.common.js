const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    devtool: 'source-map',
    entry: {
        main: path.resolve(__dirname, 'resources/ts/main.ts'),            // Main shared entry
        homePage: path.resolve(__dirname, 'resources/ts/pages/homePage.ts'),    // Entry for homepage
        userPage: path.resolve(__dirname, 'resources/ts/pages/userPage.ts'),    // Entry for userpage
        authenticatedUserPage: path.resolve(__dirname, 'resources/ts/pages/authenticatedUserPage.ts')  // Entry for authenticated user page
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.css$/,
                include: path.resolve(__dirname, "resources/css"),
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'postcss-loader',
                ],
            },
        ],
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.jsx', '.js'],
    },
};
