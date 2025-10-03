<template>
  <div class="main">
    <div class="token-input">
      <h2>Enter GitHub Token</h2>
      <div>
        <input
          class="input-box"
          v-model="token"
          placeholder="Paste Your Token"
        />
        <button class="save-button" @click="saveToken">Save</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const token = ref("");

const saveToken = async () => {
  try {
    const res = await fetch("/api/save-token", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ token: token.value }),
    });

    const data = await res.json();
      alert(data.message);
    } catch (err) {
      console.error(err);
    alert("Failed to save token");
  }
};
</script>
