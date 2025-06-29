import axios from 'axios'

const API_URL = 'https://jsonplaceholder.typicode.com'

export const getAllComments = async () => {
  const response = await axios.get(`${API_URL}/comments`)
  return response.data
}

export const getCommentsByPost = async (postId) => {
  const response = await axios.get(`${API_URL}/posts/${postId}/comments`)
  return response.data
}