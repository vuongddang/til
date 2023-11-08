'use client'
import Image from 'next/image'
import { useEffect, useState } from 'react';

export default function Home() {

  const [message, setMessage] = useState(''); // State to store the message

  useEffect(() => {
    // Call dropwizard REST api
    const fetchData = async () => {
      try {
        const response = await fetch('/api/hello');
        const helloDto = await response.json();
        setMessage(helloDto.message);
      } catch (error) {
        console.error('Error fetching data:', error);
        setMessage('Failed to load message');
      }
    };

    fetchData();
  }, []);
  
  return (
    <main className="container flex items-center p-4 mx-auto min-h-screen justify-center">
        <p className="font-mono text-sm xl:text-xl code p-4 bg-gradient-to-r from-indigo-500 via-blue-500 to-blue-400 rounded text-transparent bg-clip-text">
          {message}
        </p>
    </main>
  )
}
