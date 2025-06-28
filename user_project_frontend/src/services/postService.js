import axios from 'axios'

const API_URL = 'https://jsonplaceholder.typicode.com'

export const getAllPosts = async () => {
  const response = await axios.get(`${API_URL}/posts`)
  return response.data
}

export const getPostsByUser = async (userId) => {
  const response = await axios.get(`${API_URL}/users/${userId}/posts`)
  return response.data
}