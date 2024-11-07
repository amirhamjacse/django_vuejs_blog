<template>
    <div>
        <h1>Details</h1>
        <p>Description {{ id }}</p>
        <p>
            {{ datas }}
        </p>
        {{datas.title}}
        <br>
        {{datas.blog_description}}

            
    </div>
</template>

<script>
import axios from 'axios';
const apiUrl = import.meta.env.VITE_API_URL;
export default{
    props: ['id'],
    data(){
        return{
            description: '',
            datas: "",
            // id: this.id
        }
    },
    mounted(){
        this.detailsBlog();
    },
    methods:{
        async detailsBlog(){
        // console.log(this.id, 'working')
        const response = await axios.get(`${apiUrl}blog/details/${this.id}/`);
        this.datas = response.data;
        // console.log(response);

        }
    }
}
</script>