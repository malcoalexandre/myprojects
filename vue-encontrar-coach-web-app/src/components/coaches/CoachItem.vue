<template>
    <li>
        <h3>{{ fullName }}</h3>
        <h4>${{ rate }}/hour</h4>
        <div>
            <base-badge v-for="area in areas" :key="area" :type="area" :title="area"></base-badge>
        </div>
        <div class="actions">
            <base-button mode="outline" link :to="coachContactLink">Contact</base-button> <!-- this is a router-link -->
            <base-button link :to="coachDetailsLink">View Details</base-button> <!-- this is a router-link -->
        </div>
    </li>
</template>

<script>
export default {
    props: ['id', 'firstName', 'lastName', 'rate', 'areas'],
    computed: {
        fullName(){
            return this.firstName + ' ' + this.lastName;
        },
        coachContactLink(){
            return '/coaches/' + this.id + '/contact' // /coaches/c1/contact // replace '/coaches/' to this.$route.path
        },
        coachDetailsLink(){
            return '/coaches/' + this.id;
        }
    }
}
</script>


<style scoped>
li {
  margin: 1rem 0;
  border: 1px solid #424242;
  border-radius: 12px;
  padding: 1rem;
}

h3 {
  font-size: 1.5rem;
}

h3,
h4 {
  margin: 0.5rem 0;
}

div {
  margin: 0.5rem 0;
}

.actions {
  display: flex;
  justify-content: flex-end;
}
</style>