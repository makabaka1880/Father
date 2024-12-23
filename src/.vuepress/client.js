import { defineClientConfig } from 'vuepress/client'
import Messages from './components/Messages.vue'

export default defineClientConfig({
  enhance({ app }) {
    app.component('Messages', Messages)
  },
})