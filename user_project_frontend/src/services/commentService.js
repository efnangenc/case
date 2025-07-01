import axios from 'axios'
import { API_URL } from './apiConfig'

export const getAllComments = async () => {
  const response = await axios.get(`${API_URL}/comments`)
  return response.data
}

export const getCommentsByPost = async (postId) => {
  const response = await axios.get(`${API_URL}/posts/${postId}/comments`)
  return response.data
}