<template>
    <section>
        <coach-filter @change-filter="setFilters"></coach-filter>
    </section>
    <section>
        <base-card>
        <div class="controls">
            <base-button mode="outline">Refresh</base-button>
            <base-button v-if="!isCoach" link to="/register">Register as Coach</base-button> <!-- this is a router link, other alternative could be to make a button-router-link instead of only one base-button -->
        </div>
        <ul v-if="hasCoaches">
            <coach-item 
            v-for="coach in filteredCoaches" 
            :key="coach.id"
            :id="coach.id"
            :first-name="coach.firstName"
            :last-name="coach.lastName"
            :rate="coach.hourlyRate"
            :areas="coach.areas"
            ></coach-item>
        </ul>
        <h3 v-else>No Coaches Found</h3>
        </base-card>
    </section>
</template>

<script>
import CoachItem from '../../components/coaches/CoachItem.vue';
import CoachFilter from '../../components/coaches/CoachFilter.vue';

export default {
    components: {
        CoachItem,
        CoachFilter
    },
    data(){
        return {
            activeFilters: {
                frontend: true,
                backend: true,
                career: true
            }
        }
    },
    computed: {
        isCoach() {
            return this.$store.getters['coaches/isCoach'];
        },
        filteredCoaches(){
            const coaches = this.$store.getters['coaches/coaches']; // the first coaches is the namespaced name and the second coaches is the getter name
            return coaches.filter(coach => {
                if (this.activeFilters.frontend && coach.areas.includes('frontend')) {
                    return true;
                }
                if (this.activeFilters.backend && coach.areas.includes('backend')) {
                    return true;
                }
                if (this.activeFilters.career && coach.areas.includes('career')) {
                    return true;
                }
                return false;
            })
        },
        hasCoaches(){
            return this.$store.getters['coaches/hasCoaches'];
        }

    },
    methods: {
        setFilters(updatedFilters) {
            this.activeFilters = updatedFilters;
        }
    }
}
</script>

<style scoped>
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.controls {
  display: flex;
  justify-content: space-between;
}
</style>