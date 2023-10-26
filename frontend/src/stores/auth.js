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
        isAuthenticated: JSON.parse(localStorage.getItem("loggedin"))? true: false,
        user: JSON.parse(localStorage.getItem("user")),
		loginForm: { email: "", password: "" },
		regForm: {email: "",  password1: "", password2: "" },
		detail: {email:"", first_name: "", last_name: ""}

	}),
	actions: {
		async logout() {
			try {
			const res = await axios.post(`${BASE}/auth/logout/`, {headers: {'Content-Type': 'application/json', Authorization: `Bearer ${this.user.access}`}})//config)
				const resp = res.data 
				localStorage.clear()
                this.user = null;
                this.isAuthenticated = false;
				router.push("/login");
			} catch(errors) {
				console.log(errors);
				window.localStorage.clear();
				this.user = null;
				router.push("/account/login")
				//alertifyjs.errors("loggedout");   
			}
	},
	async login(email, password) {
		try {
			const res = await axios.post(`${BASE}/auth/login/`, {email, password});
			localStorage.setItem("user", JSON.stringify(res.data));
			localStorage.setItem("loggedin", JSON.stringify(true));
			this.getUserProfile();
            alert("success")
            router.push({name: 'profile'})
			
		} catch(errors) {
			console.log(errors)
		
				}
	},
	
	async getUserProfile(){
		//console.log(this.user.access)
		const headers = {
			"Authorization": `Bearer ${this.user.access}`,
			"Content-Type": "application/json"
		}
		try{
			const res = await axios.get(`${BASE}/auth/user/`, { headers })
			this.detail = res.data
			console.log(res)
		} catch(error){
			console.log(error)
		}
	  },
	
	  async updateProfile(kw){
		//console.log(this.user.access)
		const headers = {
			"Authorization": `Bearer ${this.user.access}`
			//"Content-Type": "application/json"
		}
		try{
			const res = await axios.put(`${BASE}/auth/user/`, {...kw}, { headers })
			this.detail = res.data
			console.log(res)
		} catch(error){
			console.log(error)
		}
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
})