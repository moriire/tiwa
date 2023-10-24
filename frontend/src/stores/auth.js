//const BASE = import.meta.env.VITE_API_URL; //
const BASE = "http://127.0.0.1:8000";
console.log(BASE);
//import alertifyjs from "@/alertifyjs";
import router from "@/router";
import axios from "axios";
import { defineStore } from "pinia"
export const useAuthStore = defineStore({
	id: "auth",
	state: ()=> ({
        isAuthenticated: false,
        user: null,
		loginForm: { email: "", password: "" },
		regForm: {email: "",  password1: "", password2: "" },
		stores : {
			data : JSON.parse(localStorage.getItem("user")),
			loggedIn: localStorage.getItem("loggedin"),
			detail: {}
		}

	}),
	actions: {
		async logout() {
			try {
			const res = await axios.post(`${BASE}/auth/logout/`, {headers: {'Content-Type': 'application/json', Authorization: `Bearer ${this.stores.access_token}`}})//config)
				const resp = res.data 
				window.localStorage.clear()
				alertifyjs.success("loggedout");   
				router.push("/account/login");
			} catch(errors) {
				console.log(errors);
				window.localStorage.clear();
				//location.href="/account/login"
				router.push("/account/login")
				//alertifyjs.errors("loggedout");   
			}
	},
	async login(email, password) {
		try {

			const res = await axios.post(`${BASE}/auth/login/`, {email, password});
			console.log(res.data
				)
			localStorage.setItem("user", JSON.stringify(res.data));
			console.log(localStorage.getItem("user"))
            this.isAuthenticated = true;
            this.user = JSON.parse(localStorage.getItem("user"))
            alert("success")
            router.push("home")
			
		} catch(errors) {
			console.log(errors)
		
				}
	},
	
	getUserProfile(){
		axios.get(`${BASE}/auth/user/`, { headers: {
		  "Authorization": `Bearer ${this.stores.access_token}`,
		  //"Content-Type": "application/json"
		}})
		.then(res => {
		  //console.log(res)
		  this.regForm = res.data
		})
		.catch(errors => {
		  if (errors.response.data.code === "token_not_valid"){
			this.logout()
		  }
		  alert(errors)
		})
	  },
	  
	async refreshToken(refresh_token = this.refresh_token) {
		try {
			const res = await axios.post(`${BASE}/auth/token/refresh/`, 
				{ refresh: refresh_token }, {header: 
					{"Authorization": `Bearer ${this.access_token}`}
				});
			const resp = res.data;
			localStorage.setItem("access_token", resp.access_token),
			localStorage.setItem("access_token_time", resp.access_token_expiration),
			
			alert("refreshed")
		} catch(errors) {
			logout();
			localStorage.clear();
			location.href=getQ(location.href)
			//alert(errors.response.data)
		}
	},
	async verifyToken(token) {
		try {
		const res = await axios.post(`${BASE}/auth/token/verify/`, { "token" : token})
		return true
		} catch(errors) {
		//localStorage.removeItem("loggedin"),
		console.log(errors.response.data)
		//location.href="/account/login"
		}
	},
	async resetPassword(email) {
		try {
			const res = await axios.post(`${BASE}/auth/password/reset/`, { email });
			const resp = res.data
			alertifyjs.alert("Password reset successful")
			router.push("/account/confirm_password")
		} catch(errors) {
				alertifyjs.alert(errors);
				$errors.code = errors.response.status;
				$errors.message= "Username or password error"
		}
	},
	async changePassword(new_password1, new_password2) {
		const config = { headers: {Authorization: `Bearer  ${ state.data.access_token }` }}
		try {
			const res = await axios.post(`${BASE}/auth/password/change/`, {new_password2, new_password1}, config);
			//location.href=location.href.split("?redirect=")[1] || '/receive'
			return res
		} catch(errors) {
		return errors.response.data
				}
	},

	async register(kw){
		try {
			const res = await axios.post(`${BASE}/auth/register/`, kw )
			//console.log(res.data)
			return res.data;
		} catch(errors){
			console.log(errors)
			//return errors.response
		}
	},

	},
	getters:{
		auth: (state)=>{
			return this.data
		}
	}
})