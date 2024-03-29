import React from 'react';
import { TextField } from '../inputs/TextField';

const AssessmentForm = () => {
  return (
    <div>
        
        AssessmentForm
        <form action="#" className = "w-3/5 absolute top-2/4 left-2/4 transform -translate-x-1/2 -translate-y-1/2 bg-slate-800 p-10 opacity-50">
        <TextField type = "textarea" placeholder = "1. Was the job description presented to you during the recruitment process accurate?"/>
        <TextField type = "textarea" placeholder = "2. Did you get a clear overview of your onboarding process from the first day on the job?"/>
        </form>
    </div>
  )
}

export default AssessmentForm