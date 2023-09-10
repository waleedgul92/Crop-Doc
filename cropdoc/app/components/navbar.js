import React from 'react'
import { Lilita_One } from 'next/font/google'

const lilita_one = Lilita_One({ 
    weight: '400',
    subsets: ['latin']

})

function navbar() {
  return (
    <nav className='outline outline-4 outline-white flex h-16 w-full bg-[#5757ff] p-5 text-[#ffdf00] text-3xl font-bold shadow-5xl rounded-bl-3xl rounded-br-3xl'>
        <a href='/'><h3 className={lilita_one.className}>Crop Doc🌱</h3></a>
    </nav>
  )
}

export default navbar