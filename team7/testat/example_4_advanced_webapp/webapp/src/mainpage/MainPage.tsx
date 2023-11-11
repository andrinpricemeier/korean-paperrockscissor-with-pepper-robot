import { useEffect } from "react";

export const MainPage: React.FunctionComponent = () => {
    useEffect(() => {
        document.title = "Robot";
    }, []);

    return (
        <div>
            <h1>Robot</h1>
        </div>
    );
}

export default MainPage;