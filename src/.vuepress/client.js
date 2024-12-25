import { defineClientConfig } from 'vuepress/client'
import MesTOC from './components/MesTOC.vue'
import Life from './components/Life.vue'
// import Scene3D from './components/Scene3D.vue'

export default defineClientConfig({
  enhance({ app }) {
    app.component('MesTOC', MesTOC);
    app.component('Life', Life);
    // app.component('Scene3D'), Scene3D
  },
})