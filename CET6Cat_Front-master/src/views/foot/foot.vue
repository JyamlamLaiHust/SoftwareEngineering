<template>
  <footer>
    <p>{{ copyright }}</p>
  </footer>
</template>

<script>
export default {
  name: "foot",
  data() {
    return {
      copyright: "Copyright©2023 at HUST"
    }
  }
}
</script>

<style scoped>
footer {
  /* background: rgb(84, 92, 100); */
  background-color: black;
  height: 39px;
  padding-top: 25px;
}

p {
  color: white;
  text-align: center;
}
</style>
