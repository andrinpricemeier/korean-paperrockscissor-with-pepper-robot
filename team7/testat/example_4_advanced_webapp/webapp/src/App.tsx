import React from 'react';
import './App.css';
import { Container, CssBaseline, ThemeProvider } from '@mui/material';
import { NavBar } from './common/NavBar';
import { Footer } from './common/Footer';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import MainPage from './mainpage/MainPage';

export const App: React.FunctionComponent = () => {
  return (
    <Router>
      <CssBaseline />
      <NavBar />
      <main>
        <Container >
          <Switch>
            <Route component={MainPage} />
          </Switch>
        </Container>
      </main>
      <Footer />
    </Router>
  );
}

export default App;
