import { AppBar, Toolbar, Typography } from "@mui/material";
import { Link } from "react-router-dom";

export const NavBar: React.FunctionComponent = () => {
    return (
        <header>
            <AppBar position="static"><Toolbar>
                <Link to={{
                    pathname: "/",
                }}>
                    <Typography variant="h6" color="inherit" component="div">
                        Robot
                    </Typography>
                </Link></Toolbar></AppBar>
        </header>
    );
}

export default NavBar;