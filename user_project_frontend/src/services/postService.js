import axios from 'axios'

import { API_URL } from './apiConfig'

export const getAllPosts = async () => {
  const response = await axios.get(`${API_URL}/posts`)
  return response.data
}

export const getPostsByUser = async (userId) => {
  const response = await axios.get(`${API_URL}/users/${userId}/posts`)
  return response.data
}