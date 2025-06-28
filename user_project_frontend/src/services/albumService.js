
import axios from 'axios'

const API_URL = 'https://jsonplaceholder.typicode.com'

export const getAlbumsByUser = async (userId) => {
  const response = await axios.get(`${API_URL}/users/${userId}/albums`)
  return response.data
}
