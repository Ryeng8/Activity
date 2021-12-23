<template>
  <div class="photo-info">
    <h1>Detail</h1>
    <p>id : {{ data.id }}</p>
    <p>title : {{ data.title }}</p>
    <p>type : {{ data.activity_type.title }}</p>


    <nuxt-link to="/photos" class="link">Back</nuxt-link>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios, params }) {
    const data = await $axios.$get(
      `http://localhost:8000/api/v1/activity/activitys/${params.id}/`
    );
    return { data };
  }
};
</script>
<style scoped>
.photo-info {
  width: 860px;
  margin: 0 auto;
  text-align: center;
}
.img {
  width: 100%;
}
.link {
  display: inline-block;
  margin-top: 2em;
}
</style>
