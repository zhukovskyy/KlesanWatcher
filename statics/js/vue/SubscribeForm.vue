<template>
    <div id="subscribe_form">
        <h1>預定天氣預報簡訊:</h1>
        <input type="date" name="date" v-bind:value="date" v-bind:min="setToday()">
        <input type="tel" name="tel" v-bind:value="phone">
        <p>{{ value }}</p>
    </div>
</template>
<script>
function _setToday(){
    var date = new Date();
    var day = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();
    if (month < 10) month = "0" + month;
    if (day < 10) day = "0" + day;
    return year + "-" + month + "-" + day;
}
module.exports = {
  name: 'SubscribeForm',
  data(){
    return {
      date: _setToday(),
      phone: '+886987654321'
    }
  },
  methods: {
    setToday: _setToday
  },
  computed: {
    value() {
      return this.$store.state.ajax_data
    }
  }
}
</script>
<style>
  h1 {
    color: black;
  }
</style>
