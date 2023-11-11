import { AppBar, Toolbar, Typography } from "@mui/material";

export const Footer: React.FunctionComponent = () => {
    return (
        <footer>
        <AppBar position="static" color="primary">
            <Toolbar>
              <Typography variant="body1" color="inherit">
                © 2021 Copyright Team 7
              </Typography>
            </Toolbar>
        </AppBar>
        </footer>
    );
  }
  
  export default Footer;