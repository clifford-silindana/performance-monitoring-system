import { useState } from 'react';
import { Button } from "@/components/ui/button"


function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <h1 className = "text-stone-400 bg-slate-900 text-center">Welcome to Performance Management System</h1>
      <Button variant = "outline">Click Me</Button>
      
    </div>
  )
}

export default App
