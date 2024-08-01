import HomeView from '@/views/HomeView.vue';
import SettingView from '@/views/SettingView.vue';
import Vue from 'vue';
import App from '@/App.vue';


const read_component = HomeView;
const create_component = SettingView;

//형제 컴포넌트 간 값 전달 방법 1 
export const eventBus = new Vue(
    {
        el: '#app',
        component: {
            'read-component' : read_component,
            'create-component' : create_component,
        },
        data() {
            return {
                isShow: 'read',
            }
        }, 
        methods : {
            settingWasEdited(settings){
                this.$emit('settingWasEdited', settings)
            }
        }
    }
);

/*
new Vue({
    el: '#app',
    component: {
        'read-component' : read_component,
        'create-component' : create_component,
    },
    data() {
        return {
            isShow: 'read',
        }
    }
})*/

