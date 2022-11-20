import Card from './components/Card';
import axios from 'axios';
import useSWR from 'swr';

async function dataFetcher(url) {
  return await axios.get(url).then(res => res.data.data[0])
}

function App() {

  const {data, setData} = useSWR("http://127.0.0.1:8000/polo/", dataFetcher)

  return (
    <div className='mx-20'>
      <h1 className='text-3xl bold py-5'>Find My Polo</h1>
      <div className='grid grid-cols-3 gap-5'>
        {data?.map((listing) => {
          return (
            <Card
              key={listing._id}
              adTitle={listing.ad_title}
              askingPrice={listing.ad_price}
              modelYear={listing.model_year}
              kmsDriven={listing.kms_driven}
              adLocation={listing.ad_location}            
            />
          )
        })}
      </div>
    </div>
  );
}

export default App;
