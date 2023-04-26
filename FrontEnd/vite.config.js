import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    cors: true, // 默认启用并允许任何源
    open: false,// 默认打开浏览器
    port: 5173,// 访问的端口号
    host: "127.0.0.1",// 访问的地址
    proxy: {
      '/api': {	//
        target: "http://127.0.0.1:5000", // 目标地址
        ws: true,
        secure: false,
        changeOrigin: true,// 是否允许跨域代理
        rewrite: (path) => path.replace(/^\/api/, "")// 重定向地址
      }
    },
  }
},
)
