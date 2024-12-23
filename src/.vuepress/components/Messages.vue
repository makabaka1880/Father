<template>
  <div>
    <!-- 分段展示 -->
    <div v-for="(section, sectionIndex) in messages" :key="sectionIndex">
      <!-- 展示 "to" -->
      <h2>{{ section.to }}</h2>
      
      <!-- 每个成员信息 -->
      <div v-for="(member, memberIndex) in section.members" :key="memberIndex" style="margin-left: 20px;">
        <h3>{{ member.name }}</h3>
        <p>{{ member.note }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [], // 存储从 JSON 文件加载的数据
    };
  },
  created() {
    this.loadMessages();
  },
  methods: {
    async loadMessages() {
      try {
        const response = await fetch('/static/messages.json'); // 根据文件路径加载 JSON
        this.messages = await response.json();
      } catch (error) {
        console.error("加载寄语失败:", error);
      }
    },
  },
};
</script>

<style scoped>
h2 {
  color: #333;
  font-size: 1.75rem;
  margin-bottom: 16px;
}
h3 {
  color: #555;
  font-size: 1.5rem;
  margin-bottom: 8px;
}
p {
  color: #777;
  margin-bottom: 16px;
}
</style>
