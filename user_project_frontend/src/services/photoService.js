
import axios from 'axios'

import { API_URL } from './apiConfig'

export const getPhotosByAlbum = async (albumId) => {
  const response = await axios.get(`${API_URL}/albums/${albumId}/photos`)
  return response.data
}
