export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    resolve({ data: 'API response data' });
  });
}
