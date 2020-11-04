
export default function Card(slot) {
  const price = parseFloat(slot.price).toFixed(2)

  return (
    <div class="max-w-sm rounded overflow-hidden shadow sm:shadow-md md:shadow-lg lg:shadow-xl xl:shadow-2xl">
        <div class='overflow-hidden h-48'>
            <img class="w-full" src={slot.imageUrl} alt="Sunset in the mountains" />
        </div>
        <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">{slot.name}</div>
            <p class="text-gray-700 text-base">
                
            </p>
        </div>
        <div class="px-6 pt-4 pb-2">
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">R$ {price}</span>
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">Qt {slot.quantity}</span>
        </div>
    </div>
)
}
