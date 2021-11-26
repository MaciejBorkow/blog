import {useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';
import Cookies from 'js-cookie';


function getArticle(id, setArticle) {
    const url = 'http://127.0.0.1:8000/api/article/33/'
    axios.get(url)
      .then(response => setArticle(response.data))
      .catch(err => console.log(err))
}

function putArticle() {
  const url = 'http://127.0.0.1:8000/api/article/33/'
  const data = {title:"react put!!!"}
  axios.put(url, data, {headers: {'X-CSRFToken': Cookies.get("csrftoken")}})
      .then(response => console.log(response.data))
      .catch(err => console.log(err))
}


function App() {
  const my_obj = {name: 'maciej'}
  const [article, setArticle] = useState({title:'loading'})
  useEffect(() => getArticle(123, setArticle), [])

  return (
    <div className="App">
      my app: {article.title}
      <button onClick={putArticle}>Put data</button>
    </div>
  );
}

export default App;
