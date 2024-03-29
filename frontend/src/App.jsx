import {BrowserRouter, Routes, Route} from "react-router-dom";
import { Button } from "@/components/ui/button";
import Registration from './pages/Registration';
import Videos from "./pages/Videos";
import AssessmentPage from "./pages/AssessmentPage";

function App() {
  return (
    <BrowserRouter>
   
          <Routes>
              <Route path = "register/" element = {<Registration />} />
              <Route path = "hr/videos/" element = {<Videos />} />
              <Route path = "hr/assessments/:video_id/" element = {<AssessmentPage />} />
          </Routes>

    </BrowserRouter>
  )
}

export default App;
