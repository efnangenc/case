import axios from "axios";

import { API_URL } from "./apiConfig";

// export const getPhotosByAlbum = async (albumId) => {
//   const response = await axios.get(`${API_URL}/albums/${albumId}/photos`)
//   return response.data
// }

// export const getPhotosByAlbum = async (albumId) => {
//   try {
//     const response = await axios.get(`${API_URL}/photos`)
//     const allPhotos = response.data

//     // Albüm ID'si eşleşenleri filtrele
//     const filteredPhotos = allPhotos.filter(photo => photo.albumId === parseInt(albumId))
//     return filteredPhotos
//   } catch (error) {
//     console.error('Fotoğraflar alınamadı:', error)
//     return []
//   }
// }

export const getPhotosByAlbum = async (albumId) => {
  const response = await axios.get(`${API_URL}/photos?albumId=${albumId}`)
  return response.data
}
