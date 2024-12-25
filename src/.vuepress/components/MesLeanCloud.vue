<template>
    <div>
      <!-- Top TOC Section -->
      <div class="toc" :class="{ collapsed: tocCollapsed }">
        <button @click="toggleToc" class="toggle-toc">
          {{ tocCollapsed ? '展开目录' : '收起目录' }}
        </button>
        <ul v-if="!tocCollapsed">
          <li v-for="(category, index) in organizedMessages" :key="index">
            <a @click="scrollToSection(index)">{{ category.to }}</a>
          </li>
        </ul>
      </div>
  
      <!-- Messages Section -->
      <div v-for="(category, index) in organizedMessages" :key="index" :id="'section-' + index" class="message-category">
        <h2>{{ category.to }}</h2>
        <div v-for="(member, idx) in category.members" :key="idx" class="message-member">
          <h3>{{ member.name }}</h3>
          <p>{{ member.note }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import AV from "leancloud-storage";
  
  export default {
    data() {
      return {
        messages: [], // Stores raw data from LeanCloud
        organizedMessages: [], // Stores the organized data
        tocCollapsed: false, // Controls whether the TOC is collapsed
      };
    },
    created() {
      this.initLeanCloud();
      this.loadMessages();
    },
    methods: {
      // Initialize LeanCloud SDK
      initLeanCloud() {
        AV.init({
          appId: "G8RpvOvXUXBg6gDeSX4QMCh7-MdYXbMMI", // Replace with your App ID
          appKey: "KIeFjTPSuv7zGnsrPtoSGgHK", // Replace with your App Key
          serverURL: "https://g8rpvovx.api.lncldglobal.com", // Replace with your Server URL
        });
      },
      // Fetch and organize messages
      async loadMessages() {
        try {
          const query = new AV.Query("Messages");
          const results = await query.find();
          this.messages = results.map((item) => ({
            name: item.get("name"),
            note: item.get("note"),
            to: item.get("to"),
          }));
          this.organizeMessages();
        } catch (error) {
          console.error("Failed to load messages:", error);
        }
      },
      // Organize messages into the desired structure
      organizeMessages() {
        const grouped = {};
        this.messages.forEach((message) => {
          if (!grouped[message.to]) {
            grouped[message.to] = [];
          }
          grouped[message.to].push({ name: message.name, note: message.note });
        });
        this.organizedMessages = Object.keys(grouped).map((key) => ({
          to: key,
          members: grouped[key],
        }));
      },
      // Toggle the TOC's collapsed state
      toggleToc() {
        this.tocCollapsed = !this.tocCollapsed;
      },
      // Scroll to the corresponding section when TOC link is clicked
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
  /* Styling for the TOC */
  .toc {
    background: #f5f5f5;
    padding: 10px;
    /* border-bottom: 1px solid #ddd; */
    border-radius: 10px;
    position: sticky;
    top: 0;
    z-index: 1000;
  }
  
  .toc.collapsed ul {
    display: none;
  }
  
  .toggle-toc {
    background: #007bff;
    color: #fff;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    font-size: 14px;
    margin-bottom: 10px;
  }
  
  .toggle-toc:hover {
    background: #0056b3;
  }
  
  /* Styling for individual message categories */
  .message-category {
    margin: 20px 0;
    padding: 10px;
    /* border: 1px solid #ddd; */
    border-radius: 5px;
    background: #fff;
  }
  
  .message-category h2 {
    margin: 0 0 10px;
    font-size: 20px;
    color: #333;
  }
  
  /* Styling for individual message members */
  .message-member {
    margin: 10px 0;
    padding: 10px;
    /* border: 1px solid #eee; */
    border-radius: 5px;
    /* background: #fafafa; */
  }
  
  .message-member h3 {
    margin: 0;
    font-size: 18px;
    color: #555;
  }
  
  .message-member p {
    margin: 5px 0 0;
    font-size: 16px;
    color: #666;
  }
  </style>
  