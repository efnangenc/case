
import axios from 'axios'

import { API_URL } from './apiConfig'

export const getTodosByUser = async (userId) => {
  const response = await axios.get(`${API_URL}/users/${userId}/todos`)
  return response.data
}
