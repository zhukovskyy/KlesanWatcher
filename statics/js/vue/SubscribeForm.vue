<template>
    <div id="subscribe_form">
        <h1>預定天氣預報簡訊:</h1>
        <input type="date" name="date" v-bind:value="date" v-bind:min="setToday()">
        <input type="tel" name="tel" v-bind:value="phone">
        <select v-model="geocode">
          <optgroup v-for="r in regions" v-bind:label="r.region">
            <option v-for="t in r.regions" v-bind:value="t.geocode">
              {{ t.town }}
            </option>
          </optgroup>
      </select>
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
    regions() {
      return this.$store.state.regions
    }
  }
}
</script>
<style>
  h1 {
    color: black;
  }
</style>
