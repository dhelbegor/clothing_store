import Nav from '../components/nav'
import Card from '../components/card'
import useSwr from 'swr'

const fetcher = (...args) => fetch(...args).then((res) => res.json())

export default function IndexPage() {
  const url = 'http://localhost:8000/api/stock/products/'
  const { data, error } = useSwr(url, fetcher)

  if (error) return <div>Failed to load products</div>
  if (!data) return <div>Loading...</div>

  const cardList = data.results.map((product) => {
    return <Card
        name={product.name}
        sku={product.sku}
        quantity={product.quantity}
        price={product.price}
        category={product.category}
        imageUrl={product.image_url} 
    />
  })
  return (
    <div>
      <Nav />
      <div className="">
        <h1 className="text-5xl text-center text-accent-1 mb-100">
            Loja de Roupas da tia Clotilde
        </h1>
        <div className='container mx-auto'>
            <div className='grid grid-cols-4 gap-4'>{cardList}</div>
        </div>
      </div>
    </div>
  )
}
