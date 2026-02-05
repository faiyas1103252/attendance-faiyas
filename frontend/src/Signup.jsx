import {useState} from "react";
import api from "../api";

function Signup(){

 const [username,setUsername]=useState("");
 const [password,setPassword]=useState("");
 const [role,setRole]=useState("employee");

 const submit=async(e)=>{
  e.preventDefault();
  await api.post("signup/",{username,password,role});
  alert("User created");
 }

 return(
  <form onSubmit={submit}>
   <input placeholder="Username" onChange={e=>setUsername(e.target.value)}/>
   <input type="password" placeholder="Password" onChange={e=>setPassword(e.target.value)}/>

   <select onChange={e=>setRole(e.target.value)}>
     <option value="employee">Employee</option>
     <option value="admin">Admin</option>
     <option value="superadmin">Super Admin</option>
   </select>

   <button>Signup</button>
  </form>
 );
}

export default Signup;
