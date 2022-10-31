
export default function Card() {
    return (
        <div className="bg-slate-100 drop-shadow-md p-8">
            <h1 className="text-xl font-bold">
                Volkswagen Polo GT TSI, 2014, Petrol
            </h1>
            <div className='grid grid-cols-2 gap-2 py-5'>
                <div className='p-1 rounded flex'>
                    <p className='bg-slate-700 rounded-l  p-2 w-full text-center text-white'>20,000 KM</p>
                    <p className='bg-slate-200 rounded-r  p-2'>5.0</p>
                </div>
                <div className='p-1 rounded flex'>
                    <p className='bg-slate-700 rounded-l  p-2 w-full text-center text-white'>₹ 7,20,000</p>
                    <p className='bg-slate-200 rounded-r  p-2'>5.0</p>
                </div>
                <div className='p-1 rounded flex'>
                    <p className='bg-slate-700 rounded-l  p-2 w-full text-center text-white'>2022</p>
                    <p className='bg-slate-200 rounded-r  p-2'>5.0</p>
                </div>
                <div className='p-1 rounded flex'>
                    <p className='bg-slate-700 rounded-l  p-2 w-full text-center text-white'>Ottapalam</p>
                    <p className='bg-slate-200 rounded-r  p-2'>5.0</p>
                </div>
            </div>
        </div>
    )
}