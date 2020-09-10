"use strict";
class CustomPlugin {
  constructor(serverless) {
    this.serverless = serverless;
    this.provider = this.serverless.getProvider("aws");
    this.hooks = {
      "after:deploy:deploy": () => this.invokeAggregator(),
    };
  }
  invokeAggregator() {
    this.provider.request("Lambda", "invoke", {
      FunctionName: "video-game-sales-dev-aggregate_data",
    });
  }
}

module.exports = CustomPlugin;
