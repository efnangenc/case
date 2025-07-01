import axios from 'axios'
import { API_URL } from './apiConfig'

export const getUsers = async () => {
  const response = await axios.get(`${API_URL}/users`)
  return response.data
}

export const getUserDetail = async (id) => {
  const response = await axios.get(`${API_URL}/users/${id}`)
  return response.data
}
