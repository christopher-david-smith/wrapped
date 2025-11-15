export const API = {

  Gifts: {

    async all() {
      const response = await fetch("http://127.0.0.1:8000/gifts/")
      console.log(response);
      if (!response.ok) {
        console.log(response);
        throw new Error(`Request failed: ${response.status}`)
      }
      return response.json()
    }

  }

};
