export const API = {

  Gifts: {

    async all() {
      const response = await fetch("http://127.0.0.1:8000/gifts/")
      if (!response.ok) {
        throw new Error(`Request failed: ${response.status}`)
      }
      return response.json()
    },

    async add(data: any) {
      const response = await fetch("http://127.0.0.1:8000/gifts/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name: data.name
        })
      });
      if (!response.ok)
        throw new Error(`Request failed: ${response.status}`);
      return response.json()
    },

    async delete(id: number) {
      const response = await fetch(`http://127.0.0.1:8000/gifts/${id}`, {
        method: "DELETE"
      })
      if (!response.ok)
        throw new Error(`Request failed: ${response.status}`);
      return response.json()
    }
  }

};
