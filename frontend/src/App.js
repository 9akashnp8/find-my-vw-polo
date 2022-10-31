import Card from './components/Card';

function App() {
  return (
    <div className='mx-20'>
      <h1 className='text-3xl bold py-5'>Find My Polo</h1>
      <div className='grid grid-cols-3 gap-5'>
        <Card/>
      </div>
    </div>
  );
}

export default App;
