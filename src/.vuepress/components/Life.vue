<template>
    <div class="timeline">
      <div
        v-for="(event, index) in events"
        :key="index"
        class="timeline-entry"
      >
        <div class="timeline-content">
          <h3>{{ event.title }}</h3>
          <p class="timeline-time">{{ formatDate(event.time) }}</p>
          <p>{{ event.description }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
    import dayjs from "dayjs"; // Import the dayjs library
    import "dayjs/locale/zh-cn"; // Import Chinese locale
    dayjs.locale("zh-cn"); // Set day.js to use Chinese locale

    export default {
    data() {
        return {
        events: [], // Stores the dynamically loaded JSON data
        };
    },
    mounted() {
        this.loadTimelineData();
    },
    methods: {
        async loadTimelineData() {
        try {
            const response = await fetch("/static/life.json");
            this.events = await response.json();
        } catch (error) {
            console.error("Failed to load timeline data:", error);
        }
        },
        formatDate(date) {
        // Format the date using dayjs with Chinese locale
        return dayjs(date).format("YYYY年M月D日"); // Example: "1990年1月1日"
        },
    },
    };
  </script>
  
  <style scoped>
  .timeline {
    display: flex;
    flex-direction: column;
    position: relative;
    padding: 20px;
  }
  
  .timeline-entry {
    position: relative;
    width: 60%; /* Center alignment */
    margin: 20px auto;
    padding: 15px 20px;
    background-color: #f4f4f4;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .timeline-content h3 {
    margin: 0;
    font-size: 1.2rem;
    font-weight: bold;
  }
  
  .timeline-time {
    font-size: 0.9rem;
    color: gray;
    margin-bottom: 10px;
  }
  
  .timeline-entry::after {
    /* content: "";
    position: absolute;
    top: 15px;
    left: -25px;
    width: 10px;
    height: 10px;
    background-color: #555;
    border-radius: 50%; */
    
  }
  
  .timeline:before {
    content: "";
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background-color: #555;
    transform: translateX(-50%);
  }
  </style>
  