body='{
"request": {
"branch":"test-python"
}}'

# urlencode / => %2F
project='sharkspeed%2Fsimple-code-for-travis-ci'

curl -s -X POST \
   -H "Content-Type: application/json" \
   -H "Accept: application/json" \
   -H "Travis-API-Version: 3" \
   -H "Authorization: token $CI_TOKEN" \
   -d "$body" \
   https://api.travis-ci.org/repo/$project/requests
