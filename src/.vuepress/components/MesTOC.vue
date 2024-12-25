<template>
  <div>
    <!-- 顶部目录 -->
      <nav class="toc-top">
        <div style="padding-left: 10px; padding-bottom: 10px;">
        <button
          @click="toggleToc"
          style="background: #0066cc; color: #fff; border: none; padding: 10px; cursor: pointer; border-radius: 4px; margin-right: 16px;"
        >
          {{ tocCollapsed ? '展开' : '收起' }}
        </button>
      </div>
        <ul v-show="!tocCollapsed" style="display: inline; margin: 0; padding: 0; list-style: none;">
          <li
            v-for="(section, index) in messages"
            :key="index"
            style="margin-right: 16px; padding: 8px;"
          >
            <a
              :href="'#section-' + index"
              @click.prevent="scrollToSection(index)"
              style="text-decoration: none; color: #0066cc;"
            >
              {{ section.to }}
            </a>
          </li>
        </ul>
      </nav>
    <!-- 内容部分 -->
    <div class="content">
      <div
        v-for="(section, sectionIndex) in messages"
        :key="sectionIndex"
        :id="'section-' + sectionIndex"
        style="margin-bottom: 32px;"
      >
        <h2>{{ section.to }}</h2>
        <div v-for="(member, memberIndex) in section.members" :key="memberIndex" style="margin-left: 20px;">
          <h3>{{ member.name }}</h3>
          <p>{{ member.note }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [], // 存储从 JSON 文件加载的数据
      tocCollapsed: false, // 控制目录是否收起
    };
  },
  created() {
    this.loadMessages();
  },
  methods: {
    async loadMessages() {
      try {
        const response = await fetch('/static/messages.json'); // 加载 JSON
        this.messages = await response.json();
      } catch (error) {
        console.error("加载寄语失败:", error);
      }
    },
    toggleToc() {
      this.tocCollapsed = !this.tocCollapsed; // 切换目录的展开/收起状态
    },
    scrollToSection(index) {
      const section = document.getElementById(`section-${index}`);
      if (section) {
        section.scrollIntoView({ behavior: "smooth" });
      }
    },
  },
};
</script>

<style scoped>
/* 顶部固定目录 */
.toc-top {
  position: sticky;
  top: 0;
  left: 0;
  width: 100%;
  padding-top: 10px;
  background: #f9f9f9;
  border-radius: 10px;
  z-index: 1000;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  padding: 10px;
}

h2 {
  margin-bottom: 16px;
  font-size: 1.75rem;
  font-weight: bold;
}

h3 {
  margin-bottom: 8px;
  font-size: 1.25rem;
  font-weight: bold;
}

p {
  margin: 0;
  color: gray;
  font-size: 1rem;
}
</style>
