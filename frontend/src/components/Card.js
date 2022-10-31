
export default function Card({ adTitle, askingPrice, modelYear, kmsDriven, adLocation }) {
    return (
        <div className="bg-slate-100 drop-shadow-md p-8">
            <h1 className="text-xl font-bold">
                {adTitle}
            </h1>
            <div className='grid grid-cols-2 gap-2 py-5'>
                <div className='p-1 rounded flex'>
                    <p className='bg-slate-700 rounded-l  p-2 w-full text-center text-white'>{kmsDriven}</p>
                    <p className='bg-slate-200 rounded-r  p-2'>5.0</p>
                </div>
                <div className='p-1 rounded flex'>
                    <p className='bg-slate-700 rounded-l  p-2 w-full text-center text-white'>{askingPrice}</p>
                    <p className='bg-slate-200 rounded-r  p-2'>5.0</p>
                </div>
                <div className='p-1 rounded flex'>
                    <p className='bg-slate-700 rounded-l  p-2 w-full text-center text-white'>{modelYear}</p>
                    <p className='bg-slate-200 rounded-r  p-2'>5.0</p>
                </div>
                <div className='p-1 rounded flex'>
                    <p className='bg-slate-700 rounded-l  p-2 w-full text-center text-white'>{adLocation}</p>
                    <p className='bg-slate-200 rounded-r  p-2'>5.0</p>
                </div>
            </div>
        </div>
    )
}