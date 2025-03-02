import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',  // Make sure this matches your Flask server
        changeOrigin: true,
        secure: false
      }
    }
  }
})