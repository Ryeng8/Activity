<template>
  <v-app>
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
    <v-main>
      <v-card>

        <!--แถบสีม่วง1-->
        <v-sheet color="purple darken-2" height="40">
        </v-sheet>

        <!--แถบสีม่วง2 และ icon กิจกรรม-->
        <v-sheet align="center" color="purple darken-3 white--text" height="120">
          <v-avatar class="overview-box-icon"
                    color="purple darken-3"
                    size="90">
            <v-icon color="white" size="60">
              mdi-calendar-search
            </v-icon>
          </v-avatar>
          <h2 class="mt-2">ระบบกิจกรรม</h2>
        </v-sheet>

        <!--row menu & content-->
        <v-row>
              <v-col class="col-3 mt-5" md="2" lg="2" xl="3">

                <v-card tile elevation="0">
                  <v-list>
                    <v-list-item-group color="primary">

                      <v-list-item :to="{path:'/activity'}" exact>
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
              </v-col>




            <v-col class="mt-10">

              <nuxt/>

            </v-col>


        </v-row>
      </v-card>

    </v-main>

    <v-footer
      :absolute="!fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire'
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Software Engineering'
    }
  }
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
