import React, { useState, useEffect } from 'react';
import {useParams } from 'react-router-dom';
import AssessmentForm from '@/components/forms/AssessmentForm';

const AssessmentPage = () => {

    const {video_id} = useParams();
    const [assessment, setAssessment] = useState([]);

    useEffect(() => {
      getVideos();
  
    }, []);
  
    let getVideos = async () => {
  
      let response = await fetch(`http://127.0.0.1:8000/api/get_assessment/${video_id}/`);
      let data = await response.json();
      console.log("DATA:", data);
      setAssessment(data);
    }


    return (
        <div>
            
            <h1>Assessment of video {video_id}</h1>

            <h1>Assessment title: {assessment.title}</h1>
            <AssessmentForm />
            
            </div>
    )
    }

export default AssessmentPage