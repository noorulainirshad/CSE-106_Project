function login() {
    
    userName = $('#username').val()
    password =  $('#password').val()

    // if input fields are empty

    if (username == '' || password == '') {
        console.log('input fields not filled')
    } else {
        const loginInput = {
            u_userName: userName,
            u_password: password
        }

        fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginInput)
        })
        .then((response) => {
            console.log('login successful')
        })
        .catch((response) => {
            console.log('login request was unsuccessful')
        })
    }
}