export default {
    namespaced: true,
    state(){
        return {
            coaches: [
                
                    {
                      id: 'c1',
                      firstName: 'Maximilian',
                      lastName: 'Schwarzmüller',
                      areas: ['frontend', 'backend', 'career'],
                      description:
                        "I'm Maximilian and I've worked as a freelance web developer for years. Let me help you become a developer as well!",
                      hourlyRate: 30
                    },
                    {
                      id: 'c2',
                      firstName: 'Julie',
                      lastName: 'Jones',
                      areas: ['frontend', 'career'],
                      description:
                        'I am Julie and as a senior developer in a big tech company, I can help you get your first job or progress in your current role.',
                      hourlyRate: 30
                    }
                  ]
            
        };
    },
    getters: {
        coaches(state){
            return state.coaches; 
        },
        hasCoaches(state) {
            return state.coaches && state.coaches.length > 0;
        },
        isCoach(_, getters, _2, rootGetters){
          const coaches = getters.coaches;
          const userId = rootGetters.userId;
          return coaches.some(coach => coach.id === userId);
        }
    },

    mutations: {
    registerCoach(state, payload) {
        state.coaches.push(payload);
      }

    },
    actions: {
      async registerCoach(context, data){
        const userId = context.rootGetters.userId;
        const coachData = { 
          /* id: context.rootGetters.userId, */
          firstName: data.first,
          lastName: data.last,
          description: data.desc,
          hourlyRate: data.rate,
          areas: data.areas
        };

        const response = await fetch(`https://coach-app-http-default-rtdb.firebaseio.com/coaches/${userId}.json`, {
            method: 'PUT',
            body: JSON.stringify(coachData)
        });

        // const respondeData = await response.json()

        if (!response.ok){
          // error
        }

        context.commit('registerCoach', {
          ...coachData,
          id: userId
        });
      }
    },
    
}