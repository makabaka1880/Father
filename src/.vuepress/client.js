import { defineClientConfig } from 'vuepress/client'
import MesTOC from './components/MesTOC.vue'

export default defineClientConfig({
  enhance({ app }) {
    app.component('MesTOC', MesTOC);
  },
})