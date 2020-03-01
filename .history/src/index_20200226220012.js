import Post from './Post'
import json from './assets/json'
import './styles/style.css'

const post = new Post('Webpack post title')
console.log('Post to string: ', post.toString())