import { defineClientConfig } from 'vuepress/client'
import Messages from './components/Messages.vue'
import MesTOC from './components/MesTOC.vue'

export default defineClientConfig({
  enhance({ app }) {
    app.component('MesTOC', MesTOC);
  },
})