import React from 'react';
import { TextField } from '../inputs/TextField';
import { SimpleOptionsInput } from '../inputs/SimpleOptionsInput';
//import { DatePicker } from '../inputs/DatePicker';

const RegistrationForm = () => {
  return (
    <div className = "absolute top-2/4 left-2/4 transform -translate-x-1/2 -translate-y-1/2 bg-slate-800 p-10 opacity-50">
        <TextField type = "text" placeholder = "first name"/>
        <TextField type = "text" placeholder = "last name"/>
        <SimpleOptionsInput placeholder = "gender" selectItems = {["male", "female"]}/>
        {/* <DatePicker /> */}
        
    </div>
  )
}

export default RegistrationForm;