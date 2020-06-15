const path = require('path');
const webpack = require('webpack');

const OUTPUT_DIR = path.resolve(__dirname, '../../static/django_comments_xtd/js');
const SOURCE_DIR = path.resolve(__dirname, 'src');

module.exports = {
  mode: "production",
  devtool: 'source-map',
  entry: {
    plugin: path.resolve(SOURCE_DIR, 'index.js')
  },
  output: {
    filename: '[name]-2.6.1.js',
    path: OUTPUT_DIR
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        default: false,
        vendors: false,
        vendor: {
          chunks: 'all',
          test: /node_modules/
        }
      }
    },
    minimize: true
  },
  module: {
    rules: [
      {
        test: /\.jsx?/,
        include: SOURCE_DIR,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  externals: {
    bootstrap: 'bootstrap',
    django: 'django',
    jquery: 'jQuery',
    react: 'React',
    'react-dom': 'ReactDOM'
  }
};
