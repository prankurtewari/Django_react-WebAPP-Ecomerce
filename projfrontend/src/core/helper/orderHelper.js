import { API } from "../../backend";

export const createOrder = (userId, token, orderData) => {
  const formData = new FormData();

  for (const name in orderData) {
    formData.append(name, orderData[name]);
  }

  return fetch(`http://localhost:8000/api/order/add/${userId}/${token}/`, {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      return response.json();
    })
    .catch((err) => console.log(err));
};
