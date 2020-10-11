<template>
    <div class="pain-evaluations">
        <h1>Évaluations de la douleur</h1>
        <div v-for="(key, type) of this.types" v-bind:key="key">
            <PainEvaluation :type="type" :date="date" :name="key" />
        </div>
    </div>
</template>

<script>
    //import axios from "axios";
    import PainEvaluation from "./PainEvaluation";

    export default {
        name: 'PainEvaluations',
        components: {
            PainEvaluation
        },
        props: {
            date: String
        },
        data: function () {
            return {
                types: {'morning' : 'Matin', 'midday': 'Midi', 'evening': 'Soir', 'night': 'Nuit'}
            }
        },
        methods: {
        }
    }
</script>
