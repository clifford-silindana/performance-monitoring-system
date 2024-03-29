import React from 'react';
import registrationbg from "../assets/images/registrationbg.jpg";
import RegistrationForm from '@/components/forms/RegistrationForm';

const Registration = () => {
  return (
    <div className = "w-full h-full">
        <img id = "registration-bg-image" className = "w-full h-full object-cover" src= {registrationbg} alt= "an open-area office space" />
        <RegistrationForm />
    </div>
  )
}

export default Registration;