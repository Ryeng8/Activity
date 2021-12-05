<template>

  <div class="text-center">

    <v-sheet color="purple darken-2" height="40">
    </v-sheet>

    <v-sheet color="purple darken-3 white--text" height="120">
      <v-avatar class="overview-box-icon"
                color="purple darken-3"
                size="90">
        <v-icon color="white" size="60">
          mdi-calendar-search
        </v-icon>

      </v-avatar>

      <h2 class="mt-2">ระบบกิจกรรม</h2>
    </v-sheet>

  </div>
</template>

<script>
export default {
  name: "SeActivityHead"
}
</script>

<style scoped>
.overview-box-icon {
  border-radius: 50%;
  width: 40px;
  height: 40px;
  line-height: 40px;
  margin: 0 auto;
  margin-top: -35px;
}
</style>
