import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";

// Create a singleton instance
const dracoLoader = new DRACOLoader();
dracoLoader.setDecoderPath("draco/");
dracoLoader.setDecoderConfig({ type: "ts" });

// Export the singleton instance
export default dracoLoader;
