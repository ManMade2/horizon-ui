import { defineConfig } from 'vite';
import { nodePolyfills } from 'vite-plugin-node-polyfills';

export default defineConfig({
    build: {
        outDir: '../backend/horizon_ui/static/dis',  // Output files to the Python static folder
        emptyOutDir: true,        // Clean the output directory before building
        rollupOptions: {
            input: './src/main.ts',  // Set the entry point manually
            output: {
                entryFileNames: '[name].js',
                chunkFileNames: '[name].js',
                assetFileNames: '[name].[ext]',
            },
        },
        watch: {
            include: 'src/**',      // Watch for changes in the 'src' folder
            clearScreen: false,     // Prevent clearing the terminal on each rebuild
        },
    },

    plugins: [
        nodePolyfills(), // Automatically polyfills core Node.js modfules in browser
    ],
    resolve: {
        alias: {
            'stream': 'stream-browserify', // Polyfill stream for browser use
        },
    },
});