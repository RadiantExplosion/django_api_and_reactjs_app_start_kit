const REQUEST = 'REQUEST';
const SUCCESS = 'SUCCESS';
const FAILURE = 'FAILURE';
const RECEIVED = 'RECEIVED';
const INIT 		= 'INIT';

function createRequestTypes(base) {
  const res = {};
  [REQUEST, SUCCESS, FAILURE, RECEIVED, INIT].forEach(type => res[type] = `${base}_${type}`);
  return res;
}

// export const LOGIN_REQUEST = '@@jwt/LOGIN_REQUEST';
// export const LOGIN_SUCCESS = '@@jwt/LOGIN_SUCCESS';
// export const LOGIN_FAILURE = '@@jwt/LOGIN_FAILURE';
//
// export const TOKEN_REQUEST = '@@jwt/TOKEN_REQUEST';
// export const TOKEN_RECEIVED = '@@jwt/TOKEN_RECEIVED';
// export const TOKEN_FAILURE = '@@jwt/TOKEN_FAILURE';

// Login events
export const LOGIN = createRequestTypes('@@jwt/LOGIN');
export const TOKEN = createRequestTypes('@@jwt/TOKEN');
export const REGISTER = createRequestTypes('@@jwt/REGISTER');

export const LOGOUT = createRequestTypes('@@jwt/LOGOUT'); // logout is always success
