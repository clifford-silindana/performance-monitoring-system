import React from 'react';
import { useState, useEffect } from 'react';
import { VideosCarousel } from '@/components/carousel/VideosCarousel';

const Videos = () => {

    const [videos, setVideos] = useState([]);

    useEffect(() => {
      getVideos();
  
    }, []);
  
    let getVideos = async () => {
  
      let response = await fetch("http://127.0.0.1:8000/api/departmental_videos/Human%20Resources/");
      let data = await response.json();
      console.log("DATA:", data);
      setVideos(data);
    }

    return (
        <div className = "w-full">
            <h1>Videos</h1>
            <VideosCarousel videos = {videos} />


        </div>
    )
}

export default Videos