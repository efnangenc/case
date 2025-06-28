
import axios from 'axios'

const API_URL = 'https://jsonplaceholder.typicode.com'

export const getPhotosByAlbum = async (albumId) => {
  const response = await axios.get(`${API_URL}/albums/${albumId}/photos`)
  return response.data
}
