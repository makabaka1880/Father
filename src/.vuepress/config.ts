import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "李璟",
  description: "李璟的数字墓碑",

  theme,

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
