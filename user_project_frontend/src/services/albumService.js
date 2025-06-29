
import axios from 'axios'

import { API_URL } from './apiConfig'

export const getAlbumsByUser = async (userId) => {
  const response = await axios.get(`${API_URL}/users/${userId}/albums`)
  return response.data
}
