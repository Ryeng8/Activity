<template>
  <v-app-bar dark clipped-left fixed app color="purple darken-4">
    <v-avatar class="mr-2">
      <v-img contain max-height="48" src="/senew.svg"></v-img>
    </v-avatar>
    <v-toolbar-title v-text="title"/>
    <v-spacer/>
    <v-btn text :to="{path:'/'}">หน้าหลัก</v-btn>
    <v-btn text :to="{path:'/activity/active'}">กิจกรรมสาขา</v-btn>
    <v-btn text>เกี่ยวกับสาขาวิชา</v-btn>
    <v-btn text>หลักสูตร</v-btn>
    <v-btn text>ติดต่อ</v-btn>
    <v-btn icon @click.stop="menuClick">
      <v-icon>mdi-menu</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: "SeAppBar",
}
</script>

<!--<style scoped>-->

<!--</style>-->
