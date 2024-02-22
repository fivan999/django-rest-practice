const loginForm = document.getElementById('login-form')
const contentContainer = document.getElementById('content-container')
const searchForm = document.getElementById('search-form')
const baseEndpoint = 'http://localhost:8000/api'
if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}
if (searchForm){
    searchForm.addEventListener('submit', getProductList)
}
console.log(searchForm)

function handleLogin(event) {
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/auth/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData  = Object.fromEntries(loginFormData)
    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(loginObjectData)
    }
    fetch(loginEndpoint, options).then(response=>{
        return response.json()
    }).then(authData => {
        handleAuthData(authData, getProductList)
    })
}

function handleAuthData(authData, callback){
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback){
        callback()
    }
}

function isTokenValid(jsonData) {
    if (jsonData.code && jsonData.code === 'token_not_valid'){
        alert('Войдите в аккаунт снова')
        return false
    } return true
}

function validateJWTToken(){
    const endpoint = `${baseEndpoint}/auth/token/verify/`
    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify({
            token: localStorage.getItem('access')
        })
    }
    fetch(endpoint, options)
    .then(response=>response.json())
    .then(x => {
        isTokenValid(x)
    })
}

function getFetchOptions(method, body){
    return {
        method: method === null ? 'GET': method,
        headers: {
            'content-type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access')}`
        },
        body: body === null ? null: body
    }
}

function getProductList(event){
    let endpoint = `${baseEndpoint}/products/`
    if (event){
        event.preventDefault()
        let searchFormData = new FormData(searchForm)
        let searchData  = Object.fromEntries(searchFormData)
        searchParams = new URLSearchParams(searchData)
        endpoint = `${baseEndpoint}/products/?${searchParams}`
    }
    const options =  {
        method: 'GET',
        headers: {
            'content-type': 'application/json',
        }
    }
    console.log(endpoint)
    fetch(endpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(data=>{
        if (isTokenValid(data)) {
            writeInContentContainer(data)
        }
    })
}

function writeInContentContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = '<pre>' + JSON.stringify(data, null, 4) + '</pre>'
    }
}
