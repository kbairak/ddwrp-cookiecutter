import ReactDOM from 'react-dom';
import React from 'react';

// Render with simple JS
const element = document.getElementById('js-div');
element.innerHTML = 'Hello from JS';

// Render with React
const wrapper = document.getElementById('react-div');
ReactDOM.render(<p>Hello from React</p>, wrapper);
