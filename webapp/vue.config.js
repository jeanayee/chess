// vue.config.js
module.exports = {
  configureWebpack: {
    output: {
      globalObject: "this"
    }
  }
  /* plugins: [
    new webpack.LoaderOptionsPlugin({
      // test: /\.xxx$/, // may apply this only for some modules
      options: {
        publicPath: "/static/"
      }
    })
  ] */
};
