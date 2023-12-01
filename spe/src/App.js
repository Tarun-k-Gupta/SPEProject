import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
       <header>
        <h1>Sentiment Analysis</h1>
    </header>

    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>

    <main>
        <p>Enter your text:</p>
        <input type="text" id="textInput" placeholder="Type here..."/>
        <button onclick="showEnteredText()">Submit</button>
        <p id="output"></p>
    </main>

    <footer>
        <p>&copy; Made with love ❤️ by Tarun and Likhith</p>
    </footer>
    </div>
  );
}

export default App;
