const api_url =
      "http://127.0.0.1:8000/api"

async function getapi(url) {
    const response = await fetch(url)

    let data = await response.json()
    console.log(data)
    return data
}

function show(data) {
    let HTMLData = `<p>
        Name: ${data.name}
        Surname: ${data.surname}
        Age: ${data.age}
    </p>`
    document.getElementById("data").innerHTML = HTMLData
}

let data = await getapi(api_url)

show(data)