<template>
  <div class="container">

    <v-simple-table>
      <template v-slot:default>
        <thead>
        <tr>
          <th class="text-left">
            <h1>ชื่อกิจกรรม</h1>
          </th>
          <th class="text-left">
            <h1>คำอธิบาย</h1>
          </th>
        </tr>
        </thead>
        <tbody>
        <tr
          v-for="data in datas"
          :key="data.id"
        >
          <td><nuxt-link :to="{ path: `/photos/${data.id}` }">{{ data.title }}</nuxt-link></td>
          <td>{{ data.description }}</td>

        </tr>

        </tbody>
      </template>
    </v-simple-table>


  </div>
</template>
<script>
export default {

  async asyncData({$axios}) {
    const datas = await $axios.$get('http://localhost:8000/api/v1/activity/activitys/');
    return {datas};
  }
};
</script>
<style scoped>
.container {
  padding: 1em;
  width: 1220px;
  margin: 0 auto;
}

.photos {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: auto;
  grid-gap: 1em;
  text-align: center;
}

.photo-item {
  width: 100%;
  height: 256px;
  object-fit: cover;
}
</style>
