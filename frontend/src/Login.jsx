import {useState} from "react";
import api from "../api";

function Login(){

 const [username,setUsername]=useState("");
 const [password,setPassword]=useState("");

 const getLocation=()=>{
  return new Promise((res,rej)=>{
   navigator.geolocation.getCurrentPosition(
    pos=>res(pos.coords),
    err=>rej(err)
   );
  });
 };

 const submit=async(e)=>{
  e.preventDefault();

  const loc = await getLocation();

  try{
   const res = await api.post("login/",{
    username,
    password,
    lat:loc.latitude,
    lon:loc.longitude
   });

   alert(`Welcome ${res.data.role}`);
  }catch{
   alert("Login blocked (outside office or invalid)");
  }
 };

 return(
  <form onSubmit={submit}>
   <input placeholder="Username" onChange={e=>setUsername(e.target.value)}/>
   <input type="password" placeholder="Password" onChange={e=>setPassword(e.target.value)}/>
   <button>Login</button>
  </form>
 );
}

export default Login;
    