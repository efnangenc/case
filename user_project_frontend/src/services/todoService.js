
import axios from 'axios'

const API_URL = 'https://jsonplaceholder.typicode.com'

export const getTodosByUser = async (userId) => {
  const response = await axios.get(`${API_URL}/users/${userId}/todos`)
  return response.data
}
