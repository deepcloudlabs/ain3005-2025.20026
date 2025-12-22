export const API_OPTIONS = {
    GET: {
        method: "GET",
        headers: {
            "Accept": "application/json"
        }
    },
    DELETE: {
        method: "DELETE",
        headers: {
            "Accept": "application/json"
        }
    },
    POST: {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    },
    PUT: {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    }
};

export default async function callApi(url, options) {
    return await fetch(`http://localhost:7001/hr/api/v1/employees${url}`, options).then(res => res.json());
}
