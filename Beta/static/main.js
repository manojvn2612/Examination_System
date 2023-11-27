function redirectlogin(params) {
    window.location.href = 'login.html';
}
function redirect_reg(params) {
    window.location.href = 'reg.html';
}
function redirect_set_q() {
    window.location.href = '{{ url_for('set_paper') }}';
}
