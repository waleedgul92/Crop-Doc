import React from 'react'
import { Lilita_One } from 'next/font/google'


function sidebar() {
  return (
    <>
      <div className='flex flex-col w-fit h-screen mt-5 bg-[#5757ff] text-[#ffdd00] text-xl border-t-4 border-r-4 border-white rounded-tr-xl'>
        <ul className='mt-5'>
          <li className='p-5 font-extrabold hover:bg-blue-500 hover:text-white hover:cursor-pointer transition-colors duration-300'>Import Photo</li>
          <li className='p-5 font-extrabold hover:bg-blue-500 hover:text-white hover:cursor-pointer transition-colors duration-300'>Capture New Photo</li>
          <li className='p-5 font-extrabold hover:bg-blue-500 hover:text-white hover:cursor-pointer transition-colors duration-300'>Capture New Video</li>
        </ul>

      </div>
    </>
  )
}

export default sidebar