<template>
  <v-card tile elevation="0">
    <v-list>
      <v-list-item-group color="primary">

        <v-list-item :to="{path:'/activity/active'}" exact>
          <v-list-item-icon>
            <v-icon>mdi-bell-ring
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>กิจกรรมล่าสุด</v-list-item-title>
          </v-list-item-content>
        </v-list-item>


        <v-list-item :to="{path:'/activity/conclude'}">
          <v-list-item-icon>
            <v-icon>mdi-view-dashboard
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>สรุปกิจกรรมทั้งหมด</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item :to="{path:'/activity/my'}">
          <v-list-item-icon>
            <v-icon>mdi-calendar-edit
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>กิจกรรมของฉัน</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <!--        <v-list-item :to="{path:'/activity/my/create'}">-->
        <!--          <v-list-item-icon>-->
        <!--            <v-icon>mdi-calendar-edit-->
        <!--            </v-icon>-->
        <!--          </v-list-item-icon>-->
        <!--          <v-list-item-content>-->
        <!--            <v-list-item-title>สร้างกิจกรรม</v-list-item-title>-->
        <!--          </v-list-item-content>-->
        <!--        </v-list-item>-->


      </v-list-item-group>
    </v-list>
  </v-card>

</template>

<script>
export default {
  name: "SeActivityMenu",
}
</script>
